import json,sys
import sympy as sp
import engine
from geometry import verify_geometric_certificate
payload=json.load(sys.stdin)
engine._find_counterexample=lambda *args,**kwargs:None
r=engine.prove_identity(payload['lhs'],payload['rhs'],'Automatic')
out={'status':r.status,'domain':list(r.domain_conditions),'route':r.selected_route,'rule_ids':list(r.rule_ids)}
if r.status=='PROVED':
 cert=r.to_certificate()
 if cert.get('schema')=='trigonometric-geometric-proof-certificate-v1':
  valid,reason=verify_geometric_certificate(cert,engine.parse_expression,r.lhs,r.rhs,r.domain_conditions)
  if not valid:out={'status':'REJECTED_CERTIFICATE','reason':reason}
 else:
  checks=[s.get('symbolic_equivalence_check') for s in cert.get('steps',[])]
  if any(v is False for v in checks):out={'status':'REJECTED_STEP_CHECK'}
 out['certificate']=cert
 out['steps']=[{'title':s.title,'expression':sp.sstr(s.expression),'previous_expression':None if s.previous_expression is None else sp.sstr(s.previous_expression),'note':s.note,'rule_ids':list(s.rule_ids),'side':s.side,'theorem_ref':s.theorem_ref,'domain_conditions':list(s.domain_conditions),'substitution':{a:b for a,b in s.substitution}} for s in r.steps]
print(json.dumps(out,ensure_ascii=False))
