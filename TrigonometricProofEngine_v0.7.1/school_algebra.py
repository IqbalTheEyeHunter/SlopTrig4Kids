"""SPM-facing proofs: ordinary trig identities, fractions, factoring and cancellation.

This module never imports the exercise list. It explores a few general
normalization paths from each side, then joins the shortest matching prefixes.
The rotation certificate remains a separate internal correctness check.
"""
from functools import lru_cache
import copy
import ast
import json
import sympy as sp
from rotation_proof import build_certificate

TRIG=(sp.sin,sp.cos,sp.tan,sp.cot,sp.sec,sp.csc)


def algebra_equal(a,b):
    try:
        return sp.cancel(sp.together(a-b)) == 0
    except (ValueError,TypeError,sp.PolynomialError):
        return False


def held_replace(expr, old, new):
    if expr == old:
        return new
    if not expr.args:
        return expr
    args=tuple(held_replace(a,old,new) for a in expr.args)
    if args==expr.args:
        return expr
    if expr.func in (sp.Add,sp.Mul,sp.Pow):
        return expr.func(*args,evaluate=False)
    return expr.func(*args)


def evaluate_algebra(expr):
    """Evaluate arithmetic nodes without invoking trigonometric simplification."""
    if not expr.args:
        return expr
    if expr.func in TRIG:
        return expr
    return expr.func(*(evaluate_algebra(a) for a in expr.args))


def base_angles(lhs,rhs):
    coefficients={}
    for atom in lhs.atoms(*TRIG)|rhs.atoms(*TRIG):
        for term in sp.Add.make_args(sp.expand(atom.args[0])):
            coeff,var=term.as_coeff_Mul()
            if var.is_Symbol and coeff.is_Rational and coeff != 0:
                coefficients.setdefault(var,[]).append(abs(coeff))
    return {v:v*min(cs) for v,cs in coefficients.items()}


def trig_replacement(atom,bases,style):
    a=atom.args[0];f=atom.func
    if f in (sp.tan,sp.cot,sp.sec,sp.csc):
        replacement={sp.tan:lambda:sp.sin(a)/sp.cos(a),sp.cot:lambda:sp.cos(a)/sp.sin(a),
                     sp.sec:lambda:1/sp.cos(a),sp.csc:lambda:1/sp.sin(a)}[f]()
        return replacement, 'Use the quotient or reciprocal identity', f'{atom} = {replacement}'
    expanded=sp.expand(a)
    if expanded.is_Add:
        terms=list(sp.Add.make_args(expanded))
        nonconstant=[t for t in terms if t.free_symbols]
        first=nonconstant[0] if nonconstant else terms[0]
        other=sp.expand(expanded-first)
        if f==sp.sin:
            replacement=sp.sin(first)*sp.cos(other)+sp.cos(first)*sp.sin(other)
            formula='sin(A+B) = sin(A)*cos(B) + cos(A)*sin(B)'
        else:
            replacement=sp.cos(first)*sp.cos(other)-sp.sin(first)*sp.sin(other)
            formula='cos(A+B) = cos(A)*cos(B) - sin(A)*sin(B)'
        return replacement,'Use the compound-angle identity',f'{formula}, with A = {first}, B = {other}. Use the exact standard-angle values.'
    coeff,var=expanded.as_coeff_Mul()
    if var in bases:
        u=bases[var];multiple=sp.cancel(expanded/u)
        if multiple.is_Integer and 1 < multiple <= 8:
            if multiple==2:
                if f==sp.sin:
                    replacement=2*sp.sin(u)*sp.cos(u)
                    reason=f'sin(2*u) = 2*sin(u)*cos(u), with u = {u}.'
                else:
                    replacement=[2*sp.cos(u)**2-1,1-2*sp.sin(u)**2,sp.cos(u)**2-sp.sin(u)**2][style]
                    reason=f'cos({a}) = {sp.sstr(replacement)}.'
                return replacement,'Use the double-angle identity',reason
            other=expanded-u
            replacement=(sp.sin(u)*sp.cos(other)+sp.cos(u)*sp.sin(other) if f==sp.sin
                         else sp.cos(u)*sp.cos(other)-sp.sin(u)*sp.sin(other))
            return replacement,'Use the compound-angle identity',f'Write {expanded} as ({u}) + ({other}) and apply the {f.__name__} addition formula.'
    return None


