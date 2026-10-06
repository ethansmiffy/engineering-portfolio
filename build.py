#!/usr/bin/env python3
"""Build a dependency-free static portfolio. Add report PDFs to reports/, then rerun."""
import json, shutil
from html import escape as e
from pathlib import Path
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'docs'
OUT.mkdir(exist_ok=True)
# Only regenerate owned HTML; preserve unrelated source files.
for old in OUT.glob('*.html'): old.unlink()
for folder in ('assets','reports'):
    if (OUT/folder).exists(): shutil.rmtree(OUT/folder)
    shutil.copytree(ROOT/folder,OUT/folder)
shutil.copy2(ROOT/'style.css',OUT/'style.css')
(OUT/'.nojekyll').touch()
projects=json.loads((ROOT/'projects.json').read_text())
def shell(title,desc,body):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{e(desc,quote=True)}"><meta name="theme-color" content="#142834"><title>{e(title)} | Ethan Smith</title><link rel="stylesheet" href="style.css"></head><body><a class="skip" href="#main">Skip to content</a><header><div class="bar"><a class="brand" href="index.html">Ethan Smith<span aria-hidden="true" style="color:#075d85">.</span></a><nav aria-label="Main navigation"><a href="index.html#projects">Projects</a><a href="index.html#about">About</a></nav></div></header><main id="main" class="wrap">{body}</main><footer><div class="wrap">Ethan Smith · Mechanical Engineering · University of Bristol</div></footer></body></html>'''
def write(name,title,desc,body): (OUT/name).write_text(shell(title,desc,body),encoding='utf-8')
cards=''
for p in projects:
 cards+=f'''<article class="card"><a class="picture" href="{p['id']}.html" tabindex="-1" aria-hidden="true"><img src="assets/{p['cover']}" alt="" loading="lazy"></a><div class="card-body"><p class="eyebrow">{e(p['category'])}</p><h3><a href="{p['id']}.html">{e(p['title'])}</a></h3><p>{e(p['intro'])}</p><a class="card-link" href="{p['id']}.html">Explore project<span class="sr-only" hidden> {e(p['title'])}</span></a></div></article>'''
write('index.html','Engineering portfolio','Mechanical engineering projects by Ethan Smith: structural health monitoring, mechanical design, finite-element analysis and heat transfer.',f'''<section class="hero"><div><p class="eyebrow">University of Bristol · MEng Mechanical Engineering</p><h1>Engineering through<br>design and analysis.</h1><p class="lead">I’m Ethan, a final-year mechanical engineering student working across mechanical design, structural analysis and machine learning.</p><a class="button" href="#projects">View selected projects</a></div><figure class="hero-figure"><img src="assets/slide2-image0.png" alt="Deployed vehicle-mounted solar array CAD model"><figcaption>Deployable solar array · Mechanism and gearbox design</figcaption></figure></section><section id="projects"><div class="section-heading"><h2>Selected engineering work</h2><span>Research and design projects / 2024–2026</span></div><div class="grid">{cards}</div></section><section class="about" id="about"><h2>About my work</h2><div><p>My work combines mechanical modelling with computational methods. After leading a five-person structural health monitoring project, I independently extended the research over summer to compare an LSTM model against a published NARX approach.</p><p>Alongside my degree, I’m reconstructing a model Shay steam engine in Autodesk Fusion 360 from inherited engineering drawings. The ongoing project covers 368 unique components and 23 functional subassemblies.</p><p>Python / PyTorch · MATLAB · Abaqus · Autodesk Fusion 360 · SolidWorks</p></div></section>''')
for p in projects:
 metrics=''.join(f'<div class="metric"><strong>{e(v)}</strong><span>{e(label)}</span></div>' for v,label in p['metrics'])
 decisions=''.join(f'<li>{e(x)}</li>' for x in p['decisions'])
 gallery=''.join(f'<figure><a href="assets/{img}" aria-label="Open full-size figure: {e(cap,quote=True)}"><img loading="lazy" src="assets/{img}" alt="{e(cap,quote=True)}"></a><figcaption>{e(cap)}</figcaption></figure>' for img,cap in p['images'])
 table=''
 if p.get('table'):
  table='<div class="table-scroll"><table><caption>Mean ROC-AUC in the reported synthetic-defect evaluation</caption><thead><tr>'+''.join(f'<th scope="col">{e(x)}</th>' for x in p['table'][0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{e(x)}</td>' for x in row)+'</tr>' for row in p['table'][1:])+'</tbody></table></div>'
 reports=[]
 for filename,label in p['reports']:
  fp=ROOT/'reports'/filename
  if not fp.exists():continue
  if fp.read_bytes()[:5]!=b'%PDF-':raise ValueError(f'{filename} is not a PDF')
  view=f'report-{fp.stem}.html'
  reports.append(f'<a class="button" href="{view}">{e(label)}</a>')
  write(view,label,p['title'],f'''<div class="crumb"><a href="{p['id']}.html">Back to {e(p['title'])}</a></div><div class="project-intro"><p class="eyebrow">Project report</p><h1>{e(label)}</h1></div><div class="reader-toolbar"><a class="button" href="reports/{filename}" download>Download PDF</a><a href="reports/{filename}">Open PDF directly</a></div><p class="date">If your browser does not display the embedded document, open the PDF directly or download it.</p><object class="reader" data="reports/{filename}" type="application/pdf" aria-label="{e(label,quote=True)}"><p><a href="reports/{filename}">Read the PDF report</a></p></object>''')
 report_body='<div class="report-list">'+''.join(reports)+'</div>' if reports else '<p class="date">The full report is not currently available on this site.</p>'
 if p.get('report_note'): report_body='<p>'+e(p['report_note'])+'</p>'+report_body
 write(p['id']+'.html',p['title'],p['intro'],f'''<div class="crumb"><a href="index.html#projects">All projects</a></div><div class="project-intro"><p class="eyebrow">{e(p['category'])}</p><h1>{e(p['title'])}</h1><p class="lead">{e(p['intro'])}</p><p class="date">{e(p['date'])}</p></div><figure class="project-image"><img src="assets/{p['cover']}" alt="{e(p['alt'],quote=True)}"><figcaption>{e(p['alt'])}</figcaption></figure><div class="metrics">{metrics}</div><div class="details"><aside class="contents" aria-label="On this page"><a href="#overview">Project overview</a><a href="#contribution">My contribution</a><a href="#approach">Engineering approach</a><a href="#results">Results and scope</a><a href="#figures">Project figures</a><a href="#reports">Reports</a></aside><div class="copy"><section id="overview"><h2>Project overview</h2><p>{e(p['summary'])}</p></section><section id="contribution"><h2>My contribution</h2><p>{e(p['role'])}</p></section><section id="approach"><h2>Engineering approach</h2><ul>{decisions}</ul></section><section id="results"><h2>Results and scope</h2><p>{e(p['results'])}</p>{table}<p class="note">{e(p['limits'])}</p></section><section id="figures"><h2>Project figures</h2><div class="gallery">{gallery}</div></section><section id="reports"><h2>Reports</h2>{report_body}</section></div></div>''')
print(f'Built {len(list(OUT.glob("*.html")))} pages in {OUT}')
