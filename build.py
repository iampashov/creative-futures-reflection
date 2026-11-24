import json, html
DAYS = {
 "day1": dict(n=1, date="Monday 23 November 2026", scene="Scene 2 · Foundations", title="Foundations", acts=[
  ("E","The Wind Blows","Energiser","Chairs in a circle, one person in the middle: \"the wind blows for everyone who...\""),
  (1,"Name, Adjective, Movement","Name game","Your name, an adjective with the same first letter, and a movement; the group repeats."),
  (2,"Human Bingo","Getting to know each other","Find someone who fits each square and collect 25 names."),
  (3,"Speed Dating","Getting to know each other","Two circles, two minutes per question, then rotate."),
  (4,"Project Rules","Group agreement","The group writes its own rules for the week."),
  (5,"Fears, Expectations, Contributions","Expectations","Three colours of sticky notes on three flipcharts."),
  (6,"Mission Impossible","Team-building challenge","17 missions around the hostel and Amsterdam Noord, in mixed teams."),
 ]),
 "day2": dict(n=2, date="Tuesday 24 November 2026", scene="Scene 3 · Theatre &amp; Storytelling", title="Theatre &amp; Storytelling", acts=[
  ("E","Follow the Leader","Energiser","The circle copies one hidden leader; the detective in the middle has to find them."),
  ("E","What Are You Doing?","Energiser","Mime one action, answer with a different one, the next person mimes what you said."),
  (1,"Erasmus+ Opportunities and Youthpass","Workshop","Erasmus+ Youth actions, how projects are built, and the 8 key competences of Youthpass."),
  (2,"Silent Lines","Theatre exercise","Line up by birthday, shoe size, distance travelled, without a word."),
  (3,"Colombian Hypnosis","Theatre exercise (Boal)","Follow your partner's hand with your face; lead, follow, then one leader and two followers."),
  (4,"Forum Theatre","Theatre of the Oppressed","A play with a bad ending, replayed while another team shouts Stop! and changes it."),
 ]),
}
COMP = [
 ("Multilingual","Communicating in English and other languages, understanding each other across cultures"),
 ("Personal, social and learning to learn","Reflecting on yourself, working with others, managing your own learning"),
 ("Citizenship","Acting as a responsible citizen, participation, democracy, human rights"),
 ("Entrepreneurship","Turning ideas into action, creativity, initiative, planning"),
 ("Cultural awareness and expression","Expressing ideas through theatre, art, storytelling; understanding other cultures"),
 ("Digital","Using digital tools critically, safely and creatively"),
 ("Mathematical, science, technology and engineering","Logical thinking, working with data, understanding how technology works"),
 ("Literacy","Reading, writing, speaking and listening; expressing yourself clearly"),
]
RATES = [("work","Is it useful in your work?"),("fun","Is it entertaining?"),("learn","Learning outcomes")]
CSS = """
:root{--navy:#0b2a4a;--cream:#fbf5ea;--yellow:#ffc83d;--pink:#ff6a4d;--green:#b6da4c;--purple:#7a5cff;--sand:#f0e7d3}
*{box-sizing:border-box;min-width:0}html{-webkit-text-size-adjust:100%}html,body{overflow-x:hidden;max-width:100%}
body{margin:0;background:var(--cream);color:var(--navy);font-family:'Bricolage Grotesque','Helvetica Neue',Arial,sans-serif;font-size:15px;line-height:1.45}
.head{background:var(--navy);color:var(--cream);padding:0 0 28px;position:relative}
.curtain{display:flex;height:16px;padding:0 2px}.curtain i{flex:1;height:16px;background:var(--pink);border-radius:0 0 50% 50%;margin-right:2px}
.wrap{max-width:860px;margin:0 auto;padding:0 16px}
.kicker{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.22em;color:var(--green);margin:22px 0 8px;text-transform:uppercase}
h1{font-family:'Fraunces',serif;font-weight:900;font-size:clamp(34px,7vw,56px);line-height:1;margin:0 0 10px;letter-spacing:-.01em}
h1 em{font-style:italic;font-weight:500;color:var(--yellow)}
.lead{max-width:620px;color:#dfe7ee;font-size:14px}
.tickets{display:flex;flex-wrap:wrap;margin:18px -16px 0;background:var(--cream);color:var(--navy)}
.tk{flex:1 1 150px;padding:12px 16px;border-right:2px dashed var(--navy)}.tk:last-child{border-right:0;background:var(--yellow)}
.tk .l{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:.18em;opacity:.75;text-transform:uppercase}
.tk .v{font-family:'Fraunces',serif;font-weight:900;font-size:17px;line-height:1.1;margin-top:3px}
.tk input{width:100%;border:0;border-bottom:2px solid var(--navy);background:transparent;font:inherit;font-family:'Fraunces',serif;font-weight:900;font-size:19px;color:var(--navy);padding:2px 0;outline:none}
.pill{display:inline-block;font-weight:800;font-size:11px;padding:3px 10px;border-radius:20px;color:var(--navy);margin-right:6px}
h2{font-family:'Fraunces',serif;font-weight:900;font-size:26px;margin:34px 0 6px;line-height:1.1}
h2 em{font-style:italic;font-weight:500;color:var(--purple)}
.sub{color:#4b5f72;margin:0 0 14px;font-size:14px}
.card{background:#fff;border:1.5px solid rgba(11,42,74,.14);border-radius:14px;padding:18px 18px 14px;margin:0 0 14px;break-inside:avoid;position:relative;overflow:hidden}
.card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:7px;background:var(--acc,var(--yellow))}
.card .n{font-family:'Fraunces',serif;font-weight:900;font-size:13px;color:var(--navy);background:var(--acc,var(--yellow));border-radius:20px;padding:2px 10px;display:inline-block;margin-right:8px}
.card h3{font-family:'Fraunces',serif;font-weight:900;font-size:20px;margin:0 0 2px;display:inline}
.card .tag{font-family:'Space Mono',monospace;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#4b5f72;margin:4px 0 2px}
.card .desc{font-size:13.5px;color:#4b5f72;margin:0 0 10px}
.rate{display:flex;align-items:center;gap:6px 10px;flex-wrap:wrap;margin:8px 0}
.rate .q{flex:0 0 100%;font-weight:600;font-size:14px}
.scale{display:flex;gap:4px;flex:0 0 100%;width:100%}
.scale b{flex:1 1 0;min-width:0;max-width:40px;height:30px;border-radius:50%;border:1.5px solid var(--navy);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;cursor:pointer;user-select:none;background:#fff}
.scale b.on{background:var(--navy);color:var(--cream)}.scale b.lt{background:var(--sand)}
.lab{font-family:'Space Mono',monospace;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#4b5f72;margin:10px 0 4px}
.note{min-height:56px;border:1.5px dashed rgba(11,42,74,.35);border-radius:10px;padding:8px 10px;font:inherit;font-size:14px;background:#fffdf7;outline:none;white-space:pre-wrap}
.note:focus{border-style:solid;border-color:var(--purple)}.note:empty::before{content:attr(data-ph);color:#9aa7b3}
.comp .rate .q{flex:0 0 100%;}.comp .rate{border-bottom:1px solid rgba(11,42,74,.08);padding:8px 0}
.comp .rate .q small{display:block;font-weight:400;color:#4b5f72;font-size:12.5px}
.bar{position:sticky;bottom:0;background:var(--navy);color:var(--cream);padding:12px 16px;display:flex;gap:10px;justify-content:center;align-items:center;flex-wrap:wrap;margin-top:30px}
.btn{font:inherit;font-weight:800;font-size:15px;padding:12px 20px;border-radius:30px;border:0;cursor:pointer;background:var(--yellow);color:var(--navy)}
.btn.ghost{background:transparent;color:var(--cream);border:1.5px solid var(--cream)}
.saved{font-family:'Space Mono',monospace;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--green)}
.foot{text-align:center;font-family:'Space Mono',monospace;font-size:10px;letter-spacing:.14em;color:#4b5f72;padding:18px 16px 30px}
.eu{display:flex;justify-content:center;align-items:center;gap:8px;margin-top:8px}.eu .flag{width:30px;height:20px;background:#039;position:relative;border-radius:2px}.eu .flag i{position:absolute;width:3px;height:3px;background:#fc0;border-radius:50%;left:13.5px;top:8.5px;transform-origin:center}
@media (min-width:700px){.rate .q{flex:0 0 200px}.scale{flex:1 1 0}.comp .rate .q{flex:0 0 300px}}
@media print{@page{size:A4;margin:12mm}body{background:#fff;font-size:12px}.head{padding-bottom:14px}.bar,.hint{display:none!important}.card{box-shadow:none;margin-bottom:8px;padding:10px 12px 8px;break-inside:auto}.rate,.note,.lab,.card h3{break-inside:avoid}.comp{break-inside:avoid}.note{min-height:30px;border-style:solid;background:#fff}.scale b{max-width:22px;font-size:9px}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}.tickets{margin:12px 0 0}h2{font-size:20px;margin:18px 0 4px}.card h3{font-size:16px}.tk input{border-bottom:0}}
"""
FLAG = '<div class="flag">'+''.join(f'<i style="transform:rotate({i*30}deg) translateY(-7px)"></i>' for i in range(12))+'</div>'
def scale(key):
    return '<div class="scale" data-key="'+key+'">'+''.join(f'<b>{i}</b>' for i in range(1,11))+'</div>'