def pythagorean_reduce(expr, eliminate):
    # Reduce nonnegative even powers of ONE trig atom using its complementary
    # square. This is polynomial substitution, not a trig simplification oracle.
    numerator,denominator=sp.fraction(sp.together(expr))
    def reduce(poly):
        for atom in sorted(poly.atoms(eliminate),key=sp.default_sort_key):
            z=sp.Dummy('square_variable')
            tmp=poly.xreplace({atom:z})
            try:
                polynomial=sp.Poly(tmp,z)
            except sp.PolynomialError:
                continue
            complement=sp.sin(atom.args[0]) if eliminate==sp.cos else sp.cos(atom.args[0])
            poly=sp.expand(sum((coefficient*z**(degree[0]%2)*(1-complement**2)**(degree[0]//2)
                                for degree,coefficient in polynomial.terms()),sp.S.Zero)).xreplace({z:atom})
        return poly
    n,d=reduce(numerator),reduce(denominator)
    return sp.Mul(n,sp.Pow(d,-1,evaluate=False),evaluate=False) if d!=1 else n


def _normalize(source, lhs, rhs, bases, style, eliminate):
    path=[];current=source
    def push(after,title,reason,kind):
        nonlocal current
        if sp.sstr(after)==sp.sstr(current) or sp.count_ops(after)>240:
            return
        if (kind=='algebra' and sp.sstr(current)==sp.sstr(evaluate_algebra(current))
                and evaluate_algebra(after)==evaluate_algebra(current)):
            return
        if kind=='algebra':
            valid=algebra_equal(current,after)
        else:
            valid=build_certificate(evaluate_algebra(current),evaluate_algebra(after),[]) is not None
        if not valid:
            return
        path.append({'before':sp.sstr(current),'after':sp.sstr(after),'title':title,'reason':reason,'kind':kind})
        current=after
    def clean():
        push(evaluate_algebra(current),'Simplify the arithmetic','Combine constants and remove common numerical factors.','algebra')
        push(sp.together(current),'Combine the fractions','Write the terms over a common denominator.','algebra')
        n,d=sp.fraction(sp.together(current))
        expanded=sp.Mul(sp.expand(n),sp.Pow(sp.expand(d),-1,evaluate=False),evaluate=False) if d!=1 else sp.expand(n)
        push(expanded,'Expand and collect like terms','Expand the products and collect like terms in the numerator and denominator.','algebra')
        n,d=sp.fraction(sp.together(current))
        factored=sp.Mul(sp.factor(n),sp.Pow(sp.factor(d),-1,evaluate=False),evaluate=False) if d!=1 else sp.factor(n)
        push(factored,'Factor the numerator and denominator','Take out common factors before cancelling.','algebra')
        push(sp.cancel(current),'Cancel common factors','Cancel common factors; the original nonzero-denominator conditions remain in force.','algebra')
    # Familiar squared identities can shorten a fraction before quotient expansion.
    for _ in range(6):
        changed=False
        for node in list(sp.preorder_traversal(current)):
            if not node.is_Add:continue
            angles={a.args[0] for a in node.atoms(*TRIG)}
            for u in sorted(angles,key=sp.default_sort_key):
                for left,right in ((sp.sec(u)**2,sp.tan(u)**2),(sp.csc(u)**2,sp.cot(u)**2)):
                    k=node.coeff(left)
                    if k==0 or node.coeff(right)!=-k:continue
                    replacement=sp.expand(node-k*left+k*right)+k
                    residual=sp.cancel(lhs-rhs);local=sp.cancel(node-replacement)
                    ratio=sp.cancel(residual/local) if local!=0 else sp.S.Zero
                    if ratio!=0 and not ratio.free_symbols and not ratio.has(*TRIG):continue
                    before=len(path)
                    push(held_replace(current,node,replacement),'Use the Pythagorean identity',
                         f'{left} - {right} = 1.','identity')
                    if len(path)>before:changed=True;break
                if changed:break
            if changed:break
        if not changed:break
    # Rewrite one identity at a time, so every displayed line has one reason.
    for _ in range(30):
        chosen=None
        atoms=sorted(current.atoms(*TRIG),key=lambda a:(0 if a.func in (sp.tan,sp.cot,sp.sec,sp.csc) else 1 if a.func==sp.cos else 2,sp.default_sort_key(a)))
        for atom in atoms:
            proposal=trig_replacement(atom,bases,style)
            if proposal:
                chosen=(atom,*proposal);break
        if chosen is None: break
        atom,replacement,title,reason=chosen
        # A double-angle formula must not be cited as its own proof. Use the
        # independently established parent addition formula in that case.
        if title=='Use the double-angle identity':
            residual=sp.cancel(lhs-rhs)
            local=sp.cancel(atom-replacement)
            ratio=sp.cancel(residual/local) if local!=0 else sp.S.Zero
            if ratio!=0 and not ratio.free_symbols and not ratio.has(*TRIG):
                u=sp.cancel(atom.args[0]/2)
                title='Use the compound-angle identity'
                reason=f'Write {atom.args[0]} as ({u}) + ({u}). Apply {atom.func.__name__}(A+B) with A = B = {u}; then multiply the terms.'
        before=len(path)
        push(held_replace(current,atom,replacement),title,reason,'identity')
        if len(path)==before: break
        # Preserve the substitution line before ordinary arithmetic cleanup.
        push(evaluate_algebra(current),'Simplify the arithmetic','Combine constants and remove common numerical factors.','algebra')
    clean()
    for _ in range(2):
        reduced=pythagorean_reduce(current,eliminate)
        push(reduced,'Use the Pythagorean identity',
             ('cos(u)**2 = 1 - sin(u)**2' if eliminate==sp.cos else 'sin(u)**2 = 1 - cos(u)**2')+
             '. Substitute for the squared terms, expand and collect like terms.','identity')
        clean()
    return path


@lru_cache(maxsize=128)
def _trace_json(lhs,rhs):
    if sp.count_ops(lhs)+sp.count_ops(rhs)>140:
        return 'null'
    bases=base_angles(lhs,rhs)
    left_paths=[];right_paths=[]
    for style in range(3):
        for eliminate in (sp.cos,sp.sin):
            left_paths.append(_normalize(lhs,lhs,rhs,bases,style,eliminate))
            right_paths.append(_normalize(rhs,lhs,rhs,bases,style,eliminate))
    from engine import parse_expression
    def prefixes(paths,start):
        seen={sp.srepr(start):(start,[])}
        for path in paths:
            for i,step in enumerate(path,1):
                expr=parse_expression(step['after'])
                key=sp.srepr(expr)
                if key not in seen or i<len(seen[key][1]):
                    seen[key]=(expr,path[:i])
        return list(seen.values())
    ls,rs=prefixes(left_paths,lhs),prefixes(right_paths,rhs)
    best=None;score=None
    for a,lp in ls:
        for b,rp in rs:
            left_text=lp[-1]['after'] if lp else sp.sstr(lhs)
            right_text=rp[-1]['after'] if rp else sp.sstr(rhs)
            needs_bridge=left_text!=right_text
            n=len(lp)+len(rp)+needs_bridge
            if score is not None and n>score[0]: continue
            if not algebra_equal(a,b): continue
            steps=copy.deepcopy(lp)
            if needs_bridge:
                steps.append({'before':left_text,'after':right_text,'title':'Simplify the algebra',
                              'reason':'Combine like terms and cancel common factors on the original domain.','kind':'algebra'})
            for step in reversed(rp):
                reverse=dict(step,before=step['after'],after=step['before'])
                if step['kind']=='algebra':
                    reverse['title']='Rearrange the algebra'
                    reverse['reason']='Use equivalent fractions, expansion or factorisation to write the expression in the required form.'
                steps.append(reverse)
            # At the join, parsed algebra may have removed unevaluated brackets;
            # these are cosmetic and the equality is rechecked during replay.
            complexity=sum(len(s['after']) for s in steps)
            candidate=(len(steps),complexity)
            if score is None or candidate<score:
                score=candidate;best={'schema':'spm-algebra-trace-v1','steps':steps}
    if best is not None:
        refined=[]
        for step in best['steps']:
            if step['kind']=='algebra':
                a=parse_expression(step['before']);b=parse_expression(step['after'])
                raw=parse_display(step['before'])
                rn,rd=sp.fraction(raw,exact=True)
                simple_d=evaluate_algebra(rd)
                if rd!=1 and sp.count_ops(simple_d)<sp.count_ops(rd):
                    intermediate=sp.Mul(evaluate_algebra(rn),sp.Pow(simple_d,-1,evaluate=False),evaluate=False)
                    if sp.sstr(intermediate) not in (step['before'],step['after']):
                        refined.append({'before':step['before'],'after':sp.sstr(intermediate),
                            'title':'Simplify the denominator',
                            'reason':'Collect like terms in the denominator.','kind':'algebra'})
                        step=dict(step,before=sp.sstr(intermediate))
                        a=parse_expression(step['before'])
                n,d=sp.fraction(a)
                if a.is_Add:n,d=sp.fraction(sp.together(a))
                try:
                    common=sp.gcd(n,d)
                    if common.free_symbols and common!=1 and sp.count_ops(b)<sp.count_ops(a):
                        fn,fd=sp.factor(n),sp.factor(d)
                        if fd.could_extract_minus_sign():fn,fd=-fn,-fd
                        factored=sp.Mul(fn,sp.Pow(fd,-1,evaluate=False),evaluate=False)
                        if sp.sstr(factored) not in (step['before'],step['after']):
                            refined.append({'before':step['before'],'after':sp.sstr(factored),
                                'title':'Factor the numerator and denominator',
                                'reason':'Expose the common factor before cancelling it.','kind':'algebra'})
                            step=dict(step,before=sp.sstr(factored),title='Cancel the common factor',
                                reason='Cancel the common factor. The original denominator must still be nonzero.')
                except sp.PolynomialError:pass
            refined.append(step)
        best['steps']=refined
        best.update(lhs=sp.sstr(lhs),rhs=sp.sstr(rhs),lhs_latex=sp.latex(lhs),rhs_latex=sp.latex(rhs))
        for step in best['steps']:
            step['before_latex']=sp.latex(parse_display(step['before']))
            step['after_latex']=sp.latex(parse_display(step['after']))
    return json.dumps(best,sort_keys=True)


def build_trace(lhs,rhs):
    return json.loads(_trace_json(lhs,rhs))


def parse_display(text):
    # Preserve trig arguments and displayed arithmetic brackets for the lesson.
    from engine import _SafeSympyParser
    class DisplayParser(_SafeSympyParser):
        def _visit(self,node):
            if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id in ('sin','cos','tan','cot','sec','csc') and len(node.args)==1:
                argument=self._visit(node.args[0])
                return getattr(sp,node.func.id)(argument,evaluate=False)
            if isinstance(node,ast.BinOp):
                left,right=self._visit(node.left),self._visit(node.right)
                if isinstance(node.op,ast.Add):return sp.Add(left,right,evaluate=False)
                if isinstance(node.op,ast.Sub):return sp.Add(left,sp.Mul(-1,right,evaluate=False),evaluate=False)
                if isinstance(node.op,ast.Mult):return sp.Mul(left,right,evaluate=False)
                if isinstance(node.op,ast.Div):
                    reciprocal=sp.Pow(right,-1,evaluate=False)
                    return reciprocal if left==1 else sp.Mul(left,reciprocal,evaluate=False)
                if isinstance(node.op,ast.Pow):return sp.Pow(left,right,evaluate=False)
            return super()._visit(node)
    return DisplayParser().parse(text)


def parse_school(text):
    from engine import _SafeSympyParser
    class SchoolParser(_SafeSympyParser):
        def _visit(self,node):
            if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id in ('sin','cos','tan','cot','sec','csc') and len(node.args)==1:
                argument=self._visit(node.args[0])
                if argument.free_symbols:return getattr(sp,node.func.id)(argument,evaluate=False)
            return super()._visit(node)
    return SchoolParser().parse(text)


def verify_trace(trace,lhs,rhs):
    from engine import parse_expression
    try:
        if parse_expression(trace['lhs'])!=lhs or parse_expression(trace['rhs'])!=rhs:return False
        a,b=parse_school(trace['lhs']),parse_school(trace['rhs'])
        return trace==build_trace(a,b)
    except (KeyError,ValueError,TypeError):return False


def report_lines(trace,lhs,rhs):
    lines=['ALGEBRAIC PROOF','',f'Start with the LHS: {lhs}','']
    for i,step in enumerate(trace['steps'],1):
        lines += [f"{i}. {step['title']}",f"   = {step['after']}",f"   Reason: {step['reason']}",'']
    lines += [f'This is the RHS: {rhs}.','Hence LHS = RHS on the stated domain.']
    return lines


def desktop_report(result):
    trace=result.certificate_override.get('student_proof')
    lhs=trace['lhs'] if trace else str(result.lhs)
    rhs=trace['rhs'] if trace else str(result.rhs)
    lines=['TRIGONOMETRIC IDENTITY REPORT','='*84,f'Claim: {lhs} = {rhs}',
           'Status: '+result.status,'Selected route: '+result.selected_route,'',
           'ORIGINAL COMMON-DOMAIN CONDITIONS','-'*84]
    lines += result.domain_conditions or ['No additional restrictions.']
    if trace:lines += ['',*report_lines(trace,lhs,rhs)]
    lines += ['','CONCLUSION',result.message,'',
              'Every displayed equality is checked. Cancelling a factor does not remove the original domain restrictions.']
    return '\n'.join(lines)


def markdown_report(result):
    trace=result.certificate_override.get('student_proof')
    lhs=trace['lhs_latex'] if trace else sp.latex(result.lhs)
    rhs=trace['rhs_latex'] if trace else sp.latex(result.rhs)
    lines=['# Trigonometric Proof Report — v0.7.1','','**Status: PROVED**','',
           '$$'+lhs+' = '+rhs+'$$','','## Domain','']
    lines += ['- `'+c+'`' for c in result.domain_conditions] or ['No additional restrictions.']
    if trace:
        lines += ['','## Algebraic proof','','Start with the LHS:','', '$$'+lhs+'$$','']
        for i,step in enumerate(trace['steps'],1):
            lines += [f"{i}. **{step['title']}**",'', '$$= '+step['after_latex']+'$$','',step['reason'],'']
        lines += ['This is the RHS, so the identity is proved on its original common domain.']
    else:lines += ['',result.message]
    return '\n'.join(lines)+'\n'
