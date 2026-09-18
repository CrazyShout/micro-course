'use strict';
// A teaching relationship is a link, not a change to a card's identity or chapter.
const activityKinds={tutorial:'Tutorial · 配套练习',assignment:'Assignment · 综合应用',report:'Research report · 研究实践',class_check:'课堂回顾与检查'};
function curriculum(course){return D.curriculum?.courses[course];}
function unitURL(course,id){return '?course='+encodeURIComponent(course)+'&chapter='+encodeURIComponent(id);}
function activityURL(id,item){return '?activity='+encodeURIComponent(id)+(item?'&item='+encodeURIComponent(item):'');}
function unitLink(course,unit){return '<a href="'+unitURL(course,unit.id)+'">'+esc(unit.title.zh)+'</a>';}
function activityLink(activity){return '<a href="'+activityURL(activity.id)+'">'+esc(activity.title.zh)+'</a>';}
function teachingLessonLink(id){const l=L[id];return '<a href="?lesson='+id+'"><small>'+id.toUpperCase()+'</small> '+esc(l.article?.title.zh||l.title_zh)+'</a>';}
function activityLookup(id){for(const c of Object.values(D.curriculum?.courses||{})){const activity=c.activities.find(a=>a.id===id);if(activity)return {course:c.course,activity};}return null;}
function teachingSources(sources){return '<details class="article-sources"><summary>材料依据与范围 / Sources and scope</summary><ul>'+sources.map(s=>'<li><strong>'+esc(s.name)+'</strong> · '+esc(s.locator)+'<p>'+esc(s.note)+'</p></li>').join('')+'</ul></details>';}
function teachingContext(lid){
  const l=L[lid],c=curriculum(l.course);if(!c||l.status==='preview')return '';
  const activities=c.activities.filter(a=>a.lesson_ids.includes(lid)||a.items.some(item=>item.lesson_ids.includes(lid)));
  const primary=c.units.filter(u=>u.lessons.some(x=>x.id===lid));
  const parents=primary.length?primary:c.units.filter(u=>activities.some(a=>a.units.includes(u.id)));
  return '<div class="teaching-context"><span>所在课堂：</span>'+parents.map(u=>unitLink(l.course,u)).join(' · ')+(activities.length?'<details><summary>相关原题与任务 / Related activities</summary><ul>'+activities.map(a=>'<li>'+activityLink(a)+'</li>').join('')+'</ul></details>':'')+(!parents.length?'课程级方法与应用':'')+'</div>';
}
function teachingLessonList(lessons){return '<ol class="course-articles">'+lessons.map(item=>'<li>'+teachingLessonLink(item.id)+'<div class="article-index-note">'+articlePair(item.lead_html)+'</div></li>').join('')+'</ol>';}
function teachingActivityList(course,ids){const c=curriculum(course);return '<ul class="teaching-activities">'+ids.map(id=>{const a=c.activities.find(x=>x.id===id);return '<li><span class="activity-kind">'+activityKinds[a.kind]+'</span>'+activityLink(a)+'<p>'+esc(a.intro.zh)+'</p></li>';}).join('')+'</ul>';}
function teachingLanguageControls(){return '<label class="sr-only" for="language">阅读语言 / Reading language</label><select id="language" aria-label="阅读语言 / Reading language"><option value="zh">中文阅读 · 英文随手看</option><option value="both">中英对照</option><option value="en">English</option></select>';}
function finishTeachingPage(){
  document.body.dataset.view='curriculum';$('#nav-controls').open=false;
  if($('#language')){$('#language').value=articleLanguage;applyArticleLanguage(articleLanguage);$('#language').onchange=e=>{articleLanguage=e.target.value;applyArticleLanguage(articleLanguage);};}
  else applyArticleLanguage('zh');
  math();
}
function renderCurriculumOverview(course){
  const c=curriculum(course);document.body.dataset.view='overview';document.body.dataset.language='zh';document.title=course+' · 课堂学习路线';
  const historic=D.lessons.filter(l=>l.course===course&&l.status==='preview');
  $('#main').innerHTML='<section class="course-opening"><div class="eyebrow">'+esc(course)+' / COURSE PATHWAY</div><h1>'+esc(c.title.zh)+'</h1><p class="subtitle">'+esc(c.title.en)+'</p>'+articlePair(c.introduction_html)+'<p class="small">选择一讲，先读导读，再顺着知识微课与原题练习往前走。复习使用原 Markji 牌组。</p></section>'+c.units.map((u,i)=>'<section class="course-chapter teaching-overview-unit"><div class="eyebrow">'+String(i+1).padStart(2,'0')+' / '+esc(course)+'</div><h2>'+unitLink(course,u)+'</h2><div class="teaching-intro">'+articlePair(u.intro_html)+'</div><a class="unit-start" href="'+unitURL(course,u.id)+'">进入本讲：导读 → 微课 → 配套任务 → 回顾 →</a><div class="unit-contents"><span>知识微课</span><ul>'+u.lessons.map(item=>'<li>'+teachingLessonLink(item.id)+'</li>').join('')+'</ul>'+(u.activities.length?'<span>配套任务</span><ul>'+u.activities.map(id=>'<li>'+activityLink(c.activities.find(a=>a.id===id))+'</li>').join('')+'</ul>':'')+'</div></section>').join('')+(c.course_activities.length?'<section class="course-chapter"><h2>课程级综合实践</h2>'+teachingActivityList(course,c.course_activities)+'</section>':'')+(c.extension_lessons.length?'<section class="course-chapter"><h2>跨讲方法与表达</h2><ul>'+c.extension_lessons.map(id=>'<li>'+teachingLessonLink(id)+'</li>').join('')+'</ul></section>':'')+(historic.length?'<section class="course-chapter teaching-preview"><details><summary>Extra Resources · 往年预习（'+historic.length+' 节）</summary><p>这些材料尚未确认为当前教学安排；不混入已下载课堂的学习顺序。</p><ol class="course-articles">'+historic.map(l=>'<li>'+teachingLessonLink(l.id)+'</li>').join('')+'</ol></details></section>':'')+'<details class="course-details"><summary>课程信息、覆盖边界与使用说明</summary><p><a href="notices.html?course='+course+'">课程信息栏</a> · <a href="guide.html">使用指南</a></p>'+coverageHTML(course)+'</details>';
  math();
}
function renderTeachingUnit(course,uid){
  const c=curriculum(course),u=c?.units.find(x=>x.id===uid);if(!u){overview();return;}
  document.title=u.title.zh+' · '+course;
  $('#main').innerHTML='<article class="lesson-article teaching-unit"><div class="article-topline"><a href="#'+course+'">← '+course+' 课程路线</a>'+teachingLanguageControls()+'</div><div class="article-head"><div class="article-kicker">'+course+' / '+esc(uid.toUpperCase())+'</div><h1>'+esc(u.title.zh)+'</h1><p class="article-subtitle">'+esc(u.title.en)+'</p></div><section class="article-section teaching-unit-intro"><h2>'+articleTitle({zh:'这一讲，从什么问题开始？',en:'Where does this class begin?'})+'</h2>'+articlePair(u.intro_html)+'</section><section class="article-section"><h2>'+articleTitle({zh:'学完要能做什么',en:'What you should be able to do'})+'</h2><ul class="teaching-outcomes">'+u.outcomes_html.map(v=>'<li>'+articlePair(v)+'</li>').join('')+'</ul></section><section class="article-section"><h2>'+articleTitle({zh:'顺着问题，逐节学懂',en:'Follow the questions through the micro-lessons'})+'</h2>'+teachingLessonList(u.lessons)+'</section>'+(u.activities.length?'<section class="article-section"><h2>'+articleTitle({zh:'把这一讲用到原题与任务里',en:'Apply this class to its exercises and tasks'})+'</h2>'+teachingActivityList(course,u.activities)+'</section>':'')+'<section class="article-section"><h2>'+articleTitle({zh:'回到这一讲，把线索连起来',en:'Connect the class back together'})+'</h2>'+articlePair(u.review_html)+'<p class="zh">每学完一节，就可以用该节的首轮卡复习，不必等整讲全部结束。</p><div class="teaching-review-links">'+u.lessons.map(x=>'<a href="?lesson='+x.id+(L[x.id].article?'&section=review':'')+'">'+x.id.toUpperCase()+' · '+L[x.id].study_route.first_pass.length+' 张首轮卡</a>').join('')+'</div><p><a class="article-cta" href="'+esc(D.courses[course].markji_url)+'" target="_blank" rel="noopener">打开原 Markji 牌组 ↗</a></p><p class="small">卡号在各微课文末。网页不会自动选卡或改变复习排程。</p></section>'+(u.missing.length?'<details class="article-aside"><summary>当前材料的边界 / Available material</summary>'+u.missing_html.map(v=>articlePair(v)).join('')+'</details>':'')+teachingSources(u.sources)+'</article>';
  finishTeachingPage();
}
function activityCard(cid,seenMedia){
  const card=D.curriculum.card_previews[cid];
  const media=names=>names.map(name=>'<figure class="article-figure activity-figure"><a href="'+esc(card.course+'/media/'+name)+'" target="_blank" rel="noopener"><img src="'+esc(card.course+'/media/'+name)+'" alt="'+esc(cid+' · 题目配图 / Problem figure')+'" loading="lazy"></a><figcaption>题目配图 · '+esc(cid)+' · 点击放大 / Enlarge</figcaption></figure>').join('');
  return '<div class="activity-question" data-card-ref="'+esc(cid)+'"><div class="eyebrow">'+esc(cid)+'</div>'+articlePair({zh:card.question_zh_html,en:card.question_en_html},'English question')+media(card.front_media.filter(name=>{const key=card.course+'/'+name;if(seenMedia.has(key))return false;seenMedia.add(key);return true;}))+'<details class="article-answer"><summary>做完后看现有讲解 / Check the study explanation</summary>'+articlePair({zh:card.answer_zh_html,en:card.answer_en_html},'English explanation')+media(card.back_media)+'<p class="small"><a href="cards.html#'+cid+'">打开原卡及出处 / Open the original card</a></p></details></div>';
}
function renderTeachingActivity(id){
  const found=activityLookup(id);if(!found){overview();return;}
  const {course,activity:a}=found,c=curriculum(course);document.title=a.title.zh+' · '+course;
  $('#main').innerHTML='<article class="lesson-article teaching-activity"><div class="article-topline"><a href="#'+course+'">← '+course+' 课程路线</a>'+teachingLanguageControls()+'</div><div class="article-head"><div class="article-kicker">'+esc(activityKinds[a.kind])+'</div><h1>'+esc(a.title.zh)+'</h1><p class="article-subtitle">'+esc(a.title.en)+'</p><div class="activity-parents">'+(a.units.length?a.units.map(uid=>unitLink(course,c.units.find(u=>u.id===uid))).join(' · '):'课程级任务 / Course-wide task')+'</div>'+articlePair(a.intro_html)+'</div><details class="article-toc"><summary>按题号／任务进入 / Tasks in this activity</summary><ol>'+a.items.map(item=>'<li><a href="'+activityURL(a.id,item.id)+'">'+articleTitle(item.title)+'</a></li>').join('')+'</ol></details>'+a.items.map(item=>{const seenMedia=new Set();return '<section id="activity-item-'+item.id+'" class="article-section activity-item" tabindex="-1"><h2>'+articleTitle(item.title)+'</h2>'+articlePair(item.task_html)+'<div class="activity-concept-links"><span>会用到 / Builds on: </span>'+item.lesson_ids.map(teachingLessonLink).join(' · ')+'</div>'+item.card_ids.map(cid=>activityCard(cid,seenMedia)).join('')+'<h3>'+articleTitle({zh:'从哪里着手，为什么这样做',en:'How to approach the task, and why'})+'</h3>'+articlePair(item.approach_html)+'<details class="article-aside"><summary>做完怎样检查 / Check your work</summary>'+articlePair(item.check_html)+'</details><details class="article-aside"><summary>容易走错的一步 / A common pitfall</summary>'+articlePair(item.pitfall_html)+'</details>'+teachingSources(item.sources)+'</section>';}).join('')+'<section class="article-section"><h2>'+articleTitle({zh:'回到课堂与复习',en:'Return to the class and review'})+'</h2><div class="teaching-review-links">'+a.lesson_ids.map(teachingLessonLink).join('')+'</div><p><a class="article-cta" href="'+esc(D.courses[course].markji_url)+'" target="_blank" rel="noopener">打开原 Markji 牌组 ↗</a></p><p class="small">按上面的原卡号复习；代码、实验和长题需亲手完成。提交要求与日期见 <a href="notices.html?course='+course+'">课程信息栏</a>。</p></section>'+teachingSources(a.sources)+'</article>';
  finishTeachingPage();
  const item=new URLSearchParams(location.search).get('item');if(item)revealArticleTarget(document.getElementById('activity-item-'+item));
}
function activityMatches(a,q){return !q||[a.title.zh,a.title.en,a.intro.zh,a.intro.en,...a.lesson_ids,...a.items.flatMap(i=>[i.title.zh,i.title.en,i.task.zh,i.task.en,...i.card_ids,...i.lesson_ids])].join(' ').toLowerCase().includes(q);}
function curriculumRouteHTML(course,found){
  const c=curriculum(course),allowed=new Set(found.map(l=>l.id)),q=$('#search').value.trim().toLowerCase(),p=new URLSearchParams(location.search),activeId=location.hash.slice(1)||p.get('lesson'),emitted=new Set();
  const lesson=id=>{emitted.add(id);const l=L[id];return '<a href="?lesson='+id+'" '+(activeId===id?'class="active" aria-current="page"':'')+'><span>'+esc(l.article?.title.zh||l.title_zh)+'</span><div class="route-meta">'+id.toUpperCase()+(done[id]?' · ✓':'')+'</div></a>';};
  let out='';
  if($('#scope').value!=='preview'){
    for(const u of c.units){
      const ls=u.lessons.filter(x=>allowed.has(x.id));
      const as=u.activities.map(id=>c.activities.find(a=>a.id===id)).filter(a=>activityMatches(a,q));
      if(ls.length||as.length||!q)out+='<div class="chapter-name">'+unitLink(course,u)+'</div>'+ls.map(x=>lesson(x.id)).join('')+as.map(a=>'<a class="route-activity" href="'+activityURL(a.id)+'">'+esc(a.title.zh)+'<div class="route-meta">'+esc(activityKinds[a.kind])+'</div></a>').join('');
    }
    const standalone=c.course_activities.map(id=>c.activities.find(a=>a.id===id)).filter(a=>activityMatches(a,q));
    if(standalone.length)out+='<div class="chapter-name">课程级综合实践</div>'+standalone.map(a=>'<a href="'+activityURL(a.id)+'">'+esc(a.title.zh)+'</a>').join('');
    const extra=c.extension_lessons.filter(id=>allowed.has(id));if(extra.length)out+='<div class="chapter-name">跨讲方法与表达</div>'+extra.map(lesson).join('');
  }
  if(q){const matching=found.filter(l=>l.status!=='preview'&&!emitted.has(l.id));if(matching.length)out+='<div class="chapter-name">匹配的配套微课</div>'+matching.map(l=>lesson(l.id)).join('');}
  const preview=found.filter(l=>l.status==='preview');if(preview.length)out+='<details class="route-preview" '+($('#scope').value==='preview'||q?'open':'')+'><summary>Extra Resources · 往年预习</summary>'+preview.map(l=>lesson(l.id)).join('')+'</details>';
  return out;
}

