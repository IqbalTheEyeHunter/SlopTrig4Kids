import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import sympy as sp
import engine as e
import rotation_proof as r
from exercises import EXERCISES
import app

class RotationProofTests(unittest.TestCase):
    def test_all_fourteen_in_both_main_modes(self):
        for method in ('Automatic','Use full identity catalogue'):
            for year,lhs,rhs in EXERCISES:
                with self.subTest(year=year,method=method):
                    result=e.prove_identity(lhs,rhs,method)
                    self.assertEqual(result.status,'PROVED')
                    cert=result.to_certificate()
                    self.assertEqual(cert['schema'],r.SCHEMA)
                    self.assertTrue(r.verify_certificate(cert,result.lhs,result.rhs,result.domain_conditions)[0])
                    self.assertEqual(result.used_theorems,[])
                    self.assertIn('ALGEBRAIC PROOF',app.TrigProofApp._format_result(None,result))
                    self.assertIn('$$',result.to_markdown())

    def test_fourteen_false_near_misses(self):
        for year,lhs,rhs in EXERCISES:
            with self.subTest(year=year):
                result=e.prove_identity(lhs,'('+rhs+')+1','Use full identity catalogue')
                self.assertEqual(result.status,'DISPROVED')
                self.assertIsNotNone(result.counterexample)

    def test_generic_angles_not_exercise_lookup(self):
        cases=[
            ('sin(a+b)','sin(a)*cos(b)+cos(a)*sin(b)'),
            ('cos(a-b)','cos(a)*cos(b)+sin(a)*sin(b)'),
            ('sin(3*t)','3*sin(t)-4*sin(t)**3'),
            ('cos(4*t)','8*cos(t)**4-8*cos(t)**2+1'),
            ('tan(z/3)+cot(z/3)','2*csc(2*z/3)'),
            ('sin(x/3+y/2)','sin(x/3)*cos(y/2)+cos(x/3)*sin(y/2)'),
            ('sin(x+pi/12)','sin(x)*(sqrt(6)+sqrt(2))/4+cos(x)*(sqrt(6)-sqrt(2))/4'),
            ('sin(-2*x)','-2*sin(x)*cos(x)'),
            ('coord_C0*sin(2*x)','2*coord_C0*sin(x)*cos(x)'),
        ]
        for lhs,rhs in cases:
            with self.subTest(lhs=lhs):
                cert=r.build_certificate(e.parse_expression(lhs),e.parse_expression(rhs),[])
                self.assertIsNotNone(cert)

    def test_no_trigonometric_or_numerical_oracle(self):
        lhs=e.parse_expression('tan(x)+cot(x)');rhs=e.parse_expression('2*csc(2*x)')
        r.circle_foundation()  # Existing geometric foundation has its own checker.
        with patch('sympy.trigsimp',side_effect=AssertionError('oracle')), \
             patch('sympy.expand_trig',side_effect=AssertionError('oracle')), \
             patch('engine._symbolically_equivalent',side_effect=AssertionError('oracle')), \
             patch('engine._find_counterexample',side_effect=AssertionError('oracle')):
            self.assertIsNotNone(r.build_certificate(lhs,rhs,[]))

    def test_mutated_witnesses_fail_replay(self):
        result=e.prove_identity(*EXERCISES[0][1:])
        cert=result.to_certificate()
        mutations={
            'status':'INCONCLUSIVE','remainder':'1','quotients':['0'],
            'cross_multiplied_numerator':'0','domain_conditions':[],
            'claim':{'lhs':'sin(x)','rhs':'cos(x)'},
            'angle_expansions':[], 'trusted_foundations':{},
            'circle_certificate':{}, 'circle_relations':['0'],
            'rational_forms':{'lhs':'1','rhs':'1'},
        }
        for key,value in mutations.items():
            with self.subTest(key=key):
                altered=copy.deepcopy(cert);altered[key]=value
                self.assertFalse(r.verify_certificate(altered,result.lhs,result.rhs,result.domain_conditions)[0])
        self.assertTrue(r.verify_certificate(result.to_certificate(),result.lhs,result.rhs,result.domain_conditions)[0])

    def test_original_domains(self):
        result=e.prove_identity(*EXERCISES[0][1:])
        self.assertEqual(set(result.domain_conditions),{'cos(x) ≠ 0','sin(x) ≠ 0','sin(2*x) ≠ 0'})
        result=e.prove_identity(*EXERCISES[9][1:])
        self.assertIn('sin(x) ≠ 0',result.domain_conditions)
        self.assertIn('cos(x/2) ≠ 0',result.domain_conditions)

    def test_decimal_literals_are_exact(self):
        self.assertEqual(e.parse_expression('0.5'),sp.Rational(1,2))
        self.assertEqual(e.parse_expression('0.1+0.2'),sp.Rational(3,10))
        self.assertEqual(e.parse_expression('1e-3'),sp.Rational(1,1000))
        self.assertEqual(e.parse_expression('0.1234567890123456789'),sp.Rational('0.1234567890123456789'))

    def test_unsupported_branches_fail_closed(self):
        for lhs,rhs in [('sqrt(sin(x)**2)','sin(x)'),('sin(x*x)','2*sin(x)'),
                        ('sin(x+pi/7)','sin(x)'),('sin(25*x)','sin(x)'),
                        ('1/(sin(x)**2+cos(x)**2-1)','0')]:
            with self.subTest(lhs=lhs):
                self.assertIsNone(r.build_certificate(e.parse_expression(lhs),e.parse_expression(rhs),[]))

    def test_self_premise_is_still_blocked(self):
        result=e.prove_identity(*EXERCISES[0][1:])
        premise={'name':'Saved','lhs':EXERCISES[0][1],'rhs':EXERCISES[0][2],
                 'domain_conditions':result.domain_conditions,'proof_certificate':result.to_certificate()}
        supplied=e.parse_theorem_premises([premise])
        self.assertEqual(e._independent_premises(result.lhs,result.rhs,supplied,e.load_catalogue_theorems(),False),[])

    def test_saved_rotation_theorem_reused_for_distinct_goal(self):
        result=e.prove_identity(*EXERCISES[0][1:])
        premise={'name':'Saved rotation proof','lhs':EXERCISES[0][1],'rhs':EXERCISES[0][2],
                 'domain_conditions':result.domain_conditions,'proof_certificate':result.to_certificate()}
        derived=e.prove_identity('(tan(x)+cot(x))*sin(x)','2*csc(2*x)*sin(x)',
                                 'Use supplied identities',[premise])
        self.assertEqual(derived.status,'PROVED')
        self.assertEqual(derived.used_theorems[0]['name'],'Saved rotation proof')
        premise['proof_certificate']['remainder']='1'
        with self.assertRaises(e.ExpressionInputError):
            e.parse_theorem_premises([premise])

if __name__=='__main__': unittest.main(verbosity=2)
