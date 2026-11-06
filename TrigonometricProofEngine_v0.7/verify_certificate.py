"""Usage: python verify_certificate.py examples/spm_01_2003.json

Standalone replay entry point for geometric and rotation certificates.
Legacy v4 transformation records still use the engine's theorem-admission path.
"""
import argparse
import json
from pathlib import Path
import engine
from geometry import verify_geometric_certificate

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    args=parser.parse_args()
    try:
        cert=json.loads(args.certificate.read_text(encoding='utf-8'))
        lhs=engine.parse_expression(cert['claim']['lhs'])
        rhs=engine.parse_expression(cert['claim']['rhs'])
        domain=cert['domain_conditions']
        required=engine._domain_conditions(lhs,rhs)
        if not set(required).issubset(set(domain)):
            raise ValueError('Required original domain condition is missing')
        if cert['schema']==engine.ROTATION_SCHEMA:
            ok,reason=engine.verify_rotation_certificate(cert,lhs,rhs,domain)
        elif cert['schema']==engine.GEO_CERTIFICATE_SCHEMA:
            ok,reason=verify_geometric_certificate(cert,engine.parse_expression,lhs,rhs,domain)
        else:
            ok,reason=False,'Unsupported schema for this standalone checker'
    except (ValueError,KeyError,TypeError,OSError) as exc:
        ok,reason=False,str(exc)
    print(('VERIFIED: ' if ok else 'REJECTED: ')+reason)
    return 0 if ok else 1

if __name__=='__main__': raise SystemExit(main())
