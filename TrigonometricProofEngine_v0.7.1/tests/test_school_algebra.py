import copy
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import engine as e
import app
import school_algebra as school
from exercises import EXERCISES

class SchoolAlgebraTests(unittest.TestCase):
    def test_all_fourteen_have_checked_algebraic_chains(self):
        for year,lhs,rhs in EXERCISES:
            with self.subTest(year=year):
                result=e.prove_identity(lhs,rhs,'Use full identity catalogue')
                self.assertEqual(result.status,'PROVED')
                cert=result.to_certificate();trace=cert['student_proof']
                self.assertTrue(school.verify_trace(trace,result.lhs,result.rhs))
                self.assertTrue(e.verify_rotation_certificate(cert,result.lhs,result.rhs,result.domain_conditions)[0])
                current=e.parse_expression(trace['lhs'])
                for step in trace['steps']:
                    before=e.parse_expression(step['before']);after=e.parse_expression(step['after'])
                    self.assertEqual(current,before,'Gap in the displayed proof chain')
                    if step['kind']=='algebra':
                        self.assertTrue(school.algebra_equal(before,after))
                    else:
                        self.assertIsNotNone(e.build_rotation_certificate(before,after,[]))
                    current=after
                self.assertEqual(current,result.rhs)
                text=app.TrigProofApp._format_result(None,result)
                md=result.to_markdown()
                for report in (text,md):
                    for forbidden in ('ROTATION','coord_','POLYNOMIAL WITNESS','LCM','Groebner','rotation-coordinate'):
                        self.assertNotIn(forbidden,report)
                self.assertIn('ALGEBRAIC PROOF',text)
                self.assertIn('$$',md)

    def test_requested_example_has_visible_substitution(self):
        result=e.prove_identity('2/(1+cos(2*x))','sec(x)**2')
        self.assertEqual(result.to_certificate()['engine_version'],'0.7.1')
        trace=result.to_certificate()['student_proof']
        self.assertIn('2*cos(x)**2 - 1',trace['steps'][0]['after'])
        self.assertEqual(trace['steps'][-1]['after'],'sec(x)**2')
        self.assertLessEqual(len(trace['steps']),5)
        self.assertIn('cos(x) ≠ 0',result.domain_conditions)

    def test_original_compound_angle_form_is_visible(self):
        result=e.prove_identity(*EXERCISES[5][1:])
        trace=result.to_certificate()['student_proof']
        self.assertIn('cos(x - pi/4)',trace['lhs'])
        self.assertEqual(trace['steps'][0]['title'],'Use the compound-angle identity')

    def test_target_double_angle_is_not_cited_as_its_own_reason(self):
        result=e.prove_identity(*EXERCISES[-1][1:])
        steps=result.to_certificate()['student_proof']['steps']
        self.assertEqual(steps[0]['title'],'Use the compound-angle identity')
        self.assertIn('A = B',steps[0]['reason'])
        self.assertNotIn('Use the double-angle identity',[s['title'] for s in steps])

    def test_altered_explanations_are_rejected(self):
        result=e.prove_identity(*EXERCISES[3][1:])
        for field,value in [('after','1'),('reason','Assume the target is true.'),('after_latex','1')]:
            cert=result.to_certificate();cert['student_proof']['steps'][0][field]=value
            self.assertFalse(e.verify_rotation_certificate(cert,result.lhs,result.rhs,result.domain_conditions)[0])

    def test_v070_rotation_certificate_remains_replayable(self):
        cert=json.loads((Path(__file__).parent/'fixtures/v070_rotation_certificate.json').read_text())
        lhs=e.parse_expression(cert['claim']['lhs']);rhs=e.parse_expression(cert['claim']['rhs'])
        self.assertTrue(e.verify_rotation_certificate(cert,lhs,rhs,cert['domain_conditions'])[0])

    def test_generic_renamed_and_scaled_angle_inputs(self):
        for lhs,rhs in [('2/(1+cos(6*t))','sec(3*t)**2'),
                        ('tan(z/3)+cot(z/3)','2*csc(2*z/3)'),
                        ('sin(a+b)','sin(a)*cos(b)+cos(a)*sin(b)')]:
            result=e.prove_identity(lhs,rhs)
            self.assertEqual(result.status,'PROVED')
            self.assertTrue(result.to_certificate().get('student_proof'))

if __name__=='__main__':unittest.main(verbosity=2)
