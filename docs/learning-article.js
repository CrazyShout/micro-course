'use strict';
// Two editorial pilots share the existing exercises, companions, and card identities.
let articleLanguage = 'zh';

function articlePair(value, label='English') {
  return '<div class="zh">'+value.zh+'</div><details class="article-translation"><summary>'+esc(label)+'</summary><div lang="en">'+value.en+'</div></details>';
}
function articleTitle(title) {
  return '<span class="zh">'+esc(title.zh)+'</span><span class="english" lang="en">'+esc(title.en)+'</span>';
}
function articleExercise(item, part, key) {
  const names={worked:['一起算完这一步','Work through the example'],practice:['你来补一步','Try the next step'],transfer:['换个条件，自己来','Try a changed condition']};
  let body='<div class="exercise-question">'+articlePair(item[part+'_q_html'],'English question')+'</div>';
  if(part==='worked') body+='<div class="article-solution">'+articlePair(item.worked_a_html,'English solution')+'</div>';
  else {
    if(part==='practice') body+='<details class="article-hint"><summary>需要一点提示 / Hint</summary>'+articlePair(item.hint_html,'English hint')+'</details>';
    body+='<details class="article-answer"><summary>想好后核对 / Check your answer</summary>'+articlePair(item[part+'_a_html'],'English solution')+'</details>';
  }
  return '<div class="article-exercise" data-exercise="'+esc(key+':'+part)+'"><h3>'+articleTitle({zh:names[part][0],en:names[part][1]})+'</h3>'+body+'</div>';
}
function articleFoundation(f) {
  return '<details id="foundation-'+esc(f.id)+'" class="article-aside"><summary>'+articleTitle(f.title)+'</summary>'+articlePair(f.body_html)+
    '<h3>跟着试一次 / A small example</h3>'+articlePair(f.worked_q_html)+articlePair(f.worked_a_html)+
    '<h3>自己检查 / Quick check</h3>'+articlePair(f.check_q_html)+'<details class="article-answer"><summary>核对 / Solution</summary>'+articlePair(f.check_a_html)+'</details>'+companionSources(f.sources)+'</details>';
}
function articleUnit(u, block) {
  if(block.part==='explain') return '<div id="unit-'+esc(u.id)+'" class="article-unit" tabindex="-1">'+articlePair(u.explain_html)+ '</div>';
  if(block.part!=='all') return articleExercise(u,block.part,'unit:'+u.id);
  const body=articlePair(u.explain_html)+articleExercise(u,'worked','unit:'+u.id)+articleExercise(u,'practice','unit:'+u.id)+articleExercise(u,'transfer','unit:'+u.id)+companionSources(u.sources);
  return '<details id="unit-'+esc(u.id)+'" class="article-aside" '+(block.collapsed?'':'open')+'><summary>'+articleTitle(u.title)+'</summary>'+body+'</details>';
}
function articleBlock(l,b) {
  switch(b.type) {
    case 'prose': return '<div class="article-prose zh">'+b.html+'</div>';
    case 'figure': {
      const f=l.first_pass.figures.find(x=>x.src===b.ref);
      return '<figure class="article-figure"><a href="'+esc(f.src)+'" target="_blank" rel="noopener"><img src="'+esc(f.src)+'" alt="'+esc(f.alt)+'" loading="lazy"></a><figcaption>'+articleTitle({zh:f.caption_zh,en:f.caption_en})+' <a href="'+esc(f.src)+'" target="_blank" rel="noopener">放大 / Enlarge</a></figcaption></figure>';
    }
    case 'foundation': return articleFoundation(l.foundations.find(f=>f.id===b.ref));
    case 'exercise': return articleExercise(l,b.part,'lesson');
    case 'unit': return articleUnit(l.units.find(u=>u.id===b.ref),b);
    case 'demo': return '<div class="article-demo" data-article-demo="'+esc(b.ref)+'"></div>';
    case 'recap': return '<details class="article-translation article-recap"><summary>试着用英语讲清楚 / Explain it in English</summary><div lang="en">'+l.recap_en_html+'</div></details>';
    default: throw new Error('Unrecognized article block: '+b.type);
  }
}
function articleCards(l) {
  const byId=Object.fromEntries(l.cards.map(c=>[c.id,c]));
  const list=ids=>'<ul class="article-card-list">'+ids.map(id=>{const c=byId[id];return '<li><a href="cards.html?lesson='+l.id+'#'+id+'"><small>'+esc(id)+'</small>'+'<span class="zh">'+c.question_zh_html+'</span><span class="english">'+c.question_en_html+'</span>'+'</a></li>'}).join('')+'</ul>';
  return '<section id="article-review" class="article-review" tabindex="-1"><div class="eyebrow">UNDERSTAND → RECALL</div><h2>'+articleTitle({zh:'现在，把理解变成记得住的知识',en:'Turn understanding into recall'})+'</h2><p class="zh">先用这 '+l.study_route.first_pass.length+' 张现有卡检查自己。不要逐字背本文：试着说出结论，以及为什么。</p><p class="english">Start with these '+l.study_route.first_pass.length+' existing cards. Explain the conclusion and its reason, rather than reciting this article.</p><a class="article-cta" href="'+esc(D.courses[l.course].markji_url)+'" target="_blank" rel="noopener">去 Markji 复习 / Open Markji ↗</a><p class="article-caption">打开原牌组后按下方卡号搜索；链接不会自动选卡或更改复习排程。<br>Search these IDs in the original deck; this link does not select cards or change your schedule.</p>'+list(l.study_route.first_pass)+'<details class="article-aside"><summary>后续再看其余 '+l.study_route.after_practice.length+' 张 / More cards for later</summary>'+list(l.study_route.after_practice)+'</details></section>';
}
function articleSources(l) {
  const refs=l.article.sources.map(s=>'<li><strong>'+esc(s.name)+'</strong> · '+esc(s.locator)+'<p>'+esc(s.note)+'</p></li>').join('');
  return '<details class="article-sources"><summary>课堂、Tutorial 与教学改编的出处 / Sources</summary><ul>'+refs+'</ul><p>教学例子用于解释课程知识；不代表教师原题、真实测量或完整 QE 范围。</p></details>';
}
function applyArticleLanguage(value) {
  document.body.dataset.language=value;
  document.querySelectorAll('.article-translation').forEach(d=>{d.open=value!=='zh';});
}
function revealArticleTarget(target) {
  if(!target) return;
  for(let el=target;el&&el!==document.body;el=el.parentElement) if(el.tagName==='DETAILS') el.open=true;
  requestAnimationFrame(()=>{target.scrollIntoView({block:'start',behavior:'instant'});target.focus({preventScroll:true});});
}
window.renderArticleLesson=function(l) {
  const a=l.article,seq=D.lessons.filter(x=>x.course===l.course),i=seq.findIndex(x=>x.id===l.id);
  const titleParts=a.title.zh.split('，'),heading=titleParts.map((part,i)=>'<span class="title-clause">'+esc(part)+(i<titleParts.length-1?'，':'')+'</span>').join('');
  document.body.dataset.view='article';
  $('#nav-controls').open=false;
  document.title=a.title.zh+' · '+l.id.toUpperCase()+' · Micro Course';
  const sections=a.sections.map(s=>{
    const content=s.blocks.map(b=>articleBlock(l,b)).join('');
    return s.optional?'<details id="article-'+s.id+'" class="article-section article-optional" tabindex="-1"><summary>'+articleTitle(s.title)+' <small>选读 / Optional</small></summary>'+content+'</details>':'<section id="article-'+s.id+'" class="article-section" tabindex="-1"><h2>'+articleTitle(s.title)+'</h2>'+content+'</section>';
  }).join('');
  const referencedUnits=new Set(a.sections.flatMap(s=>s.blocks.filter(b=>b.type==='unit').map(b=>b.ref)));
  const extraUnits=l.units.filter(u=>!referencedUnits.has(u.id)).map(u=>articleUnit(u,{part:'all',collapsed:true})).join('');
  $('#main').innerHTML='<article class="lesson-article"><div class="article-topline"><a href="#'+l.course+'">← '+l.course+' 课程目录</a><label for="language" class="sr-only">阅读语言 / Reading language</label><select id="language" aria-label="阅读语言 / Reading language"><option value="zh">中文阅读 · 英文随手看</option><option value="both">中英题答对照</option><option value="en">英语训练</option></select></div><div class="article-head"><div class="article-kicker">'+l.course+' / '+l.id.toUpperCase()+' <span>'+labels[l.status]+'</span></div><h1>'+heading+'</h1><p class="article-subtitle" lang="en">'+esc(a.title.en)+'</p><p class="article-meta">阅读约 '+esc(a.minutes)+' 分钟 · 做题、补课另计</p><div class="article-lede">'+articlePair(a.lede_html,'Read the opening in English')+'</div></div><p class="english article-language-note">English mode provides the lesson recap, worked examples and exercises. It is not a full translation of the Chinese narrative.</p><details class="article-toc"><summary>本篇路线 / On this page</summary><ol>'+a.sections.map(s=>'<li><a data-article-anchor="article-'+s.id+'" href="?lesson='+l.id+'&section='+s.id+'">'+articleTitle(s.title)+(s.optional?' <small>选读</small>':'')+'</a></li>').join('')+'<li><a data-article-anchor="article-review" href="?lesson='+l.id+'&section=review">去复习 / Review</a></li></ol></details>'+sections+extraUnits+articleCards(l)+'<div class="article-finish"><label><input id="complete" type="checkbox" '+(done[l.id]?'checked':'')+'>我已独立做过变式，并尝试英文解释 / I tried the variation and an English explanation.</label><p class="small" id="save-status">这是保存在当前浏览器的自评，不是自动判分。</p></div>'+articleSources(l)+'<nav class="article-next" aria-label="推荐学习顺序">'+(i?'<a href="#'+seq[i-1].id+'">← '+esc(seq[i-1].title_zh)+'</a>':'<a href="#'+l.course+'">课程目录</a>')+(i<seq.length-1?'<a href="#'+seq[i+1].id+'">'+esc(seq[i+1].title_zh)+' →</a>':'')+'</nav></article>';
  $('#language').value=articleLanguage;
  applyArticleLanguage(articleLanguage);
  $('#language').onchange=e=>{articleLanguage=e.target.value;applyArticleLanguage(articleLanguage);};
  $('#complete').onchange=e=>{
    if(e.target.checked) done[l.id]={completed_at:new Date().toISOString()}; else delete done[l.id];
    try{localStorage.setItem('micro-course-lessons-v1',JSON.stringify(done));$('#save-status').textContent='已保存你的自评记录。';}catch(error){$('#save-status').textContent='此环境不能保存，请导出学习记录。';}route();
  };
  document.querySelectorAll('[data-article-anchor]').forEach(link=>link.onclick=e=>{e.preventDefault();revealArticleTarget(document.getElementById(link.dataset.articleAnchor));});
  math();
  document.querySelectorAll('[data-article-demo]').forEach(host=>window.mountArticleDemo(host,host.dataset.articleDemo));
};