def page(k,d):
    accs=["#ffc83d","#b6da4c","#7a5cff","#ff6a4d","#9ad5ff","#ffb3c7","#ffc83d","#b6da4c"]
    cards=''
    for i,(n,t,tag,desc) in enumerate(d["acts"]):
        key=f'a{i}'; acc=accs[i%len(accs)]
        rates=''.join(f'<div class="rate"><div class="q">{q}</div>{scale(key+"_"+rk)}</div>' for rk,q in RATES)
        cards+=f'''<div class="card" style="--acc:{acc}"><span class="n">{"Energiser" if n=="E" else n}</span><h3>{t}</h3><div class="tag">{tag}</div><p class="desc">{desc}</p>
{rates}
<div class="lab">Was it useful? What did you notice?</div><div class="note" contenteditable="true" data-key="{key}_notes" data-ph="Your notes..."></div>
<div class="lab">How would you use it with your young people?</div><div class="note" contenteditable="true" data-key="{key}_use" data-ph="With which group, on which topic, what would you change..."></div>
</div>
'''
    comps=''.join(f'<div class="rate"><div class="q">{c}<small>{s}</small></div>{scale("c"+str(i))}</div>' for i,(c,s) in enumerate(COMP))
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Creative Futures · Day {d["n"]} reflection</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=Fraunces:ital,opsz,wght@0,9..144,900;1,9..144,500;1,9..144,900&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="head"><div class="curtain">{"<i></i>"*40}</div><div class="wrap">
<div class="kicker">My learning diary · Erasmus+ KA153-YOU · Mobility of Youth Workers</div>
<h1>Day {d["n"]} <em>{d["title"]}</em></h1>
<p class="lead">Your personal reflection for today. Rate each activity, note what you noticed and how you would use it with your young people, then mark which key competences you used. It saves itself in this browser as you write. At the end, download it as a PDF.</p>
<div class="tickets"><div class="tk"><div class="l">Your name</div><input data-key="name" placeholder="First and last name"></div><div class="tk"><div class="l">Date</div><div class="v">{d["date"]}</div></div><div class="tk"><div class="l">Scene</div><div class="v">{d["scene"]}</div></div></div>
</div></div>
<div class="wrap">
<h2>The <em>activities</em></h2><p class="sub">For each activity: three marks from 1 (not at all) to 10 (very much), and two short notes. Skip what you did not take part in.</p>
{cards}
<h2>My <em>key competences</em> today</h2><p class="sub">The 8 key competences of Youthpass. How much did you use and develop each one today, from 1 (not at all) to 10 (a lot)? These marks build your personal plan at the end of the week.</p>
<div class="card comp" style="--acc:#7a5cff">{comps}</div>
<h2>The day in <em>three lines</em></h2>
<div class="card" style="--acc:#b6da4c">
<div class="lab">The moment I will remember</div><div class="note" contenteditable="true" data-key="d_best" data-ph="..."></div>
<div class="lab">One thing I learned about myself or my work</div><div class="note" contenteditable="true" data-key="d_learn" data-ph="..."></div>
<div class="lab">One question I still have</div><div class="note" contenteditable="true" data-key="d_q" data-ph="..."></div>
</div>
<p class="hint sub">Your answers stay on this device only (browser storage). Nobody else can see them. To keep them, download the PDF before you clear your browser or switch phone.</p>
</div>
<div class="bar"><button class="btn" onclick="dl()">Download as PDF</button><button class="btn ghost" onclick="clr()">Clear this day</button><span class="saved" id="sv">saved</span></div>
<div class="foot">Creative Futures: Theatre, Tech &amp; European Participation · Amsterdam 2026<div class="eu">{FLAG}<span>Co-funded by the European Union</span></div></div>
<script>
const K='cf_reflection_{k}';let D={{}};try{{D=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
function save(){{try{{localStorage.setItem(K,JSON.stringify(D));const s=document.getElementById('sv');s.textContent='saved '+new Date().toLocaleTimeString([],{{hour:'2-digit',minute:'2-digit'}})}}catch(e){{}}}}
document.querySelectorAll('.scale').forEach(sc=>{{const k=sc.dataset.key;const paint=v=>sc.querySelectorAll('b').forEach((b,i)=>{{b.classList.toggle('on',i+1==v);b.classList.toggle('lt',i+1<v)}});if(D[k])paint(D[k]);sc.querySelectorAll('b').forEach((b,i)=>b.onclick=()=>{{D[k]=(D[k]==i+1)?0:i+1;paint(D[k]);save()}})}});
document.querySelectorAll('[contenteditable]').forEach(el=>{{const k=el.dataset.key;if(D[k])el.textContent=D[k];el.oninput=()=>{{D[k]=el.textContent;save()}}}});
const nm=document.querySelector('input[data-key=name]');if(D.name)nm.value=D.name;nm.oninput=()=>{{D.name=nm.value;save()}};
function dl(){{document.title='Creative Futures - Day {d["n"]} - '+(D.name||'reflection');window.print()}}
function clr(){{if(confirm('Delete all your answers for Day {d["n"]} on this device?')){{D={{}};localStorage.removeItem(K);location.reload()}}}}
</script></body></html>'''
for k,d in DAYS.items(): open(f'{k}.html','w').write(page(k,d))
idx='''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Creative Futures · Learning diary</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=Fraunces:ital,opsz,wght@0,9..144,900;1,9..144,500&family=Space+Mono:wght@700&display=swap" rel="stylesheet"><style>'''+CSS+'''
.days{display:grid;gap:14px;margin-top:24px}.day{display:block;text-decoration:none;color:var(--navy)}.day .card{margin:0}.day h3{font-family:'Fraunces',serif;font-size:24px;margin:0}.day .tag{margin-top:6px}.soon{opacity:.45}
</style></head><body><div class="head"><div class="curtain">'''+"<i></i>"*40+'''</div><div class="wrap"><div class="kicker">My learning diary · Erasmus+ KA153-YOU</div><h1>Creative <em>Futures</em></h1><p class="lead">One page per day. Rate the activities, write your notes, mark your key competences. At the end of the week your pages become your personal plan.</p></div></div>
<div class="wrap"><div class="days">
<a class="day" href="day1.html"><div class="card" style="--acc:#b6da4c"><span class="n">Day 1</span><h3>Foundations</h3><div class="tag">Monday 23 November</div></div></a>
<a class="day" href="day2.html"><div class="card" style="--acc:#ffc83d"><span class="n">Day 2</span><h3>Theatre &amp; Storytelling</h3><div class="tag">Tuesday 24 November</div></div></a>
<div class="card soon" style="--acc:#7a5cff"><span class="n">Day 3</span><h3>Digital Awareness</h3><div class="tag">Wednesday 25 November · coming</div></div>
<div class="card soon" style="--acc:#ff6a4d"><span class="n">Day 4</span><h3>Wellbeing &amp; Inclusion</h3><div class="tag">Thursday 26 November · coming</div></div>
<div class="card soon" style="--acc:#9ad5ff"><span class="n">Day 5</span><h3>Action &amp; Closing · Personal plan</h3><div class="tag">Friday 27 November · coming</div></div>
</div></div><div class="foot">Creative Futures: Theatre, Tech &amp; European Participation · Amsterdam 2026</div></body></html>'''
open('index.html','w').write(idx); print('ok')
