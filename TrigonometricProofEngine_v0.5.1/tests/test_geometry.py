import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import engine
from geometry import GEOMETRIC_CERTIFICATE_SCHEMA, verify_geometric_certificate, _certificate_digest


class GeometricF08Tests(unittest.TestCase):
    def prove(self, lhs, rhs):
        result = engine.prove_identity(lhs, rhs)
        self.assertEqual(result.status, 'PROVED')
        self.assertEqual(result.selected_route, 'GEO: G01 → G03 → G04')
        self.assertEqual(result.rule_ids, ('G01', 'G03', 'G04'))
        self.assertEqual(result.used_theorems, [])
        certificate = result.to_certificate()
        self.assertEqual(certificate['schema'], GEOMETRIC_CERTIFICATE_SCHEMA)
        valid, reason = verify_geometric_certificate(
            certificate, engine.parse_expression, result.lhs, result.rhs, result.domain_conditions
        )
        self.assertTrue(valid, reason)
        return result

    def test_canonical_f08(self):
        self.prove('sin(x)**2 + cos(x)**2', '1')

    def test_reversed_f08(self):
        self.prove('1', 'sin(t)**2 + cos(t)**2')

    def test_rearranged_f08(self):
        self.prove('sin(t)**2', '1 - cos(t)**2')

    def test_scaled_f08(self):
        self.prove('2*sin(t)**2 + 2*cos(t)**2', '2')

    def test_arbitrary_angle_expression(self):
        self.prove('sin(2*t + 1)**2 + cos(2*t + 1)**2', '1')

    def test_original_domain_is_preserved_for_scaled_relation(self):
        result = self.prove('(sin(x)**2 + cos(x)**2)/x', '1/x')
        self.assertEqual(result.domain_conditions, ['x ≠ 0'])
        self.assertEqual(result.to_certificate()['original_domain_conditions'], ['x ≠ 0'])

    def test_formal_match_does_not_assume_unrelated_angles(self):
        result = engine.prove_identity('sin(x)**2 + cos(y)**2', '1')
        self.assertEqual(result.status, 'DISPROVED')

    def test_certificate_has_no_trigonometric_premises(self):
        certificate = self.prove('sin(x)**2 + cos(x)**2', '1').to_certificate()
        self.assertEqual(certificate['used_identity_ids'], [])
        self.assertEqual(certificate['assumptions'], [])
        self.assertEqual(certificate['open_assumptions'], [])
        self.assertNotIn('F08', certificate['dependencies'])
        self.assertNotIn('F09', certificate['dependencies'])
        self.assertNotIn('F10', certificate['dependencies'])
        self.assertEqual(
            [node['node_id'] for node in certificate['proof_nodes']],
            ['G01', 'G03', 'G04', 'GOAL'],
        )

    def test_certificate_tampering_is_rejected(self):
        result = self.prove('sin(x)**2 + cos(x)**2', '1')
        certificate = dict(result.to_certificate())
        certificate['used_identity_ids'] = ['F08']
        valid, reason = verify_geometric_certificate(
            certificate, engine.parse_expression, result.lhs, result.rhs, result.domain_conditions
        )
        self.assertFalse(valid)
        self.assertIn('used_identity_ids', reason)

    def test_certificate_digest_is_checked(self):
        result = self.prove('sin(x)**2 + cos(x)**2', '1')
        certificate = dict(result.to_certificate())
        certificate['certificate_digest'] = '0' * 64
        valid, reason = verify_geometric_certificate(
            certificate, engine.parse_expression, result.lhs, result.rhs, result.domain_conditions
        )
        self.assertFalse(valid)
        self.assertIn('digest', reason)

    def test_f08_catalogue_theorem_is_not_admitted_for_f08_goal(self):
        catalogue = engine.load_catalogue_theorems()
        admitted = engine._independent_premises(
            engine.parse_expression('sin(x)**2 + cos(x)**2'),
            engine.parse_expression('1'), [], catalogue,
        )
        self.assertFalse({'F08', 'F09', 'F10', 'F11', 'F12'} & {t.identity_id for t in admitted})

    def test_catalogue_dependents_require_geometric_replay(self):
        catalogue = engine.load_catalogue_theorems()
        with patch.object(engine, '_verified_geometric_f08_foundation', return_value=False):
            admitted = engine._independent_premises(
                engine.parse_expression('sin(x)'), engine.parse_expression('cos(x)'), [], catalogue
            )
        self.assertFalse({'F08', 'F09', 'F10', 'F11', 'F12'} & {t.identity_id for t in admitted})

    def test_forged_v4_f08_certificate_cannot_bypass_geometric_replay(self):
        forged = {
            "name": "Forged legacy F08",
            "lhs": "sin(x)**2 + cos(x)**2",
            "rhs": "1",
            "proof_certificate": {
                "schema": "trigonometric-proof-certificate-v4",
                "status": "PROVED",
                "claim": {"lhs": "sin(x)**2 + cos(x)**2", "rhs": "1"},
                "used_theorems": [],
                "steps": [],
            },
        }
        supplied = engine.parse_theorem_premises([forged])
        admitted = engine._independent_premises(
            engine.parse_expression("sin(x)"), engine.parse_expression("cos(x)"),
            supplied, engine.load_catalogue_theorems(), include_catalogue=False,
        )
        self.assertEqual(admitted, [])

    def test_f08_is_admitted_as_dependency_only_after_geometric_replay(self):
        result = self.prove('sin(x)**2 + cos(x)**2', '1')
        saved = {
            'name': 'Geometric F08',
            'lhs': str(result.lhs),
            'rhs': str(result.rhs),
            'source': 'Trigonometric Proof Engine v0.5.1 GEO certificate',
            'domain_conditions': result.domain_conditions,
            'proof_certificate': result.to_certificate(),
        }
        supplied = engine.parse_theorem_premises([saved])
        catalogue = engine.load_catalogue_theorems()
        admitted = engine._independent_premises(
            engine.parse_expression('sin(x)'), engine.parse_expression('cos(x)'),
            supplied, catalogue, include_catalogue=False,
        )
        self.assertEqual(len(admitted), 1)
        self.assertEqual(admitted[0].name, 'Geometric F08')

    def test_modified_domain_ledger_is_rejected_even_with_recomputed_digest(self):
        result = self.prove('sin(x)**2 + cos(x)**2', '1')
        certificate = dict(result.to_certificate())
        certificate['original_domain_conditions'] = ['x ≠ 0']
        certificate['certificate_digest'] = _certificate_digest(certificate)
        valid, reason = verify_geometric_certificate(
            certificate, engine.parse_expression, result.lhs, result.rhs, result.domain_conditions
        )
        self.assertFalse(valid)
        self.assertIn('original-domain', reason)

    def test_geometry_route_does_not_call_trig_simplifier(self):
        with patch.object(engine.sp, 'trigsimp', side_effect=AssertionError('trigsimp must not prove F08')):
            result = engine.prove_identity('sin(x)**2 + cos(x)**2', '1')
        self.assertEqual(result.status, 'PROVED')
        self.assertEqual(result.selected_route, 'GEO: G01 → G03 → G04')


if __name__ == '__main__':
    unittest.main()
