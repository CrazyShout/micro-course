'use strict';
const N=window.COURSE_NOTICES,byId=Object.fromEntries(N.entries.map(e=>[e.id,e]));
const $=s=>document.querySelector(s),esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
for(const [id,names] of Object.entries(N.categories))$('#notice-category').insertAdjacentHTML('beforeend','<option value="'+id+'">'+esc(names.join(' / '))+'</option>');
function render(){
 const course=$('#notice-course').value,category=$('#notice-category').value,q=$('#notice-search').value.trim().toLowerCase();
 const entries=N.entries.filter(e=>(course==='all'||e.course===course)&&(category==='all'||e.category===category)&&(!q||[e.id,e.title_zh,e.title_en,e.body_zh,e.body_en].join(' ').toLowerCase().includes(q)));
 document.body.dataset.language=$('#notice-language').value;
 $('#notice-count').textContent=entries.length+' 条 / entries · 整理于 / Updated '+N.updated;
 $('#notices').innerHTML=entries.map(e=>'<article class="panel notice" id="'+e.id+'"><span class="badge">'+esc(e.course)+'</span><span class="small">'+esc(N.categories[e.category].join(' / '))+'</span><h2><span class="zh">'+esc(e.title_zh)+'</span><span class="english">'+esc(e.title_en)+'</span></h2><p class="small">材料快照 / Material snapshot: '+esc(e.material_snapshot)+'</p><div class="zh">'+e.body_zh_html+'</div><div class="english">'+e.body_en_html+'</div><details><summary>资料出处 / Sources</summary><ul>'+e.sources.map(s=>'<li>'+(s.href?'<a href="'+esc(s.href)+'" target="_blank" rel="noopener">'+esc(s.name)+'</a>':esc(s.name))+' · '+esc(s.unit+' '+s.locator)+' · '+esc(s.provenance)+'</li>').join('')+'</ul></details><div class="notice-links"><a href="#'+e.id+'">此条链接 / Permalink</a>'+e.lesson_ids.map(id=>'<a href="index.html?lesson='+id+'">关联微课 / Lesson '+id.toUpperCase()+'</a>').join('')+'</div></article>').join('')||'<div class="panel board-empty">没有匹配信息 / No matching entries</div>';
 if(window.renderMathInElement)renderMathInElement($('#notices'),{delimiters:[{left:'\\(',right:'\\)',display:false}],throwOnError:false,strict:false});
}
function followAnchor(){const entry=byId[location.hash.slice(1)];if(entry){$('#notice-course').value=entry.course;$('#notice-category').value='all';$('#notice-search').value='';render();document.getElementById(entry.id).scrollIntoView({block:'start'});}}
const requested=new URLSearchParams(location.search).get('course');if(['CS5489','CS5222'].includes(requested))$('#notice-course').value=requested;
for(const id of ['notice-course','notice-category','notice-language'])$('#'+id).onchange=render;
$('#notice-search').oninput=render;window.addEventListener('hashchange',followAnchor);render();followAnchor();
