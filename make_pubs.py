

# Setup bibtexparser
# !pip install bibtexparser

import pandas as pd
import bibtexparser
import re


with open('publications.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

def remove_braces(s):
    return re.sub(r'[\{\}]', '', s)
def clean(s):
    return re.sub(r'[\{\}:#\.\/]', '', s)

df = pd.DataFrame()

df['ID'] = [clean(e['ID']) for e in bib_database.entries]
df['year'] = [e['year'] for e in bib_database.entries]
df['title'] = [remove_braces(e['title']) for e in bib_database.entries]
df['author'] = [remove_braces(e['author']) for e in bib_database.entries]
df['keywords'] = [e['keywords'] for e in bib_database.entries]
df['month'] = [e['month'] if 'month' in e else 1 for e in bib_database.entries]
df['url'] = [e['url'] if 'url' in e else "" for e in bib_database.entries]
df['abstract'] = [e['abstract'] if 'abstract' in e else "" for e in bib_database.entries]

assert((df['ID'].value_counts() > 1).sum() == 0)

def get_venue(e):
    if "booktitle" in e:
        return e['booktitle']
    elif "journal" in e:
        if e['journal'] == "CoRR":
            return "CoRR (arXiv)"
        else: 
            return e['journal']
    elif "institution" in e:
        return f"""{e['institution']} Technical Report"""
    else:
        return "arXiv"
        
df['venue'] = [remove_braces(get_venue(e)) for e in bib_database.entries]

df['bib'] = bib_database.entries





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
    # f.write(f"""\t<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#{row['ID']}_nat_bib" role="button" aria-expanded="false" aria-controls="CollapseBib">natbib</a></li>\n""")
    if len(row['abstract']) > 0:
        f.write(f"""\t<li><a class="btn btn-primary btn-sm" data-toggle="collapse" href="#{row['ID']}_abs" role="button" aria-expanded="false" aria-controls="CollapseAbstract">abstract</a></li>\n""")
    if "url" in row:
        f.write(f"""\t<li><a class="btn btn-primary btn-sm" target="_blank" href="{row["url"]}">paper</a></li>\n""")
    if "code" in row['bib']:
        f.write(f"""\t<li><a class="btn btn-primary btn-sm" target="_blank" href="{row['bib']["code"]}">code</a></li>\n""")

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

def write_nat_bib(bib_id, r, f):
    # f.write(f"""<div id="{bib_id}_nat_bib" class="collapse nat-bibtex-entry">""")
    # f.write('<div class="card card-body">')
    authors = ", ".join(map(str.strip, r["author"].split(" and ")))
    authors = authors[::-1].replace(",", ", and"[::-1], 1)[::-1]
    f.write("<p>" + authors + 
        ". <i>\"" + r['title'] + ".\" </i>" +
        "<b>" + r['venue'] + "</b>, " +
        r['year'] + ".</p>")
    # f.write('</div></div>\n')
        
    
def write_entries(df, f):
    for (i,r) in df.iterrows():
        print(r['ID'])
        f.write(f"""<div id="{r['ID']}" class="publication">\n""")
        
        f.write('<div class="summary">')
        write_nat_bib(r['ID'], r, f)
        # write_authors(r['author'], f)
        # f.write(f"""<div class="title">{r['title']}</div>""")
        # f.write('<div class="venue">')
        # f.write(r['venue'])
        # f.write('</div>\n')
        # f.write(f"""<div class="year">{r['year']}</div>""")
        f.write('</div>')
        
        write_links(r, f)
        
        f.write("""<div class="cards">""")
        f.write(f"""<div id="{r['ID']}_abs" class="collapse abstract"><div class="card card-body">{r['abstract']}</div></div>""")
        write_bib(r['ID'], r['bib'], f)

        f.write("</div>")
        
        f.write('</div>\n\n')
        
        
        
published = df[df['keywords'].str.contains("peerrev") | df['keywords'].str.contains("techreport")].sort_values(["year", "month", "title"], ascending=[False, False, True])
arxivpre = df[df['keywords'].str.contains("arxivpre")].sort_values(["year", "month", "title"], ascending=[False, False, True])

        
with  open("publications.md", "w") as f:
#     f.write("""---
# layout: default
# title: "Publications"
# description: "Recent Publications"
# group: navigation
# order: 2
# ---

# # ArXiv Preprints

# """)
#     write_entries(arxivpre, f)
    
#     f.write("""

# <br/><br/>

# ---

# # Publications


# """)
    f.write("""---
layout: default
title: "Publications"
description: "Recent Publications"
group: navigation
order: 2
---


# Publications


<!-- This file is automatically generated to make modifications to entries update the publications.bib file in the same location. -->


""")

    write_entries(df.sort_values(["year", "month", "title"], ascending=[False, False, True]), f)


