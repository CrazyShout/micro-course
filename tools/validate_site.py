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
    notices=load_js(site/'notices-data.js');notice_ids={n['id'] for n in notices['entries']}
    assert len(notice_ids)==len(notices['entries'])==manifest['notices']
    assert notices['moved_card_ids']==manifest['moved_card_ids']
    assert set(notices['moved_card_ids']).isdisjoint(cards)
    assert all(c['kind']!='admin' for c in cards.values())
    for n in notices['entries']:
        assert n['material_snapshot'] and n['sources'] and all(lid in lessons for lid in n['lesson_ids'])
        for lang in ['zh','en']:assert n['body_'+lang] and n['body_'+lang+'_html'] and n['title_'+lang]
        for s in n['sources']:assert 'path' not in s and (s['href'] is None or s['href'].startswith('https://'))
    for name in ['notices.html','notices.js','notices-data.js']:local_link(name)
    assert len(cards)==len(reader['cards'])==manifest['total_cards']
    assert len(lessons)==len(learning['lessons'])==manifest['total_lessons']
    assert set(index['card_context'])==set(cards)
    linked=[];images=set();reading_figures=set();reading_count=0;beginner_figures=set();practice_assets=set()
    for lesson in lessons.values():
        assert 'foundations' in lesson and 'units' in lesson and 'practical_tasks' in lesson
        study=lesson['study_route'];ids=study['first_pass']+study['after_practice']
        assert study['first_pass'] and len(ids)==len(set(ids)) and set(ids)==set(lesson['card_ids'])
        assert study['note']['zh'] and study['note']['en']
        for item in lesson['foundations']:
            for field in ['title','body','worked_q','worked_a','check_q','check_a']:
                assert item[field]['zh'] and item[field]['en'] and item[field+'_html']['zh'] and item[field+'_html']['en']
            assert item['sources']
        for unit in lesson['units']:
            assert set(unit['card_ids'])<=set(lesson['card_ids'])
            for field in ['title','goal','explain','worked_q','worked_a','practice_q','hint','practice_a','transfer_q','transfer_a']:
                assert unit[field]['zh'] and unit[field]['en'] and unit[field+'_html']['zh'] and unit[field+'_html']['en']
        for task in lesson['practical_tasks']:
            assert lesson['id'] in task['lessons']
            for field in ['title','goal','instructions','acceptance']:assert task[field]['zh'] and task[field]['en']
            for attachment in task.get('attachments',[]):
                local_link(attachment['href']);practice_assets.add(attachment['href'])
                assert attachment['label']['zh'] and attachment['label']['en']
            if task.get('figure'):
                f=task['figure'];local_link(f['src']);practice_assets.add(f['src'])
                assert f['alt'] and f['caption']['zh'] and f['caption']['en']
        beginner=lesson['first_pass']
        assert len(beginner['steps'])==len(beginner['steps_html'])==3,lesson['id']
        for pair in [beginner['start'],beginner['trap'],*beginner['steps']]:
            assert re.search('[\u3400-\u9fff]',pair['zh']) and len(re.findall('[A-Za-z]+',pair['en']))>=4,lesson['id']
        for figure in beginner['figures']:
            local_link(figure['src']);beginner_figures.add(figure['src'])
            assert figure['alt'] and figure['caption_zh'] and figure['caption_en']
            svg=(site/figure['src']).read_text()
            assert '<title ' in svg and '<desc ' in svg and '<script' not in svg
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
    # Article pilots retain the existing bilingual exercises and recovery anchors.
    article_ids=[]
    for lesson in lessons.values():
        article=lesson.get('article')
        if not article:continue
        article_ids.append(lesson['id'])
        assert article['lesson_id']==lesson['id']
        assert all(article['lede_html'][lang] and article['title'][lang] for lang in ['zh','en'])
        sections=article['sections'];section_ids={s['id'] for s in sections}
        assert len(section_ids)==len(sections)
        blocks=[b for s in sections for b in s['blocks']]
        assert sum(b['type']=='demo' for b in blocks)==1
        assert sorted(b['part'] for b in blocks if b['type']=='exercise')==['practice','transfer','worked']
        unit_ids={u['id'] for u in lesson['units']};foundation_ids={f['id'] for f in lesson['foundations']}
        for block in blocks:
            assert block['type'] in {'prose','figure','foundation','exercise','unit','demo','recap'}
            if block['type']=='prose':assert block['text'] and block['html']
            elif block['type']=='figure':
                assert block['ref'] in {f['src'] for f in lesson['first_pass']['figures']+article.get('figures',[])};local_link(block['ref'])
            elif block['type']=='foundation':assert block['ref'] in foundation_ids
            elif block['type']=='unit':assert block['ref'] in unit_ids
            elif block['type']=='demo':assert block['ref'] in {'gaussian-score','cafe-capacity'}
        mapped=set()
        for objective in article['objective_map']:
            assert set(objective['sections'])<=section_ids
            assert set(objective['cards'])<=set(lesson['card_ids'])
            mapped.update(objective['cards'])
        assert set(lesson['study_route']['first_pass'])<=mapped
        assert article['sources']
        assert all(s['name'] and s['locator'] and 'path' not in s for s in article['sources'])
    assert article_ids==manifest.get('article_lessons',[])
    if article_ids:
        for name in ['learning-article.js','learning-article.css','learning-article-demos.js']:local_link(name)
    article_figures={f['src'] for l in lessons.values() for f in l.get('article',{}).get('figures',[])}
    assert len(article_figures)==manifest.get('article_figures',0)
    for name in article_figures:
        local_link(name);svg=(site/name).read_text()
        assert '<title' in svg and '<desc' in svg and '<script' not in svg
    route=learning['curriculum'];assert set(route['courses'])==set(learning['courses'])
    unit_count=activity_count=item_count=0
    preview_ids=set()
    for course,c in route['courses'].items():
        units={u['id']:u for u in c['units']};activities={a['id']:a for a in c['activities']}
        assert len(units)==len(c['units']) and len(activities)==len(c['activities'])
        unit_count+=len(units);activity_count+=len(activities)
        reached=set(c['extension_lessons'])
        for u in units.values():
            reached.update(l['id'] for l in u['lessons'])
            assert all(a in activities and u['id'] in activities[a]['units'] for a in u['activities'])
            for l in u['lessons']:assert l['lead_html']['zh'] and l['lead_html']['en']
            assert u['intro_html']['zh'] and u['intro_html']['en'] and u['outcomes_html'] and u['sources']
        for a in activities.values():
            assert all(u in units and a['id'] in units[u]['activities'] for u in a['units'])
            assert bool(a['units']) != (a['id'] in c['course_activities'])
            reached.update(a['lesson_ids']);item_count+=len(a['items'])
            assert len({i['id'] for i in a['items']})==len(a['items'])
            for item in a['items']:
                reached.update(item['lesson_ids']);preview_ids.update(item['card_ids'])
                for field in ['title','task','approach','check','pitfall']:
                    assert item[field+'_html']['zh'] and item[field+'_html']['en']
                assert item['sources'] and all(cid in cards and cards[cid]['course']==course for cid in item['card_ids'])
        assert reached=={l['id'] for l in lessons.values() if l['course']==course and l['status']!='preview'}
    assert set(route['card_previews'])==preview_ids
    for cid,card in route['card_previews'].items():
        assert set(card)=={'id','course','question_zh_html','question_en_html','answer_zh_html','answer_en_html','front_media','back_media'}
        assert all(card[f]==cards[cid][f] for f in card)
        for name in card['front_media']+card['back_media']:local_link(card['course']+'/media/'+name)
    assert (unit_count,activity_count,item_count)==(manifest['teaching_units'],manifest['teaching_activities'],manifest['activity_items'])
    for name in ['learning-curriculum.js','learning-curriculum.css']:local_link(name)
    assert {o['lesson_id'] for o in learning['coverage']['objectives']}==set(lessons)
    assert manifest['optional_foundations']==len({f['id'] for l in lessons.values() for f in l['foundations']})
    assert manifest['focused_units']==sum(len(l['units']) for l in lessons.values())
    assert manifest['practical_tasks']==len({t['id'] for l in lessons.values() for t in l['practical_tasks']})
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
            assert link['id'] in lessons
            expected='https://crazyshout.github.io/micro-course/?lesson='+link['id']
            if link.get('unit'):
                unit=next(u for u in lessons[link['id']]['units'] if u['id']==link['unit'])
                assert card['id'] in unit['card_ids']
                assert link['title_zh']==unit['title']['zh'] and link['title_en']==unit['title']['en']
                expected+='&unit='+link['unit']
            assert link['url']==expected
        for lid in card['learning_context']['lesson_ids']:assert lid in lessons
        for ref in card['sources']:assert 'path' not in ref and (ref['href'] is None or ref['href'].startswith('https://'))
        for image in card['media']:
            rel=card['course']+'/media/'+image;local_link(rel);images.add(rel)
    assert not list(site.rglob('*.apkg')), 'Retired package files must not be published'
    for page in site.glob('*.html'):
        assert '.apkg' not in page.read_text().lower(), 'Retired package download link'
    assert len(practice_assets)==manifest['practice_assets']
    assert sum(len(l['study_route']['first_pass']) for l in lessons.values())==manifest['first_pass_cards']
    assert len(images)==manifest['images']
    assert reading_count==manifest['reading_supplements']
    assert len(reading_figures)==manifest['reading_figures']
    assert len(beginner_figures)==manifest['beginner_figures']
    assert manifest['beginner_entries']==len(lessons)
    introductions=json.loads((site/'deck-introductions.json').read_text())
    assert set(introductions['courses'])==set(manifest['courses'])
    for course,intro in introductions['courses'].items():
        assert len(intro['short_description'])<=256
        own=[c for c in cards.values() if c['course']==course]
        npreview=sum(c['source_status']=='historical_preview' for c in own)
        assert intro['counts']=={'total':len(own),'current_support':len(own)-npreview,'historical_preview':npreview,'lessons':manifest['courses'][course]['lessons']}
        scope=next(s for s in intro['sections'] if s['title_en']=='Current scope and historical preview')
        assert re.search(r'\b'+str(len(own)-npreview)+r'\b',scope['body_en']) and re.search(r'\b'+str(npreview)+r'\b',scope['body_en'])
        assert intro['guide_url'].endswith('guide.html?course='+course)
        assert 'id="'+course+'"' in (site/'guide.html').read_text()
    for course,counts in manifest['courses'].items():
        assert sum(c['course']==course for c in cards.values())==counts['cards']
        assert sum(l['course']==course for l in lessons.values())==counts['lessons']
    forbidden=re.compile(r'/Users/|/private/tmp/|(?:https?://)?(?:localhost|127\.0\.0\.1)(?=[:/])|(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{25,})')
    for file in site.rglob('*'):
        if file.is_file() and file.suffix in ['.html','.js','.css','.json','.md','.py','.txt']:
            assert not forbidden.search(file.read_text()),('Local path or credential-like data',str(file.relative_to(site)))
        assert not any(part in ['materials','checks','.git','markji-ready'] for part in file.relative_to(site).parts),file
    print(json.dumps({'status':'passed','files':len(actual),'lessons':len(lessons),'article_lessons':article_ids,'teaching_units':unit_count,'activities':activity_count,'activity_items':item_count,'cards':len(cards),'images':len(images),'reading_supplements':reading_count,'reading_figures':len(reading_figures),'all_local_links_resolve':True,'manifest_matches':True,'private_sync_metadata_excluded':True},ensure_ascii=False))

if __name__=='__main__':main()
