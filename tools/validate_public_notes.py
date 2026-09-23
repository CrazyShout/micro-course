"""Dependency-free validation of the generated online course notes (also used by CI)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re


class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.links=[]; self.math=0; self.details=0; self.images=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for key in ['href','src']:
            if a.get(key):self.links.append(a[key])
        if 'arithmatex' in a.get('class','').split():self.math+=1
        if tag=='details':self.details+=1
        if tag=='img':self.images+=1


def validate(site):
    site=Path(site).resolve(); root=site/'notes'; manifest=json.loads((root/'manifest.json').read_text())
    assert manifest['major_documents']==15
    assert len(manifest['documents'])==18 and sum(d['major'] for d in manifest['documents'])==15
    declared={a['path'] for a in manifest['assets']}|{'manifest.json'}
    actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    assert actual==declared,actual^declared
    for a in manifest['assets']:
        p=root/a['path'];assert p.stat().st_size==a['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256'],p
    parsed={}
    for p in root.rglob('*.html'):
        page=Page();text=p.read_text();page.feed(text);parsed[p.resolve()]=page
        assert len(page.ids)==len(set(page.ids)),('duplicate IDs',p)
        assert not re.search(r'<details\b[^>]*\bmarkdown=|<p>\s*<details\b',text),p
        assert 'notes.css' in text and 'katex.min.js' in text,p
    refs=0
    for p,page in parsed.items():
        for href in page.links:
            u=urlsplit(href)
            if u.scheme in {'http','https','mailto','data'}:continue
            assert not u.scheme and not u.netloc and not u.path.startswith('/'),href
            target=(p.parent/unquote(u.path)).resolve() if u.path else p
            assert target.is_relative_to(site) and target.exists(),(p,href)
            if u.fragment and target in parsed:
                assert unquote(u.fragment) in parsed[target].ids,('missing anchor',p.name,href)
            refs+=1
    forbidden=re.compile(r'/Users/|/private/(?:tmp|var)/|file://|(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{25,})')
    for p in root.rglob('*'):
        if p.is_file() and p.suffix in {'.html','.css','.json','.py'}:
            assert not forbidden.search(p.read_text()),('private path or credential-like data',p)
        if p.suffix=='.pdf':
            assert b'/Users/' not in p.read_bytes() and b'file://' not in p.read_bytes(),p
        assert not any(x in p.relative_to(root).parts for x in ['checks','materials','my_tutorial','.venv']),p
    result={'status':'passed','reading_documents':18,'major_documents':15,'directory_pages':3,
            'html_pages':len(parsed),'local_links_and_anchors':refs,
            'math_blocks':sum(p.math for p in parsed.values()),'images_in_pages':sum(p.images for p in parsed.values()),
            'answer_blocks':sum(p.details for p in parsed.values()),'pdf_pages':sum(p['pages'] for p in manifest['pdfs'])}
    assert len(parsed)==21 and result['pdf_pages']==232
    return result


if __name__=='__main__':
    import sys
    print(json.dumps(validate(sys.argv[1]),ensure_ascii=False))
