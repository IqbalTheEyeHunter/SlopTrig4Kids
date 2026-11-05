import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import engine as e

class CircularityTests(unittest.TestCase):
    def test_f08_all_modes(self):
        for mode in ('Automatic', 'LHS to RHS', 'RHS to LHS', 'Both sides to common form',
                     'Difference method', 'Angle expansion first', 'Fu transformations first',
                     'Algebraic reduction first', 'Use supplied identities', 'Use full identity catalogue'):
            with self.subTest(mode=mode):
                r = e.prove_identity('sin(x)**2+cos(x)**2', '1', mode)
                self.assertEqual(r.status, 'PROVED')
                self.assertEqual(r.selected_route, 'GEO: G01 → G03 → G04')
                self.assertEqual(r.rule_ids, ('G01', 'G03', 'G04'))
                self.assertEqual(r.used_theorems, [])
                self.assertEqual(r.to_certificate()['schema'], 'trigonometric-geometric-proof-certificate-v1')
    def test_equivalent_targets(self):
        for left,right in [('1','sin(t)**2+cos(t)**2'), ('sin(t)**2','1-cos(t)**2'),
                           ('2*sin(t)**2+2*cos(t)**2','2'),
                           ('sin(2*t)**2+cos(2*t)**2','1')]:
            result = e.prove_identity(left,right)
            self.assertEqual(result.status,'PROVED')
            self.assertEqual(result.rule_ids, ('G01', 'G03', 'G04'))
    def test_dependency_closure(self):
        cat=e.load_catalogue_theorems()
        admitted=e._independent_premises(e.parse_expression('sin(x)**2+cos(x)**2'),e.parse_expression('1'),[],cat)
        self.assertFalse({'F08','F09','F10','F11','F12'} & {t.identity_id for t in admitted})
    def test_renamed_self_premise(self):
        r=e.prove_identity('sin(x)**2+cos(x)**2','1',premises=['Other: sin(t)**2+cos(t)**2=1'])
        self.assertEqual(r.status,'PROVED')
        self.assertEqual(r.selected_route, 'GEO: G01 → G03 → G04')
        self.assertEqual(r.used_theorems, [])
    def test_legacy_certificate_cannot_bypass(self):
        premise={'name':'Old F09','lhs':'1+tan(x)**2','rhs':'sec(x)**2',
                 'proof_certificate':{'schema':'trigonometric-proof-certificate-v3','status':'PROVED'}}
        r=e.prove_identity('sin(x)**2+cos(x)**2','1',premises=[premise])
        self.assertEqual(r.status,'PROVED')
        self.assertEqual(r.selected_route, 'GEO: G01 → G03 → G04')
        self.assertEqual(r.used_theorems, [])
    def test_no_opaque_fallback(self):
        with patch.object(e,'_simplify_side',side_effect=AssertionError), patch.object(e,'_difference_route',side_effect=AssertionError), patch.object(e,'_common_form_route',side_effect=AssertionError):
            result = e.prove_identity('sin(x)**2+cos(x)**2','1')
            self.assertEqual(result.status,'PROVED')
            self.assertEqual(result.selected_route, 'GEO: G01 → G03 → G04')
    def test_valid_multi_identity_proof(self):
        r=e.prove_identity('1+tan(x)**2','1/cos(x)**2','Use full identity catalogue')
        self.assertEqual(r.status,'PROVED')
        self.assertEqual(r.rule_ids,('F09','F03'))
        self.assertTrue(r.domain_conditions)
        provenance = r.to_certificate()['dependency_provenance']
        self.assertIn('F08 depends on GEO.F08', provenance)
        self.assertIn('GEO.F08 is admitted only after replaying G01 → G03 → G04', provenance)
    def test_algebra_and_false_claim(self):
        self.assertEqual(e.prove_identity('2*sin(x)','sin(x)+sin(x)').status,'PROVED')
        self.assertEqual(e.prove_identity('sin(x)','cos(x)').status,'DISPROVED')
    def test_cycle_and_missing_provenance(self):
        cat=e.load_catalogue_theorems()
        with patch.dict(e.AUDITED_DEPENDENCIES,{'F09':('F11',),'F11':('F09',)}):
            allowed=e._independent_premises(e.parse_expression('sin(x)'),e.parse_expression('cos(x)'),[],cat)
            self.assertFalse({'F09','F11','A01'} & {t.identity_id for t in allowed})
    def test_certificate_roundtrip(self):
        r=e.prove_identity('1+tan(x)**2','1/cos(x)**2','Use full identity catalogue')
        saved={'name':'Saved','lhs':str(r.lhs),'rhs':str(r.rhs),'proof_certificate':r.to_certificate()}
        cat=e.load_catalogue_theorems()
        allowed=e._independent_premises(e.parse_expression('sin(y)'),e.parse_expression('cos(y)'),e.parse_theorem_premises([saved]),cat,False)
        self.assertEqual(len(allowed),1)
        allowed=e._independent_premises(e.parse_expression('sin(x)**2+cos(x)**2'),e.parse_expression('1'),e.parse_theorem_premises([saved]),cat,False)
        self.assertEqual(allowed,[])
if __name__=='__main__': unittest.main()
