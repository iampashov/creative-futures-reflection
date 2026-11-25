import re
CSS=re.search(r'CSS = """(.*?)"""',open('build.py').read(),re.S).group(1)
CSS+="""
.f{display:block;width:100%;border:1.5px dashed rgba(11,42,74,.35);border-radius:10px;padding:8px 10px;font:inherit;font-size:14px;background:#fffdf7;outline:none;min-height:40px;white-space:pre-wrap}
.f:focus{border-style:solid;border-color:var(--purple)}.f:empty::before{content:attr(data-ph);color:#9aa7b3}
.grid2{display:grid;gap:10px}@media(min-width:700px){.grid2{grid-template-columns:1fr 1fr}}
.chk{display:flex;gap:10px;align-items:flex-start;margin:6px 0;font-size:14px}.chk input{width:22px;height:22px;margin:0;accent-color:var(--navy);flex:0 0 22px}
.tool{--acc:var(--yellow)}.tool.ai{--acc:var(--purple)}
.steps{counter-reset:s}.steps .f{margin-bottom:6px}
@media print{.f{min-height:26px;border-style:solid;background:#fff}.f:empty::before{content:""}.grid2{grid-template-columns:1fr 1fr}.chk input{width:14px;height:14px}}
"""
FIELDS=[("name","Tool name","..."),("link","Web link (where to access it)","https://..."),("does","What it does in one sentence","..."),("price","Pricing model and price per month","Free · Freemium · Open source · Paid, and the price for one person"),("npo","Non-profit or education discount","Yes with the percentage or free plan · No · Not found"),("age","Age limit, data and privacy","Minimum age in the terms, where data are stored, whether young people need an account, whether inputs train the AI"),("works","Works on, offline / low data, accessibility","Phone, laptop, both · offline mode or online only · screen reader, captions, plain language"),("use","Creative Futures use: one concrete scenario","Who it helps: a theatre group, a video crew, a youth council, a reflection circle..."),("test","Our test: what we made, what worked, what went wrong","..."),("ai","AI check: three honest lines","1. What it did well  2. What it got wrong or made up  3. What a youth worker must check before using it with young people")]
def tool(n,kind):
    k=f't{n}'; cls='tool ai' if kind=='AI' else 'tool'
    inner=''.join(f'<div class="lab">{l}</div><div class="f" contenteditable="true" data-key="{k}_{fk}" data-ph="{ph}"></div>' for fk,l,ph in FIELDS[:7])
    steps='<div class="lab">Basic guideline: how a beginner sets it up and uses it, in three steps</div><div class="steps">'+''.join(f'<div class="f" contenteditable="true" data-key="{k}_step{i}" data-ph="Step {i}..."></div>' for i in (1,2,3))+'</div>'
    rest=''.join(f'<div class="lab">{l}</div><div class="f" contenteditable="true" data-key="{k}_{fk}" data-ph="{ph}"></div>' for fk,l,ph in FIELDS[7:])
    return f'<div class="card {cls}"><span class="n">Tool {n}</span><h3>{"AI tool" if kind=="AI" else "Digital tool"}</h3>{inner}{steps}{rest}</div>'
needs=''.join(f'<div class="lab">Need {i}</div><div class="f" contenteditable="true" data-key="need{i}" data-ph="What do the young people or the youth worker need? One real example from your work..."></div>' for i in (1,2,3))
checks=["Every link opens and goes to the tool, not to an ad.","Prices checked on the tool's own pricing page today.","One screenshot per tool from your own test, uploaded to the team folder.","No personal data of young people in screenshots or examples.","The no-budget and the worth-paying-for recommendations are filled in.","Team number, countries and date are at the top."]
chk=''.join(f'<label class="chk"><input type="checkbox" data-key="chk{i}"><span>{c}</span></label>' for i,c in enumerate(checks))
html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Creative Futures · Tools team sheet</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=Fraunces:ital,opsz,wght@0,9..144,900;1,9..144,500;1,9..144,900&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="head"><div class="curtain">{"<i></i>"*40}</div><div class="wrap">
<div class="kicker">Tools for Creative Futures · team sheet · Erasmus+ KA153-YOU</div>
<h1>Tools <em>team sheet</em></h1>
<p class="lead">Fill this sheet together on one phone or laptop while you test. It saves itself in this browser. When it is complete, press Download as PDF and upload the file to your team folder.</p>
<div class="tickets"><div class="tk"><div class="l">Team</div><input data-key="team" placeholder="Team 1 to 5 and your area"></div><div class="tk"><div class="l">Countries</div><input data-key="countries" placeholder="e.g. GR, TR, ES"></div><div class="tk"><div class="l">Date</div><input data-key="date" placeholder="25 November 2026"></div></div>
</div></div>
<div class="wrap">
<h2>The <em>needs</em></h2><p class="sub">Write these before the tools: what do the people in your area actually need, and what does a youth worker need to help them?</p>
<div class="card" style="--acc:#b6da4c">{needs}</div>
<h2>The <em>tools</em></h2><p class="sub">At least one digital tool and one AI tool. Every field filled; "not found" is an answer, an empty box is not.</p>
<div class="grid2">{tool(1,"digital")}{tool(2,"AI")}</div>
<h2>Our <em>recommendations</em></h2>
<div class="card" style="--acc:#ff6a4d">
<div class="lab">The one tool for a youth centre with no budget, and why</div><div class="f" contenteditable="true" data-key="rec_free" data-ph="Tool and one sentence..."></div>
<div class="lab">The one tool worth paying for, and why</div><div class="f" contenteditable="true" data-key="rec_paid" data-ph="Tool and one sentence..."></div>
<div class="lab">One idea we will try in our own organisation</div><div class="f" contenteditable="true" data-key="rec_try" data-ph="..."></div>
</div>
<h2>Before you <em>upload</em></h2>
<div class="card" style="--acc:#ffc83d">{chk}</div>
<p class="hint sub">This sheet stays on this device only. Download the PDF before you close the browser, and upload it to Daily Media › Day 4 › Tools for Creative Futures › your team.</p>
</div>
<div class="bar"><button class="btn" onclick="dl()">Download as PDF</button><button class="btn ghost" onclick="clr()">Clear sheet</button><span class="saved" id="sv">saved</span></div>
<div class="foot">Creative Futures: Theatre, Tech &amp; European Participation · Amsterdam 2026 · Tool names are brands of their owners</div>
<script>
const K='cf_tools_sheet';let D={{}};try{{D=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
function save(){{try{{localStorage.setItem(K,JSON.stringify(D));document.getElementById('sv').textContent='saved '+new Date().toLocaleTimeString([],{{hour:'2-digit',minute:'2-digit'}})}}catch(e){{}}}}
document.querySelectorAll('[contenteditable]').forEach(el=>{{const k=el.dataset.key;if(D[k])el.textContent=D[k];el.oninput=()=>{{D[k]=el.textContent;save()}}}});
document.querySelectorAll('input[type=text],input:not([type])').forEach(el=>{{const k=el.dataset.key;if(D[k])el.value=D[k];el.oninput=()=>{{D[k]=el.value;save()}}}});
document.querySelectorAll('input[type=checkbox]').forEach(el=>{{const k=el.dataset.key;el.checked=!!D[k];el.onchange=()=>{{D[k]=el.checked;save()}}}});
function dl(){{document.title='Creative Futures - Tools - '+(D.team||'team sheet');window.print()}}
function clr(){{if(confirm('Delete everything on this sheet on this device?')){{D={{}};localStorage.removeItem(K);location.reload()}}}}
</script></body></html>'''
open('tools.html','w').write(html); print('tools.html ok')