function alignTeachingNavigation(l){
  const c=curriculum(l.course);if(!c||l.status==='preview')return;
  const nav=document.querySelector('#main .lesson-nav,#main .article-next');if(!nav)return;
  const u=c.units.find(u=>u.lessons.some(x=>x.id===l.id));
  if(u){const i=u.lessons.findIndex(x=>x.id===l.id),previous=i?L[u.lessons[i-1].id]:null,next=i+1<u.lessons.length?L[u.lessons[i+1].id]:null;
    nav.innerHTML=(previous?'<a href="?lesson='+previous.id+'">← '+esc(previous.article?.title.zh||previous.title_zh)+'</a>':'<a href="'+unitURL(l.course,u.id)+'">← 回到本讲导读</a>')+(next?'<a href="?lesson='+next.id+'">'+esc(next.article?.title.zh||next.title_zh)+' →</a>':'<a href="'+unitURL(l.course,u.id)+'">本讲回顾与配套任务 →</a>');
  }else{const activities=c.activities.filter(a=>a.lesson_ids.includes(l.id)||a.items.some(x=>x.lesson_ids.includes(l.id)));if(activities.length)nav.innerHTML=activities.map(a=>'<a href="'+activityURL(a.id)+'">回到 '+esc(a.title.zh)+' →</a>').join('');}
}
