import json,sys,time
from pathlib import Path
import sympy as sp
import engine
from geometry import verify_geometric_certificate
root=Path(__file__).resolve().parent
catalog=json.loads((root/'candidate_catalog.json').read_text())['global']
start,end=map(int,sys.argv[1:3])
results_path=root/'candidate_proofs.json'
results=json.loads(results_path.read_text()) if results_path.exists() else {}
engine._find_counterexample=lambda *args,**kwargs:None
for idx in range(start,end):
 c=catalog[idx]; key='|'.join(c['key'])
 if key in results:continue
 t=time.time()
 try:
  r=engine.prove_identity(c['lhs'],c['rhs'],'Automatic')
  out={'status':r.status,'domain':list(r.domain_conditions),'route':r.selected_route,'rule_ids':list(r.rule_ids)}
  if r.status=='PROVED':
   cert=r.to_certificate()
   if cert.get('schema')=='trigonometric-geometric-proof-certificate-v1':
    valid,reason=verify_geometric_certificate(cert,engine.parse_expression,r.lhs,r.rhs,r.domain_conditions)
    if not valid:out={'status':'REJECTED_CERTIFICATE','reason':reason}
   elif cert.get('schema')==engine.ROTATION_SCHEMA:
    valid,reason=engine.verify_rotation_certificate(cert,r.lhs,r.rhs,r.domain_conditions)
    if not valid:out={'status':'REJECTED_CERTIFICATE','reason':reason}
   else:
    checks=[s.get('symbolic_equivalence_check') for s in cert.get('steps',[])]
    if any(v is False for v in checks):out={'status':'REJECTED_STEP_CHECK'}
   out['certificate']=cert
   out['steps']=[{'title':s.title,'expression':sp.sstr(s.expression),'previous_expression':None if s.previous_expression is None else sp.sstr(s.previous_expression),'note':s.note,'rule_ids':list(s.rule_ids),'side':s.side,'theorem_ref':s.theorem_ref,'domain_conditions':list(s.domain_conditions),'substitution':{a:b for a,b in s.substitution}} for s in r.steps]
 except Exception as exc:out={'status':'WORKER_ERROR','reason':repr(exc)}
 results[key]=out
 print(idx+1,'/',len(catalog),round(time.time()-t,2),out.get('status'),c['template'],c['lhs'],'=',c['rhs'],flush=True)
 results_path.write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
