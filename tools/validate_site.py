"""Validate published data, lesson links, local assets, and deployment boundaries."""
import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for name,value in attrs:
            if name in ['src','href'] and value:self.links.append(value)

def load_js(path):return json.loads(path.read_text().split(' = ',1)[1].rstrip(';\n'))

def main():
    p=argparse.ArgumentParser();p.add_argument('site',type=Path,nargs='?',default=Path(__file__).resolve().parents[1]/'docs');site=p.parse_args().site.resolve()
    manifest=json.loads((site/'publication.json').read_text())
    declared={a['path'] for a in manifest['assets']}|{'publication.json'}
    actual={str(f.relative_to(site)) for f in site.rglob('*') if f.is_file()}
    assert actual==declared,('Unlisted/missing files',actual^declared)
    for asset in manifest['assets']:
        file=site/asset['path'];assert file.stat().st_size==asset['bytes'] and hashlib.sha256(file.read_bytes()).hexdigest()==asset['sha256'],asset['path']
    def local_link(value,base=site):
        u=urlsplit(value)
        if u.scheme in ['https','http','mailto','data','blob'] or not u.path:return
        assert not u.scheme and not u.netloc,value
        assert not u.path.startswith('/'),('Root-relative link breaks project-site portability',value)
        target=(base/unquote(u.path)).resolve();assert target.is_relative_to(site),value
        assert target.exists(),('Missing link',value)
    for file in site.rglob('*.html'):
        parsed=Links();parsed.feed(file.read_text())
        for value in parsed.links:local_link(value,file.parent)
    for file in site.rglob('*.css'):
        for value in re.findall(r'url\([\'"]?([^\)\'" ]+)',file.read_text()):local_link(value,file.parent)
    reader=load_js(site/'reader-data.js');learning=load_js(site/'learning-data.js');index=load_js(site/'learning-index.js')
    cards={c['id']:c for c in reader['cards']};lessons={l['id']:l for l in learning['lessons']}
    assert len(cards)==len(reader['cards'])==manifest['total_cards']
    assert len(lessons)==len(learning['lessons'])==manifest['total_lessons']
    assert set(index['card_context'])==set(cards)
    linked=[];images=set();reading_figures=set();reading_count=0
    for lesson in lessons.values():
        linked.extend(lesson['card_ids'])
        assert all(x in lessons for x in lesson['prerequisites']+lesson['related'])
        assert all(c in cards for c in lesson['card_ids'])
        for ref in lesson['sources']:assert 'path' not in ref and (ref['href'] is None or ref['href'].startswith('https://'))
        if lesson.get('reading'):
            reading_count+=1;r=lesson['reading']
            for field in ['body','check_q','check_a']:
                assert re.search('[\u3400-\u9fff]',r[field]['zh']), (lesson['id'],field)
                assert len(re.findall('[A-Za-z]+',r[field]['en']))>=4,(lesson['id'],field)
                assert all(r[field+'_html'][lang] for lang in ['zh','en'])
            assert r['sources'] and isinstance(r['optional'],bool)
            for ref in r['sources']:
                assert 'path' not in ref and ref['locator']
                assert ref['href'] is None or ref['href'].startswith('https://www.rfc-editor.org/')
            if r.get('figure'):
                f=r['figure'];local_link(f['src']);reading_figures.add(f['src'])
                assert f['alt'] and all(f['caption_'+lang] for lang in ['zh','en'])
                svg=(site/f['src']).read_text()
                assert '<title ' in svg and '<desc ' in svg and '<script' not in svg
    assert len(linked)==len(set(linked)) and set(linked)==set(cards)
    for card in cards.values():
        assert 'remote' not in card and card['learning_context']
        for field in ['question_en','question_zh','answer_en','answer_zh']:
            assert card.get(field,'').strip(),(card['id'],field)
            assert card.get(field+'_html','').strip(),(card['id'],field+'_html')
            assert re.search('[\u3400-\u9fff]',card[field]) if field.endswith('zh') else len(re.findall('[A-Za-z]+',card[field]))>3
        for ref in card['sources']:
            assert reader.get('source_labels',{}).get(ref['provenance']),('Missing bilingual provenance',ref['provenance'])
        assert card.get('microcourse_links'),card['id']
        for link in card['microcourse_links']:
            assert link['id'] in lessons and link['url']=='https://crazyshout.github.io/micro-course/?lesson='+link['id']
        for lid in card['learning_context']['lesson_ids']:assert lid in lessons
        for ref in card['sources']:assert 'path' not in ref and (ref['href'] is None or ref['href'].startswith('https://'))
        for image in card['media']:
            rel=card['course']+'/media/'+image;local_link(rel);images.add(rel)
    assert len(images)==manifest['images']
    assert reading_count==manifest['reading_supplements']
    assert len(reading_figures)==manifest['reading_figures']
    introductions=json.loads((site/'deck-introductions.json').read_text())
    assert set(introductions['courses'])==set(manifest['courses'])
    for course,intro in introductions['courses'].items():
        assert len(intro['short_description'])<=256
        assert intro['guide_url'].endswith('guide.html?course='+course)
        assert 'id="'+course+'"' in (site/'guide.html').read_text()
    for course,counts in manifest['courses'].items():
        assert sum(c['course']==course for c in cards.values())==counts['cards']
        assert sum(l['course']==course for l in lessons.values())==counts['lessons']
        local_link(course+'/exports/'+course+'-bilingual.apkg')
    forbidden=re.compile(r'/Users/|/private/tmp/|(?:https?://)?(?:localhost|127\.0\.0\.1)(?=[:/])|(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{25,})')
    for file in site.rglob('*'):
        if file.is_file() and file.suffix in ['.html','.js','.css','.json','.md']:
            assert not forbidden.search(file.read_text()),('Local path or credential-like data',str(file.relative_to(site)))
        assert not any(part in ['materials','checks','.git','markji-ready'] for part in file.relative_to(site).parts),file
    print(json.dumps({'status':'passed','files':len(actual),'lessons':len(lessons),'cards':len(cards),'images':len(images),'reading_supplements':reading_count,'reading_figures':len(reading_figures),'all_local_links_resolve':True,'manifest_matches':True,'private_sync_metadata_excluded':True},ensure_ascii=False))

if __name__=='__main__':main()
