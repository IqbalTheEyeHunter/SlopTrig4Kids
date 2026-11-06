import json,sys,subprocess,time
from pathlib import Path
root=Path(__file__).resolve().parent
catalog=json.loads((root/'candidate_catalog.json').read_text())['global']
start,end=map(int,sys.argv[1:3]); timeout=float(sys.argv[3]) if len(sys.argv)>3 else 20
results_path=root/'candidate_proofs.json'
results=json.loads(results_path.read_text()) if results_path.exists() else {}
for idx in range(start,end):
 c=catalog[idx]; key='|'.join(c['key'])
 if key in results:continue
 t=time.time()
 try:
  p=subprocess.run([sys.executable,'proof_worker_cli.py'],input=json.dumps({'lhs':c['lhs'],'rhs':c['rhs']}),text=True,capture_output=True,timeout=timeout)
  if p.returncode==0:
   out=json.loads(p.stdout.strip().splitlines()[-1])
  else:out={'status':'WORKER_ERROR','stderr':p.stderr[-2000:]}
 except subprocess.TimeoutExpired:out={'status':'TIMEOUT'}
 results[key]=out
 print(idx+1,'/',len(catalog),round(time.time()-t,2),out.get('status'),c['template'],c['lhs'],'=',c['rhs'],flush=True)
 results_path.write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
