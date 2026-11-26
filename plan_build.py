import re
CSS=re.search(r'CSS = """(.*?)"""',open('build.py').read(),re.S).group(1)
CSS+="""
.f{display:block;width:100%;border:1.5px dashed rgba(11,42,74,.35);border-radius:10px;padding:8px 10px;font:inherit;font-size:14px;background:#fffdf7;outline:none;min-height:40px;white-space:pre-wrap}
.f:focus{border-style:solid;border-color:var(--purple)}.f:empty::before{content:attr(data-ph);color:#9aa7b3}
.sel{width:100%;font:inherit;font-size:15px;padding:10px 12px;border:1.5px solid var(--navy);border-radius:10px;background:#fff;color:var(--navy)}
.mon{width:100%;font:inherit;font-size:15px;padding:9px 12px;border:1.5px solid var(--navy);border-radius:10px;background:#fff;color:var(--navy)}
.who{display:flex;gap:16px;align-items:center;margin-top:18px;background:var(--cream);color:var(--navy);padding:14px 16px;border-radius:14px}
.ph{width:96px;height:96px;border-radius:50%;background:#fff;border:2px dashed var(--yellow);display:flex;align-items:center;justify-content:center;overflow:hidden;flex:0 0 96px;cursor:pointer;position:relative}
.ph img{width:100%;height:100%;object-fit:cover}.ph span{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:.1em;text-transform:uppercase;text-align:center;color:#4b5f72;padding:6px}
.ph input{position:absolute;inset:0;opacity:0;cursor:pointer}
.who .nm{flex:1}.who .nm .l{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:.18em;text-transform:uppercase;opacity:.75}
.who .nm input{width:100%;border:0;border-bottom:2px solid var(--navy);background:transparent;font:inherit;font-family:'Fraunces',serif;font-weight:900;font-size:20px;color:var(--navy);padding:4px 0;outline:none}
.rmph{font:inherit;font-size:11px;background:none;border:1px solid var(--navy);border-radius:20px;padding:3px 10px;color:var(--navy);cursor:pointer;margin-top:6px}
.act{--acc:var(--yellow)}.act2{--acc:var(--green)}
.comp .rate{border-bottom:1px solid rgba(11,42,74,.08);padding:8px 0 10px}.comp .rate .q{flex:0 0 100%}.comp .f{min-height:34px;margin-top:6px;font-size:13.5px}
@media (min-width:700px){.comp .rate .q{flex:0 0 100%}}
@media print{h2,.sub{break-after:avoid}.rate{break-inside:avoid}.f{min-height:26px;border-style:solid;background:#fff}.f:empty::before{content:""}.ph{border-style:solid}.rmph,.ph input{display:none}.sel,.mon{border:1px solid #999}.comp .f{min-height:22px}}
"""
COMP=[("Multilingual","Communicating in English and other languages, understanding each other across cultures"),("Personal, social and learning to learn","Reflecting on yourself, working with others, managing your own learning"),("Citizenship","Acting as a responsible citizen, participation, democracy, human rights"),("Entrepreneurship","Turning ideas into action, creativity, initiative, planning"),("Cultural awareness and expression","Expressing ideas through theatre, art, storytelling; understanding other cultures"),("Digital","Using digital tools critically, safely and creatively"),("Mathematical, science, technology and engineering","Logical thinking, working with data, understanding how technology works"),("Literacy","Reading, writing, speaking and listening; expressing yourself clearly")]
def scale(key,n=8): return '<div class="scale" data-key="'+key+'">'+''.join(f'<b>{i}</b>' for i in range(1,n+1))+'</div>'
def f(key,ph,lab=None): return (f'<div class="lab">{lab}</div>' if lab else '')+f'<div class="f" contenteditable="true" data-key="{key}" data-ph="{ph}"></div>'
acts=''.join(f'<div class="card {"act" if i==1 else "act2"}"><span class="n">Activity {i}</span><h3>Biggest impact</h3>'+f(f'a{i}_name','The name of the activity...','Name of the activity')+f(f'a{i}_desc','What happened, in two or three sentences...','Description')+f(f'a{i}_why','What changed for me, what I will take home...','Why it was impactful for me')+'</div>' for i in (1,2))
ener=''.join(f'<div class="lab">Energiser {i}</div><div class="f" contenteditable="true" data-key="e{i}" data-ph="Name of the energiser, and in one line why it worked..."></div>' for i in (1,2))
comps=''.join(f'<div class="rate"><div class="q">{c}<small>{s}</small></div>{scale("c"+str(i))}<div class="f" contenteditable="true" data-key="c{i}_how" data-ph="How I developed it during the project..."></div></div>' for i,(c,s) in enumerate(COMP))
OPTS=["Social media posts (photos and videos)","Presentation in front of a group of young people","Replication of an activity from the project with a group of young people","Webinar","Blog article"]
sel='<select class="sel" data-key="dis_type"><option value="">Choose how you will disseminate the project...</option>'+''.join(f'<option>{o}</option>' for o in OPTS)+'</select>'
html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Creative Futures · Personal Action Plan</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=Fraunces:ital,opsz,wght@0,9..144,900;1,9..144,500;1,9..144,900&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="head"><div class="curtain">{"<i></i>"*40}</div><div class="wrap">
<div class="kicker">Creative Futures · Erasmus+ KA153-YOU · Mobility of Youth Workers</div>
<h1>Personal <em>Action Plan</em></h1>
<p class="lead">What I take home from Amsterdam: the activities that mattered most, my key competences, and one concrete thing I will do with young people and my organisation in the next months. It saves itself on this device; download the PDF when it is complete.</p>
<div class="who"><label class="ph" id="ph"><span>Add your photo</span><input type="file" accept="image/*" id="phin"></label><div class="nm"><div class="l">Name and surname</div><input data-key="name" placeholder="Your name"><div class="l" style="margin-top:8px">Organisation and country</div><input data-key="org" placeholder="Organisation, country" style="font-size:16px;font-weight:600;font-family:'Bricolage Grotesque'"><button class="rmph" id="rmph" type="button" style="display:none">Remove photo</button></div></div>
</div></div>
<div class="wrap">
<h2>Activities with the <em>biggest impact</em></h2><p class="sub">Two activities from the week that changed something for you: a method, an idea, a feeling.</p>
<div class="grid2">{acts}</div>
<h2>Two best <em>energisers</em></h2><p class="sub">The ones you will steal for your own groups.</p>
<div class="card" style="--acc:#ff6a4d">{ener}</div>
<h2>My <em>key competences</em></h2><p class="sub">The 8 key competences of Youthpass. Mark from 1 (a little) to 8 (a lot) how much you developed each one during the project, and write how.</p>
<div class="card comp" style="--acc:#7a5cff">{comps}</div>
<h2>Local follow-up action and <em>dissemination</em></h2><p class="sub">How you will bring Creative Futures to young people and colleagues at home.</p>
<div class="card" style="--acc:#b6da4c">
{f('follow','One activity with young people or colleagues, using a method from the project...','My local follow-up action')}
<div class="lab">How I will disseminate the project</div>{sel}
{f('dis_where','The city, the youth centre, the school, or the platform: Instagram, TikTok, Facebook, YouTube, a website...','Where, or on which platform')}
{f('dis_structure','What happens, step by step: who takes part, what you show, what they do, how long it takes...','The structure of the dissemination activity')}
<div class="lab">When it will take place (month and year)</div><input type="month" class="mon" data-key="dis_when" min="2026-11" max="2027-12">
{f('dis_proof','A link, photos, a short report, the number of people reached...','How I will share the evidence with the project team')}
</div>
<p class="hint sub">Your plan stays on this device only. Download the PDF and upload it to the Action Plans folder of the project, or send it to your sending organisation.</p>
</div>
<div class="bar"><button class="btn" onclick="dl()">Download as PDF</button><button class="btn ghost" onclick="clr()">Clear plan</button><span class="saved" id="sv">saved</span></div>
<div class="foot">Creative Futures: Theatre, Tech &amp; European Participation · Amsterdam 2026</div>
<script>
const K='cf_action_plan';let D={{}};try{{D=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
function save(){{try{{localStorage.setItem(K,JSON.stringify(D));document.getElementById('sv').textContent='saved '+new Date().toLocaleTimeString([],{{hour:'2-digit',minute:'2-digit'}})}}catch(e){{document.getElementById('sv').textContent='could not save (storage full)'}}}}
document.querySelectorAll('.scale').forEach(sc=>{{const k=sc.dataset.key;const paint=v=>sc.querySelectorAll('b').forEach((b,i)=>{{b.classList.toggle('on',i+1==v);b.classList.toggle('lt',i+1<v)}});if(D[k])paint(D[k]);sc.querySelectorAll('b').forEach((b,i)=>b.onclick=()=>{{D[k]=(D[k]==i+1)?0:i+1;paint(D[k]);save()}})}});
document.querySelectorAll('[contenteditable]').forEach(el=>{{const k=el.dataset.key;if(D[k])el.textContent=D[k];el.oninput=()=>{{D[k]=el.textContent;save()}}}});
document.querySelectorAll('input[data-key],select[data-key]').forEach(el=>{{const k=el.dataset.key;if(D[k])el.value=D[k];el.oninput=el.onchange=()=>{{D[k]=el.value;save()}}}});
const ph=document.getElementById('ph'),phin=document.getElementById('phin'),rm=document.getElementById('rmph');
function showPhoto(){{if(D.photo){{ph.innerHTML='<img src="'+D.photo+'" alt="Photo">';ph.appendChild(phin);rm.style.display='inline-block'}}}}
showPhoto();
phin.onchange=()=>{{const file=phin.files[0];if(!file)return;const img=new Image();const rd=new FileReader();rd.onload=()=>{{img.onload=()=>{{const c=document.createElement('canvas');const s=Math.min(1,520/Math.max(img.width,img.height));c.width=Math.round(img.width*s);c.height=Math.round(img.height*s);c.getContext('2d').drawImage(img,0,0,c.width,c.height);D.photo=c.toDataURL('image/jpeg',.82);save();showPhoto()}};img.src=rd.result}};rd.readAsDataURL(file)}};
rm.onclick=()=>{{delete D.photo;save();ph.innerHTML='<span>Add your photo</span>';ph.appendChild(phin);rm.style.display='none'}};
function dl(){{document.title='Creative Futures - Action Plan - '+(D.name||'plan');window.print()}}
function clr(){{if(confirm('Delete your whole action plan on this device?')){{D={{}};localStorage.removeItem(K);location.reload()}}}}
</script></body></html>'''
open('plan.html','w').write(html); print('plan.html ok')
