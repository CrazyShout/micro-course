"""Export the Course learning library as a self-contained public static site.

Usage: python3 tools/sync_from_course.py ../Course/codexing
Only learning content and referenced media are exported. The original Course
workspace remains the editable source of truth.
"""
import argparse
import hashlib
import html
import json
import re
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_js(path):
    text = path.read_text()
    return json.loads(text.split(' = ', 1)[1].rstrip(';\n'))

def write_js(path, variable, data):
    path.write_text('window.' + variable + ' = ' + json.dumps(data, ensure_ascii=False).replace('</', r'<\/') + ';\n')

def source_ref(source):
    original = source.get('path', '')
    public_url = original if original.startswith('https://') else None
    return {
        'name': source.get('name') or Path(original).name,
        'href': public_url,
        'unit': source['unit'],
        **({'locators': source['locators']} if 'locators' in source else {'locator': source['locator']}),
        'provenance': source['provenance'],
    }

def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('The source UI changed; review the publishing adaptation: ' + old[:70])
    return text.replace(old, new, 1)

def guide_html(courses, lessons, introductions):
    count = len(lessons)
    cards = sum(c['cards'] for c in courses.values())
    course_links = ''.join('<p><a href="index.html#' + k + '">' + k + '</a> · ' + str(v['lessons']) + ' 节微课 · ' + str(v['cards']) + ' 张卡片</p>' for k,v in courses.items())
    deck_guides=''
    for course,info in introductions['courses'].items():
        deck_guides+='<section class="panel" id="'+course+'"><h2>'+html.escape(info['title_zh'])+'</h2><p class="english">'+html.escape(info['title_en'])+'</p>'
        deck_guides+='<p><a href="'+html.escape(info['course_url'],quote=True)+'">进入本课程微课 / Open lessons</a> · <a href="cards.html#'+next(l['card_ids'][0] for l in lessons if l['course']==course)+'">查看卡片 / Open cards</a></p>'
        for section in info['sections']:
            deck_guides+='<h3>'+html.escape(section['title_zh'])+' / '+html.escape(section['title_en'])+'</h3><p>'+html.escape(section['body_zh'])+'</p><p class="english">'+html.escape(section['body_en'])+'</p>'
        deck_guides+='</section>'
    return '''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="CS5489 和 CS5222 连续微课、双语记忆卡与交互演示的使用方法。"><title>怎样使用 · Micro Course</title><link rel="stylesheet" href="learning.css"></head><body>
<header><a class="brand" href="index.html">MICRO COURSE</a><nav><a href="index.html">连续微课</a><a href="cards.html">复习卡片</a><a href="notices.html">课程信息 / Notices</a></nav></header>
<main style="max-width:900px;margin:28px auto;padding:0 16px"><section class="hero"><div class="eyebrow">LEARN → PRACTICE → RECALL</div><h1>先理解，再检索</h1><p>'''+str(count)+' 节连续微课 · '+str(cards)+''' 张双语卡片</p></section>
<section class="panel"><h2>课程信息 / Course information</h2><p>评分、提交清单、课件范围与运行提醒见<a href="notices.html">课程信息与学习指南</a>，不再作为记忆卡复习。 / Assessment, submissions, material scope, and setup notes are on the information board.</p></section><section class="panel"><h2>从这里开始</h2>'''+course_links+'''<ol><li>先读具体场景和三个分步例子，再看概念与公式；不熟悉的概念沿“先修补课”返回。</li><li>跟着完整例题手算，再独立尝试提示练习。需要时才展开提示，完成后核对答案。</li><li>不看答案做条件变化题，并用英语解释机制、假设和结论。</li><li>打开对应卡片做检索，再用 Markji 安排间隔复习。长推导和编程题仍应完整重做。</li></ol></section>
'''+deck_guides+'''<section class="panel"><h2>语言与范围</h2><p>中文用于连续串讲；英文术语、英语摘要及中英双语题答帮助过渡到英文考试。“英语口述训练”展示英文摘要与题答，不是整篇中文讲解的逐句翻译。</p><p>本学期 Canvas 是课程范围基准。Extra Resources 来自往年资料，尚未确认为本学期或 QE 的完整范围。新增串讲、类比和练习是 AI 编写的学习辅助。</p><p>卡片中保留原图，以及资料文件名、页码或 Notebook 单元号。Canvas 和历史仓库的完整原文件留在本地资料库；公开的官方文档仍可通过出处链接访问。</p></section>
<section class="panel"><h2>参考书怎么读 / Reading companion</h2><p>50 节均有双语入门场景、150 个讲解步骤与 22 幅入门图。另有 26 节参考书补充、14 幅图示和 26 道双语自测。先看机制，再沿图读一遍例子，最后独立回答自测；图示可点击放大。决策树和 AdaBoost 折叠为选读，可按兴趣展开。</p><p>Machine Learning in Action（2012）与《机器学习实战》（2013）是同一著作的两个语言版本。网络部分参考 Computer Networking: A Top-Down Approach 第 8 版及《图解 HTTP》（2014）；HTTP 缓存、TLS 与 HTTP/3 的版本差异另核对 RFC 9111、8446、9114。新增段落有单独的书页定位，原始 PDF 留在本地。</p><p class="english">Reading supplements add original diagrams and bilingual checks. Book chapters explain mechanisms; Canvas remains the assessment baseline. The English and Chinese editions of Machine Learning in Action are the same work. Legacy code and protocol descriptions are qualified where needed.</p></section><section class="panel"><h2>学习记录与换设备</h2><p>完成标记和待复习标记保存在当前浏览器，可导出 JSON；网站没有账户或云同步。手机、电脑和原来的本地学习页各自保存记录，不会自动合并。自评标记也不会改变 Markji 的复习进度。</p><p>Markji 链接打开原课程牌组。APKG 是便携备份；已经在同一 Markji 牌组学习时，不必重复导入。</p><p><a href="CS5489/exports/CS5489-bilingual.apkg" download>下载 CS5489 APKG</a> · <a href="CS5222/exports/CS5222-bilingual.apkg" download>下载 CS5222 APKG</a></p></section>
<section class="panel"><h2>课程维护</h2><p>页面内容随仓库更新发布。发现解释跳步时，应补那个中间步骤，再用变式检查能否迁移。</p><p><a href="https://github.com/CrazyShout/micro-course" target="_blank" rel="noopener">GitHub 仓库</a> · <a href="publication.json">当前内容与资源清单</a></p></section></main><script>const course=new URLSearchParams(location.search).get('course');const section=course&&document.getElementById(course);if(section)section.scrollIntoView();</script></body></html>'''

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('source',type=Path,nargs='?',default=ROOT.parent/'Course/codexing')
    args=parser.parse_args();source=args.source.resolve()
    learning=load_js(source/'learning-data.js')
    reader=load_js(source/'reader-data.js')
    index=load_js(source/'learning-index.js')
    introductions=json.loads((source/'deck-introductions.json').read_text())
    assert set(introductions['courses'])==set(learning['courses'])
    assert all(len(v['short_description'])<=256 for v in introductions['courses'].values())
    for lesson in learning['lessons']:
        lesson['sources']=[source_ref(s) for s in lesson['sources']]
    for card in reader['cards']:
        card.pop('remote',None)
        card['sources']=[source_ref(s) for s in card['sources']]
    with tempfile.TemporaryDirectory(prefix='.export-',dir=ROOT) as tmp:
        out=Path(tmp)
        for name in ['learning.css','learning-demos.js']:
            shutil.copy2(source/name,out/name)
        notices=load_js(source/'notices-data.js')
        shutil.copy2(source/'notices-data.js',out/'notices-data.js')
        for name in ['notices.html','notices.js']:
            page=(source/name).read_text().replace('index.html','cards.html').replace('learning.html','index.html')
            (out/name).write_text(page)
        page=(source/'learning.html').read_text()
        page=page.replace('href="learning.html"','href="index.html"').replace('href="index.html">复习卡片','href="cards.html">复习卡片').replace('href="LEARNING_GUIDE.md"','href="guide.html"')
        page=page.replace('<title>','<meta name="description" content="CS5489 与 CS5222：连续微课、双语卡片、独立练习和交互演示。"><title>',1)
        (out/'index.html').write_text(page)
        js=(source/'learning.js').read_text().replace('index.html','cards.html')
        start=js.index('l.sources.map(s=>')
        end=js.index(".join('')",start)+len(".join('')")
        js=js[:start]+"l.sources.map(publicSourceHTML).join('')"+js[end:]
        js+="\nfunction publicSourceHTML(s){const label=s.href?'<a target=\"_blank\" rel=\"noopener\" href=\"'+esc(s.href)+'\">'+esc(s.name)+'</a>':'<span>'+esc(s.name)+'</span>';return '<li>'+label+' · '+esc(s.unit+' '+s.locators.join('; '))+' · '+esc(s.provenance)+'</li>';}\n"
        # Project sites share an origin with other GitHub Pages projects.
        js=js.replace('codexing-lessons-v1','micro-course-lessons-v1')
        (out/'learning.js').write_text(js)
        cards=(source/'index.html').read_text().replace('learning.html','index.html').replace('href="README.md"','href="guide.html"')
        old=next(line for line in cards.splitlines() if line.startswith('function sourceHTML(c)'))
        new="function sourceHTML(c){return c.sources.map(s=>{const label=s.href?'<a target=\"_blank\" rel=\"noopener\" href=\"'+escape(s.href)+'\">'+escape(s.name)+'</a>':'<span>'+escape(s.name)+'</span>';return '<li>'+label+' · '+escape(sourceUnit(s.unit)+' '+s.locator)+'<br>'+escape(sourceLabel(s.provenance))+'</li>'}).join('')}"
        cards=replace_once(cards,old,new).replace('codexing-marked-v1','micro-course-marked-v1')
        (out/'cards.html').write_text(cards)
        write_js(out/'learning-data.js','LEARNING_DATA',learning)
        write_js(out/'reader-data.js','COURSE_DATA',reader)
        write_js(out/'learning-index.js','LEARNING_INDEX',index)
        figures=set()
        beginner_figures=set()
        for lesson in learning['lessons']:
            for figure in lesson.get('first_pass',{}).get('figures',[]):
                rel=Path(figure['src'])
                assert rel.parent==Path('learning/figures') and rel.suffix=='.svg',rel
                dst=out/rel;dst.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(source/rel,dst);beginner_figures.add(str(rel))
            figure=lesson.get('reading',{}).get('figure')
            if figure:
                rel=Path(figure['src'])
                assert rel.parent==Path('reading/figures') and rel.suffix=='.svg',rel
                dst=out/rel;dst.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(source/rel,dst);figures.add(str(rel))
        for card in reader['cards']:
            for name in card['media']:
                relative=Path(card['course'])/'media'/name
                assert Path(name).name==name, name
                dst=out/relative;dst.parent.mkdir(parents=True,exist_ok=True)
                if not dst.exists():shutil.copy2(source/relative,dst)
        for course in learning['courses']:
            rel=Path(course)/'exports'/f'{course}-bilingual.apkg'
            dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(source/rel,dest)
        for name in ['katex.min.css','katex.min.js','contrib/auto-render.min.js','LICENSE']:
            rel=Path('vendor/katex')/name
            dst=out/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source/rel,dst)
        shutil.copytree(source/'vendor/katex/fonts',out/'vendor/katex/fonts')
        (out/'guide.html').write_text(guide_html(learning['courses'],learning['lessons'],introductions))
        (out/'deck-introductions.json').write_text(json.dumps(introductions,ensure_ascii=False,indent=2)+'\n')
        (out/'.nojekyll').touch()
        # Content versions prevent mixed old scripts/styles after a Pages update.
        for page_path in out.glob('*.html'):
            def version_asset(match):
                rel=match.group(2)
                target=out/rel
                if not target.is_file():return match.group(0)
                version=hashlib.sha256(target.read_bytes()).hexdigest()[:12]
                return match.group(1)+rel+'?v='+version+match.group(3)
            page_path.write_text(re.sub(r'((?:src|href)=")([^"?]+\.(?:css|js))(?:\?[^"]*)?(")',version_asset,page_path.read_text()))
        manifest={'schema_version':1,'source_snapshot':learning['snapshot'],
                  'beginner_revision':learning.get('beginner_revision'),'beginner_entries':len(learning['lessons']),
                  'beginner_figures':len(beginner_figures),
                  'self_study_revision':learning.get('self_study_revision'),
                  'optional_foundations':len({f['id'] for l in learning['lessons'] for f in l.get('foundations',[])}),
                  'focused_units':sum(len(l.get('units',[])) for l in learning['lessons']),
                  'practical_tasks':len({t['id'] for l in learning['lessons'] for t in l.get('practical_tasks',[])}),
                  'reading_revision':learning.get('reading_revision'),
                  'reading_supplements':sum(bool(l.get('reading')) for l in learning['lessons']),
                  'reading_figures':len(figures),
                  'notices':len(notices['entries']),
                  'moved_card_ids':notices['moved_card_ids'],
                  'courses':{c:{'lessons':v['lessons'],'cards':v['cards']} for c,v in learning['courses'].items()},
                  'total_lessons':len(learning['lessons']),'total_cards':len(reader['cards']),
                  'images':len({(c['course'],m) for c in reader['cards'] for m in c['media']}),
                  'assets':[]}
        for path in sorted(out.rglob('*')):
            if path.is_file():manifest['assets'].append({'path':str(path.relative_to(out)),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        (out/'publication.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        target=ROOT/'docs'
        if target.exists():
            if not (target/'publication.json').is_file():raise RuntimeError('Refusing to replace an unmanaged docs directory')
            shutil.rmtree(target)
        shutil.copytree(out,target)
    # Human-readable authoring copies, excluding raw materials and API tooling.
    notice_dest=ROOT/'content/notices';notice_dest.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source/'notices/README.md',notice_dest/'README.md')
    (notice_dest/'entries.json').write_text(json.dumps(notices,ensure_ascii=False,indent=2)+'\n')
    reading_dest=ROOT/'content/reading';reading_dest.mkdir(parents=True,exist_ok=True)
    beginner_dest=ROOT/'content/learning';beginner_dest.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source/'learning/first-pass.md',beginner_dest/'first-pass.md')
    for name in ['foundations.json','lesson-units.json','practical-tasks.json','coverage-scope.json','coverage.json','card-recovery.json']:
        shutil.copy2(source/'learning'/name,beginner_dest/name)
    shutil.copy2(source/'reading/authoring.md',reading_dest/'lessons.md')
    source_catalog=json.loads((source/'reading/sources.json').read_text())
    (reading_dest/'sources.json').write_text(json.dumps({k:{f:v for f,v in s.items() if f not in ['path','sha256']} for k,s in source_catalog.items()},ensure_ascii=False,indent=2)+'\n')
    for course in learning['courses']:
        dest=ROOT/'content'/course;dest.mkdir(parents=True,exist_ok=True)
        for src,name in [('learning/authoring.md','lessons.md'),('cards/authoring.md','cards.md'),('cards/extra-resources/authoring.md','extra-cards.md')]:
            shutil.copy2(source/course/src,dest/name)
        info=introductions['courses'][course]
        lines=['# '+info['title_zh'],'',info['title_en'],'','[课程微课]('+info['course_url']+') · [牌组介绍]('+info['guide_url']+')','']
        for section in info['sections']:
            lines += ['## '+section['title_zh']+' / '+section['title_en'],'',section['body_zh'],'',section['body_en'],'']
        (dest/'deck-introduction.md').write_text('\n'.join(lines).rstrip()+'\n')
    print(json.dumps({k:v for k,v in manifest.items() if k!='assets'},ensure_ascii=False))
    print('Exported files:',len(manifest['assets'])+1,'bytes:',sum(x['bytes'] for x in manifest['assets']))

if __name__=='__main__':main()
