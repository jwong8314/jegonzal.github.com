

# Setup bibtexparser
# !pip install bibtexparser

import pandas as pd
import bibtexparser
with open('publications.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

df = pd.DataFrame()
df['ID'] = [e['ID'] for e in bib_database.entries]
df['year'] = [e['year'] for e in bib_database.entries]
df['title'] = [e['title'].replace("{", "").replace("}","") for e in bib_database.entries]
df['author'] = [e['author'].replace("{", "").replace("}","") for e in bib_database.entries]
df['keywords'] = [e['keywords'] for e in bib_database.entries]
df['month'] = [e['month'] if 'month' in e else 1 for e in bib_database.entries]
df['url'] = [e['url'] if 'url' in e else "" for e in bib_database.entries]
df['abstract'] = [e['abstract'] if 'abstract' in e else "" for e in bib_database.entries]
df['bib'] = bib_database.entries
df.head()


published = df[df['keywords'].str.contains("peerrev") | df['keywords'].str.contains("techreport")].sort_values(["year", "month", "title"], ascending=[False, False, True])
arxivpre = df[df['keywords'].str.contains("arxivpre")].sort_values(["year", "month", "title"], ascending=[False, False, True])



def write_authors(authors, f):
    f.write('<div class="authors">\n')
    f.write('<ul class="author">\n')
    print(authors)
    for author in map(str.strip, authors.split(" and ")):
        f.write(f"\t<li>{author}</li>\n")
    f.write("</ul>\n")
    f.write('</div>\n')

def write_links(row, f):
    f.write('<div class="links">\n')
    f.write("<ul>\n")
    f.write(f"""\t<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#{row['ID']}_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">bibtex</a></li>\n""")
    if len(row['abstract']) > 0:
        f.write(f"""\t<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#{row['ID']}_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>\n""")
    if "url" in row:
        f.write(f"""\t<li><a class="btn btn-primary btn-sm" href="{row["url"]}">paper</a></li>\n""")
    if "code" in row['bib']:
        f.write(f"""\t<li><a class="btn btn-primary btn-sm" href="{row['bib']["code"]}">code</a></li>\n""")


    f.write("</ul>\n")
    f.write('</div>\n')
    
def write_bib(bib_id, bib, f):
    f.write(f"""<div id="{bib_id}_bib" class="collapse bibtex-entry">""")
    f.write('<div class="card card-body">')
    f.write('<pre><code class="language-bib" data-lang="bib">\n')
    db = bibtexparser.bibdatabase.BibDatabase()
    db.entries = [bib]
    f.write(bibtexparser.dumps(db).replace("{{", "{ {").replace("}}","} }").strip() +"\n")
    f.write('</code></pre></div></div>\n')
    
def write_venue(r, f):
    f.write('<div class="venue">')
    if "booktitle" in r['bib']:
        f.write(r['bib']['booktitle'].replace("{", "").replace("}",""))
    elif "journal" in r['bib']:
        f.write(r['bib']['journal'].replace("{", "").replace("}",""))
    elif "institution" in r['bib']:
        f.write(f"""{r['bib']['institution']} Technical Report""")
    else:
        f.write("Unpublished.")
    f.write('</div>\n')
    
def write_entries(df, f):
    for (i,r) in df.iterrows():
        print(r['ID'])
        f.write(f"""<div id="{r['ID']}" class="publication">\n""")
        
        f.write('<div class="summary">')
        write_authors(r['author'], f)
        f.write(f"""<div class="title">{r['title']}</div>""")
        write_venue(r,f)
        f.write(f"""<div class="year">{r['year']}</div>""")
        f.write('</div>')
        
        write_links(r, f)
        
        f.write("""<div class="cards">""")
        f.write(f"""<div id="{r['ID']}_abs" class="collapse abstract"><div class="card card-body">{r['abstract']}</div></div>""")
        write_bib(r['ID'], r['bib'], f)
        f.write("</div>")
        
        f.write('</div>\n\n')
        
        
        
        
        
with  open("publications.md", "w") as f:
    f.write("""---
layout: default
title: "Publications"
description: "Recent Publications"
group: navigation
order: 2
---

# ArXiv Preprints

""")
    write_entries(arxivpre, f)
    
    f.write("""

<br/><br/>

---

# Publications


""")
    write_entries(published, f)


