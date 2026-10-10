"use client";

import { useEffect } from "react";

export default function Page() {
  useEffect(() => {
    const $=(s,r=document)=>r.querySelector(s),esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
    const DEMO='<span class="demo">DEMO DATA — NOT NASA MEASUREMENTS</span>';
    // ---- synthetic demo data (seeded, illustrative only) ----
    function rng(s){return()=>(s=(s*16807)%2147483647)/2147483647}
    function mk(seed,chs,ign){const r=rng(seed),t=[...Array(120).keys()],d={t};
     const base={temp:[22,.15],o2:[21,.05],co2:[.04,.002],co:[2,.1],air:[20,.4]};
     chs.forEach(c=>{const[b,n]=base[c];d[c]=t.map(i=>{let v=b+(r()-.5)*n*4;if(i>ign){const k=Math.min(1,(i-ign)/30);
      if(c=='temp')v+=14*k;if(c=='co2')v+=.12*k;if(c=='co')v+=40*k;if(c=='o2')v-=.8*k}return+v.toFixed(3)})});
     d.units={temp:'°C',o2:'%',co2:'% vol',co:'ppm',air:'cm/s'};return d}
    const DEMOX=[
     {id:'DEMO-A',title:'Demo A — thin fuel, forced flow (synthetic)',material:'Illustrative thin cellulose-like sample',cond:'Synthetic: 21% O₂, 20 cm/s flow',type:'Flame spread',data:mk(7,['temp','o2','co2','co','air'],60),ev:['saf1','saf6']},
     {id:'DEMO-B',title:'Demo B — thick fuel, low flow (synthetic)',material:'Illustrative PMMA-like sample',cond:'Synthetic: 21% O₂, 5 cm/s flow',type:'Flame spread',data:mk(11,['temp','o2','air'],75),ev:['saf45','pla']}];
    const LABEL={temp:'Temperature',o2:'Oxygen',co2:'Carbon dioxide',co:'Carbon monoxide',air:'Airflow'};
    // ---- real-source catalog (links only; no data loaded) ----
    const N='https://ntrs.nasa.gov/citations/';
    const CAT=[
     {id:'saf',title:'Saffire (Spacecraft Fire Experiment) series',org:'NASA Glenn / SFS Demo project',type:'Large-scale spacecraft fire',mat:'Various (see papers)',mod:['Publication','Sensor (per papers)','Video (per papers)'],status:'Publications verified; raw-data access NOT verified here',links:[['Saffire overview paper (NTRS 20170001636)',N+'20170001636']]},
     {id:'bass',title:'BASS-II (Burning and Suppression of Solids-II)',org:'NASA Physical Sciences Informatics',type:'Solid-fuel flammability',mat:'See PSI record',mod:['Repository (verify files)'],status:'Not verified here: check PSI for public vs. restricted files',links:[['NASA PSI search',"https://psi.nasa.gov/"]]},
     {id:'same',title:'SAME (Smoke Aerosol Measurement Experiment)',org:'NASA / NIST',type:'Smoke & detectors',mat:'Smoke aerosols',mod:['Publication'],status:'Not verified here: search NTRS/NIST for SAME reports',links:[['NASA NTRS',"https://ntrs.nasa.gov/"],['NIST publications',"https://www.nist.gov/publications"]]}];
    const EV=[
     {id:'saf1',t:'Results of Large-Scale Spacecraft Flammability Tests',o:'NASA Glenn Research Center',u:N+'20170008805'.replace(/^/,''),url:'https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20170008805.pdf',cat:'Flame behavior',f:'Large-scale fire in orbit behaved qualitatively differently from Earth upward spread; forced flow, and sample scale, mattered.',s:'Small-scale ground/short tests may not scale linearly to spacecraft fires.',n:'Does not give a universal flame-spread law or cover all materials.'},
     {id:'saf45',t:'Fire Safety Implications of Preliminary Results from Saffire IV and V',o:'NASA Glenn / JSC / ESTEC',url:N+'20210011521',cat:'Flame behavior',f:'PMMA, cotton and cotton/fiberglass samples burned in Cygnus; fires measurably affected vehicle pressure, temperature and CO₂.',s:'Fires leave a measurable cabin signature in several channels.',n:'Preliminary results; not a detector performance evaluation.'},
     {id:'saf6',t:'Preliminary Results from the Saffire VI Experiment',o:'NASA Glenn Research Center',url:N+'20240002981',cat:'Material flammability',f:'Temperature and pressure rise were less significant than CO and CO₂ increase in the studied tests.',s:'Gas channels may be informative alongside temperature.',n:'Preliminary; specific to the tested vehicle, volume and samples.'},
     {id:'saf1o',t:'Saffire: A Novel Approach to Study of Spacecraft Fire Safety Using Un-Manned Spacecraft',o:'NASA Glenn Research Center',url:N+'20180005168',cat:'Experimental limitations',f:'Tests were run on an unoccupied Cygnus after leaving ISS, commanded from the ground.',s:'Explains why such tests are feasible and their setup.',n:'Does not show results apply to crewed cabins unchanged.'},
     {id:'pla',t:'Model Development of Large-Scale Spacecraft Fires During the Saffire-IV Experiments',o:'J. Brooker, J. Niehaus et al., NASA Glenn',url:N+'20220002714',cat:'Experimental limitations',f:'A PyroSim model was compared with Saffire-IV gas measurements and sources of error were discussed.',s:'Models can be checked against flight data.',n:'A simulation is not an observed outcome.'},
     {id:'sfs',t:'The Spacecraft Fire Experiment (Saffire) — Objectives, Development and Status',o:'NASA Glenn Research Center',url:N+'20170001636',cat:'Experimental limitations',f:'Describes Saffire-I to III objectives: material flammability at realistic spacecraft length scales.',s:'Motivation and design of the experiments.',n:'Not results; planning-stage paper.'}];
    // ---- charts ----
    function chart(cv,x,ys,opt={}){const c=cv.getContext('2d'),W=cv.width=cv.clientWidth*2,H=cv.height=(opt.h||150)*2;c.clearRect(0,0,W,H);
     const v=ys.filter(a=>a!=null&&!isNaN(a));if(!v.length){c.fillStyle='#98a6c3';c.font='24px sans-serif';c.fillText('No data',20,40);return}
     let lo=Math.min(...v),hi=Math.max(...v);if(hi==lo){hi+=1;lo-=1}const X=i=>30+i/(ys.length-1||1)*(W-50),Y=a=>H-24-(a-lo)/(hi-lo)*(H-44);
     c.strokeStyle='#223256';c.strokeRect(30,10,W-50,H-34);c.fillStyle='#98a6c3';c.font='20px sans-serif';c.fillText(hi.toFixed(2),2,22);c.fillText(lo.toFixed(2),2,H-26);
     c.strokeStyle='#4fd1e8';c.lineWidth=2;c.beginPath();let pen=0;ys.forEach((a,i)=>{if(a==null||isNaN(a)){pen=0;return}pen?c.lineTo(X(i),Y(a)):c.moveTo(X(i),Y(a));pen=1});c.stroke();
     (opt.mark||[]).forEach(i=>{c.fillStyle='#f5b041';c.beginPath();c.arc(X(i),Y(ys[i]),6,0,7);c.fill()})}
    function robust(a,w,th){const ev=[];a.forEach((v,i)=>{if(v==null||isNaN(v))return;const win=a.slice(Math.max(0,i-w),i).filter(x=>x!=null&&!isNaN(x));if(win.length<5)return;
     const s=[...win].sort((p,q)=>p-q),med=s[s.length>>1],dev=win.map(x=>Math.abs(x-med)).sort((p,q)=>p-q),mad=dev[dev.length>>1]||1e-9,z=.6745*(v-med)/mad;if(Math.abs(z)>th)ev.push({i,z:+z.toFixed(1)})});return ev}
    const RULE=(w,th)=>`Rolling robust z-score: z=0.6745·(x−median)/MAD over the previous ${w} samples; flagged when |z|>${th}. Descriptive rule, not a validated fire detector.`;
    function stats(a){const v=a.filter(x=>x!=null&&!isNaN(x));if(!v.length)return null;const m=v.reduce((p,q)=>p+q,0)/v.length;return{n:v.length,miss:a.length-v.length,min:Math.min(...v),max:Math.max(...v),mean:m,sd:Math.sqrt(v.reduce((p,q)=>p+(q-m)**2,0)/v.length)}}
    const f=(n,d=2)=>Number(n).toFixed(d);
    function dl(name,txt,type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([txt],{type}));a.download=name;a.click()}
    let sel=0,cmpA=0,cmpB=1,tour=true,U=null;const cleanups=[];
    function evCard(e){return`<div class="c"><span class="tag">${e.cat}</span><h3>${esc(e.t)}</h3><div class="mu">${esc(e.o)} · year: see source</div><p>${esc(e.f)}</p><p class="ok"><b>Supports:</b> ${esc(e.s)}</p><p class="warn"><b>Does not establish:</b> ${esc(e.n)}</p><a href="${e.url}" target="_blank" rel="noopener">Source publication ↗</a></div>`}
    // ---- pages ----
    const P={};
    P['/']=()=>`<section class="hero"><h1>FIREWISE-X</h1><div class="mu">Evidence-Grounded AI for Microgravity Fire Safety</div><h2 style="font-size:1.6rem">Understand the Flame. Follow the Evidence.</h2>
    <p>Without buoyancy, hot gases do not rise, so flames in freefall are often rounder, dimmer and driven by slow forced flow rather than convection. NASA's Saffire tests found large-scale fire behaviour in orbit differed qualitatively from Earth.</p>
    <div class="row"><a class="btn" href="#/mc">Launch Mission Control</a><a class="btn" style="background:transparent;color:var(--tx);border:1px solid var(--bd)" href="#/exp">Explore Experiments</a></div></section>
    <div class="g"><div class="c"><h3>1 · Explore NASA Experiments</h3><p class="mu">Catalog of Saffire, BASS-II and SAME with source links.</p></div><div class="c"><h3>2 · Analyze Flame Behavior</h3><p class="mu">Real brightness-threshold analysis of images/videos you upload.</p></div><div class="c"><h3>3 · Discover Evidence-Backed Insights</h3><p class="mu">Searchable cards with what each finding does and does not establish.</p></div></div>
    <div class="g" style="margin-top:12px"><div class="c"><h2>Scientific motivation</h2><p class="mu">Fire is a catastrophic spacecraft hazard and 1-g flammability intuition may not transfer. Tools that make microgravity combustion data legible can help researchers ask better questions.</p></div>
    <div class="c"><h2>Limitations</h2><p class="mu">Demo experiments are synthetic. No NASA raw dataset is loaded; BASS-II/SAME file access is unverified. Anomaly flags are statistical, not predictions. Pixel area ≠ physical area. No NASA endorsement.</p></div></div>`;
    function opts(v){return DEMOX.map((e,i)=>`<option value="${i}" ${i==v?'selected':''}>${e.id}</option>`).join('')}
    P['/mc']=()=>{const e=DEMOX[sel],d=e.data,chs=Object.keys(LABEL);
     return`<div class="row"><h1 style="margin:0">Mission Control</h1><select id="s" aria-label="Experiment">${opts(sel)}</select><button class="s" onclick="sel=0;go()">Reset demo</button><button class="s" onclick="tour=!tour;go()">How to use</button><button onclick="exportCSV()">Export CSV</button><button onclick="window.print()">Print report</button></div>${DEMO}
    ${tour?'<div class="c" style="margin:8px 0">1) Pick an experiment · 2) Read sensor charts (amber dots = flagged) · 3) Check the interpretation panel · 4) Open evidence · 5) <a href="#/cmp">Compare</a> · 6) Export. Unavailable channels say so rather than inventing data.</div>':''}
    <div class="g"><div class="c"><h2>${esc(e.title)}</h2><table><tr><td>ID</td><td>${e.id}</td></tr><tr><td>Material</td><td>${e.material}</td></tr><tr><td>Conditions</td><td>${e.cond}</td></tr><tr><td>Source</td><td>Generated in-browser (seeded synthetic)</td></tr></table>
    <p class="mu">Timeline: samples 0–119 (arbitrary units). Synthetic ignition-like change at sample ${e===DEMOX[0]?60:75}.</p></div>
    <div class="c" id="risk"></div></div><div class="g" style="margin-top:12px" id="ch">${chs.map(c=>`<div class="c"><h3>${LABEL[c]} ${d[c]?'('+d.units[c]+')':''}</h3>${d[c]?`<canvas id="c_${c}"></canvas>`:'<p class="na">Not available in this experiment</p>'}</div>`).join('')}</div>
    <h2 style="margin-top:16px">Related evidence</h2><div class="g">${e.ev.map(i=>evCard(EV.find(x=>x.id==i))).join('')}</div>`};
    function mcInit(){const e=DEMOX[sel],d=e.data;$('#s').onchange=ev=>{sel=+ev.target.value;go()};let hits=[];
     Object.keys(LABEL).forEach(c=>{if(!d[c])return;const v=robust(d[c],15,6);v.length&&hits.push([c,v]);chart($('#c_'+c),d.t,d[c],{mark:v.map(x=>x.i)})});
     const miss=Object.keys(LABEL).filter(c=>!d[c]).map(c=>LABEL[c]);
     $('#risk').innerHTML=`<h2>Evidence-based interpretation</h2><p><b class="${hits.length?'warn':'ok'}">${hits.length?'Significant change observed in '+hits.length+' channel(s)':'Normal relative to this experiment baseline'}</b></p>
     <p class="mu"><b>Triggers:</b> ${hits.map(h=>LABEL[h[0]]+' (first flag @ sample '+h[1][0].i+', z='+h[1][0].z+')').join('; ')||'none'}<br><b>Rule:</b> ${RULE(15,6)}<br><b>Data quality:</b> synthetic data; ${miss.length?'missing channels: '+miss.join(', '):'all channels present'}.<br><b>Uncertainty:</b> no calibrated probability is computed; strength is qualitative — multi-channel agreement is stronger than a single-channel flag.<br><b>Next step:</b> ${hits.length?'inspect the video in <a href="#/flame">Flame Studio</a> and compare with <a href="#/cmp">another experiment</a>.':'try a lower threshold in <a href="#/sensor">Sensors</a>.'}</p>`}

    function exportCSV(){const d=DEMOX[window.sel].data,k=['t',...Object.keys(LABEL).filter(c=>d[c])];dl(DEMOX[window.sel].id+'.csv','# DEMO DATA - NOT NASA MEASUREMENTS\n'+k.join(',')+'\n'+d.t.map((_,i)=>k.map(c=>d[c][i]).join(',')).join('\n'),'text/csv')}
    P['/exp']=()=>`<h1>Experiment Explorer</h1><div class="row"><input type="search" id="q" placeholder="Search name, material, keyword" aria-label="Search"><select id="ty"><option value="">All types</option>${[...new Set([...CAT,...DEMOX].map(x=>x.type))].map(t=>`<option>${t}</option>`).join('')}</select><select id="mo"><option value="">All modalities</option><option>Sensor</option><option>Video</option><option>Publication</option></select><label class="mu"><input type="checkbox" id="rl"> Real sources only</label></div><div class="g" id="list"></div>`;
    function expInit(){const draw=()=>{const q=$('#q').value.toLowerCase(),t=$('#ty').value,m=$('#mo').value,r=$('#rl').checked;
     const L=[...CAT.map(x=>({...x,real:1})),...DEMOX.map(x=>({id:x.id,title:x.title,org:'Synthetic',type:x.type,mat:x.material,mod:['Sensor','Video (synthetic frame)'],status:'Demo only',links:[],real:0}))].filter(x=>(!r||x.real)&&(!t||x.type==t)&&(!m||x.mod.join().includes(m))&&(x.title+x.mat+x.type+x.org).toLowerCase().includes(q));
     $('#list').innerHTML=L.length?L.map(x=>`<div class="c">${x.real?'':DEMO}<h3>${esc(x.title)}</h3><div class="mu">${esc(x.org)} · ${esc(x.mat)}</div><p>${x.mod.map(y=>`<span class="tag">${y}</span>`).join('')}</p><p class="${x.real?'warn':'mu'}">${x.status}</p>${x.links.map(l=>`<div><a href="${l[1]}" target="_blank" rel="noopener">${l[0]} ↗</a> <span class="mu">(source page, not raw data)</span></div>`).join('')}${x.real?'':`<button onclick="sel=${DEMOX.findIndex(d=>d.id==x.id)};go();location.hash='#/mc'">Open in Mission Control</button>`}</div>`).join(''):'<div class="c na">No experiments match your filters.</div>'};
     ['q','ty','mo','rl'].forEach(i=>$('#'+i).oninput=draw);draw()}
    P['/flame']=()=>`<h1>Flame Analysis Studio</h1><div class="c"><p class="mu"><b>Method:</b> luminance threshold segmentation on the current frame (Rec.709 luma). Flame = pixels brighter than the threshold; largest values from bounding box, edge-pixel count and mean position. <b>Limits:</b> brightness, camera angle, occlusion, frame rate and segmentation quality affect results; pixel area is not physical area unless scale is calibrated. This is classical image processing, not a trained AI model.</p>
    <div class="row"><input type="file" id="fl" accept="image/*,video/*" aria-label="Upload image or video"><button class="s" id="dm">Load synthetic demo frame</button><label>Threshold <input type="range" id="th" min="30" max="250" value="150"> <span id="tv">150</span></label></div><div id="msg" class="mu">Upload an image/video or load the synthetic frame.</div>
    <video id="vd" controls playsinline style="max-width:100%;display:none"></video><canvas id="cv" style="max-width:520px"></canvas><div class="row"><button id="sm" class="s" style="display:none">Sample 20 frames → area vs time</button></div><div id="out"></div><canvas id="ac" style="display:none"></canvas></div>`;
    function flameInit(){const cv=$('#cv'),x=cv.getContext('2d',{willReadFrequently:true}),vd=$('#vd');let src=null,isDemo=0;
     const draw=()=>{if(!src)return;const w=src.videoWidth||src.width,h=src.videoHeight||src.height;if(!w)return;const s=Math.min(1,480/w);cv.width=w*s|0;cv.height=h*s|0;x.drawImage(src,0,0,cv.width,cv.height);analyze()};
     function seg(){const im=x.getImageData(0,0,cv.width,cv.height),t=+$('#th').value,W=cv.width,m=new Uint8Array(W*cv.height);let n=0,sx=0,sy=0,x0=1e9,x1=-1,y0=1e9,y1=-1;
      for(let i=0;i<m.length;i++){const L=.2126*im.data[i*4]+.7152*im.data[i*4+1]+.0722*im.data[i*4+2];if(L>t){m[i]=1;n++;const px=i%W,py=i/W|0;sx+=px;sy+=py;x0=Math.min(x0,px);x1=Math.max(x1,px);y0=Math.min(y0,py);y1=Math.max(y1,py)}}
      let per=0;for(let i=0;i<m.length;i++)if(m[i]){const px=i%W;if(!m[i-1]||!m[i+1]||!m[i-W]||!m[i+W]||px==0||px==W-1)per++}
      for(let i=0;i<m.length;i++)if(m[i]){im.data[i*4]=245;im.data[i*4+1]=176;im.data[i*4+2]=65}
      return{im,n,per,cx:sx/n,cy:sy/n,len:y1-y0+1,wid:x1-x0+1}}
     function analyze(){const r=seg();if(!r.n){$('#out').innerHTML='<p class="na">No pixels above threshold — nothing to measure. Lower the threshold.</p>';return}x.putImageData(r.im,0,0);
      $('#out').innerHTML=`${isDemo?DEMO:''}<table><tr><th>Feature (pixels, uncalibrated)</th><th>Value</th></tr><tr><td>Area</td><td>${r.n} px²</td></tr><tr><td>Bounding length × width</td><td>${r.len} × ${r.wid} px</td></tr><tr><td>Edge-pixel perimeter</td><td>${r.per} px</td></tr><tr><td>Centroid</td><td>(${f(r.cx,1)}, ${f(r.cy,1)})</td></tr></table>`}
     $('#th').oninput=e=>{$('#tv').textContent=e.target.value;draw()};
     $('#dm').onclick=()=>{const c=document.createElement('canvas');c.width=480;c.height=320;const g=c.getContext('2d');g.fillStyle='#050a14';g.fillRect(0,0,480,320);const gr=g.createRadialGradient(240,170,5,240,170,70);gr.addColorStop(0,'#fff');gr.addColorStop(.5,'#9fd');gr.addColorStop(1,'#0000');g.fillStyle=gr;g.beginPath();g.arc(240,170,70,0,7);g.fill();src=c;isDemo=1;vd.style.display='none';$('#sm').style.display='none';$('#msg').innerHTML='Synthetic frame (a procedurally drawn sphere-like glow, not a NASA image).';draw()};
     $('#fl').onchange=e=>{const fl=e.target.files[0];if(!fl)return;isDemo=0;if(fl.size>200e6){$('#msg').innerHTML='<span class="warn">File too large (>200 MB).</span>';return}const u=URL.createObjectURL(fl);
      if(fl.type.startsWith('image/')){const im=new Image();im.onload=()=>{src=im;vd.style.display='none';$('#sm').style.display='none';$('#msg').textContent='Image loaded.';draw()};im.onerror=()=>$('#msg').innerHTML='<span class="warn">Could not decode image.</span>';im.src=u}
      else if(fl.type.startsWith('video/')){vd.style.display='block';vd.src=u;src=vd;vd.onloadeddata=()=>{$('#msg').textContent='Video loaded — pause/scrub, analysis follows the current frame.';$('#sm').style.display='';draw()};['seeked','pause','timeupdate'].forEach(v=>vd['on'+v]=draw);vd.onerror=()=>$('#msg').innerHTML='<span class="warn">Video format not supported by this browser.</span>'}
      else $('#msg').innerHTML='<span class="warn">Unsupported file type. Use an image or video.</span>'};
     $('#sm').onclick=async()=>{const D=vd.duration,a=[];for(let i=0;i<20;i++){vd.currentTime=D*i/19;await new Promise(r=>vd.onseeked=r);draw();a.push(seg().n)}const ac=$('#ac');ac.style.display='block';chart(ac,0,a);$('#msg').textContent='Area (px²) vs. time over 20 evenly spaced frames; same threshold throughout.'}}
    P['/sensor']=()=>`<h1>Sensor Analytics</h1><div class="c"><div class="row"><input type="file" id="cf" accept=".csv,.json" aria-label="Upload CSV or JSON"><button class="s" id="sd">Load sample CSV</button></div><div id="sm2" class="mu">CSV needs a header row; first column is time/index. JSON: array of row objects. Missing values stay missing (no interpolation).</div><div id="sp"></div></div>`;
    function parse(t,name){if(name.endsWith('.json')){const j=JSON.parse(t);if(!Array.isArray(j)||!j.length||typeof j[0]!='object')throw Error('JSON must be a non-empty array of objects');const h=Object.keys(j[0]);return{h,rows:j.map(r=>h.map(k=>r[k]))}}
     const L=t.split(/\r?\n/).filter(l=>l.trim()&&!l.startsWith('#'));if(L.length<10)throw Error('Need a header and at least 9 data rows');return{h:L[0].split(',').map(s=>s.trim()),rows:L.slice(1).map(l=>l.split(','))}}
    function sensorShow(D,demo){const h=D.h,cols=h.slice(1).filter((_,j)=>D.rows.some(r=>r[j+1]!==''&&!isNaN(parseFloat(r[j+1]))));if(!cols.length){$('#sp').innerHTML='<p class="warn">No numeric columns found.</p>';return}
     $('#sp').innerHTML=`${demo?DEMO:''}<p class="mu">Columns: ${h.map(esc).join(', ')} · rows: ${D.rows.length}</p><div class="row"><select id="cc">${cols.map(c=>`<option>${esc(c)}</option>`).join('')}</select><label>Threshold |z|> <input type="range" id="zt" min="2" max="12" step=".5" value="6"> <b id="zv">6</b></label></div><canvas id="sc"></canvas><div id="si"></div>`;
     const run=()=>{const j=h.indexOf($('#cc').value),a=D.rows.map(r=>{const v=r[j];return v===''||v==null||isNaN(+v)?null:+v}),th=+$('#zt').value;$('#zv').textContent=th;const ev=robust(a,15,th),s=stats(a);chart($('#sc'),0,a,{mark:ev.map(e=>e.i)});
      $('#si').innerHTML=`<table><tr><td>n / missing</td><td>${s.n} / ${s.miss}${s.miss?' <span class="warn">⚠ missing values left as gaps</span>':''}</td></tr><tr><td>min / max</td><td>${f(s.min)} / ${f(s.max)}</td></tr><tr><td>mean / sd</td><td>${f(s.mean)} / ${f(s.sd)}</td></tr></table><p class="mu">${RULE(15,th)}</p>${ev.length?`<div class="wrap"><table><tr><th>Row</th><th>Value</th><th>z</th><th>Triggered rule</th></tr>${ev.slice(0,30).map(e=>`<tr><td>${e.i}</td><td>${a[e.i]}</td><td>${e.z}</td><td>|z|>${th}</td></tr>`).join('')}</table></div>`:'<p class="ok">No events at this threshold.</p>'}`};
     $('#cc').onchange=$('#zt').oninput=run;run()}
    function sensorInit(){$('#sd').onclick=()=>{const d=DEMOX[0].data,h=['t','temp','o2','co2','co','air'];sensorShow({h,rows:d.t.map((_,i)=>h.map(c=>d[c][i]))},1)};
     $('#cf').onchange=e=>{const fl=e.target.files[0];if(!fl)return;const r=new FileReader();r.onload=()=>{try{sensorShow(parse(r.result,fl.name.toLowerCase()),0);$('#sm2').textContent='Loaded '+fl.name+' (user data; not verified by this app).'}catch(er){$('#sp').innerHTML='<p class="warn">Could not read file: '+esc(er.message)+'</p>'}};r.onerror=()=>$('#sp').innerHTML='<p class="warn">File read error.</p>';r.readAsText(fl)}}
    P['/evid']=()=>`<h1>Evidence Engine</h1><p class="mu">Searchable catalog of NASA NTRS records I checked. Summaries are paraphrased from the record abstracts; no generative AI is used. Open the source for authoritative detail.</p><div class="row"><input type="search" id="eq" placeholder="Search evidence" aria-label="Search evidence"><select id="ec"><option value="">All categories</option>${[...new Set(EV.map(e=>e.cat))].map(c=>`<option>${c}</option>`).join('')}</select></div><div class="g" id="el"></div>`;
    function evidInit(){const d=()=>{const q=$('#eq').value.toLowerCase(),c=$('#ec').value,L=EV.filter(e=>(!c||e.cat==c)&&(e.t+e.f+e.s+e.n).toLowerCase().includes(q));$('#el').innerHTML=L.length?L.map(evCard).join(''):'<div class="c na">No evidence cards match. The catalog is small; absence here is not absence of evidence.</div>'};$('#eq').oninput=$('#ec').oninput=d;d()}
    P['/cmp']=()=>{const A=DEMOX[window.cmpA],B=DEMOX[window.cmpB],row=(l,a,b)=>`<tr><td>${l}</td><td>${a}</td><td>${b}</td></tr>`,st=(e,c)=>e.data[c]?`mean ${f(stats(e.data[c]).mean)} ${e.data.units[c]}`:'<span class="na">Not available</span>';
     return`<h1>Compare Experiments</h1>${DEMO}<div class="row">A <select id="a">${opts(window.cmpA)}</select> B <select id="b">${opts(window.cmpB)}</select></div>${A==B?'<p class="warn">Select two different experiments.</p>':''}<div class="c wrap"><table><tr><th></th><th>${A.id}</th><th>${B.id}</th></tr>${row('Material',A.material,B.material)}${row('Conditions <span class="warn">(differ — not equivalent)</span>',A.cond,B.cond)}${Object.keys(LABEL).map(c=>row(LABEL[c],st(A,c),st(B,c))).join('')}${row('Flame-area trend','<span class="na">Not compared (no shared real video)</span>','<span class="na">Not compared</span>')}${row('Related findings',A.ev.length+' evidence cards',B.ev.length+' evidence cards')}</table><p class="mu">Means are over synthetic samples with different baselines; channels are compared only where both exist.</p></div>`};
    const INIT={'/mc':mcInit,'/exp':expInit,'/flame':flameInit,'/sensor':sensorInit,'/evid':evidInit,'/cmp':()=>{$('#a').onchange=e=>{window.cmpA=+e.target.value;go()};$('#b').onchange=e=>{window.cmpB=+e.target.value;go()}}};
    function go(){const p=location.hash.slice(1)||'/',pg=P[p]?p:'/';document.querySelectorAll('nav a').forEach(a=>a.classList.toggle('on',a.getAttribute('href')=='#'+pg));
     try{$('#app').innerHTML=P[pg]();(INIT[pg]||(()=>{}))()}catch(e){$('#app').innerHTML='<div class="c warn">Something went wrong: '+esc(e.message)+'</div>'}}
    
    // Make global for inline handlers
    window.sel = sel; window.go = go; window.cmpA = cmpA; window.cmpB = cmpB; window.tour = tour; window.exportCSV = exportCSV; window.P = P; window.INIT = INIT; window.DEMOX = DEMOX; window.chart = chart; window.f = f; window.stats = stats; window.RULE = RULE; window.robust = robust; window.LABEL = LABEL; window.$ = $; window.esc = esc; window.DEMO = DEMO; window.EV = EV; window.CAT = CAT; window.dl = dl; window.evCard = evCard; window.opts = opts; window.parse = parse; window.sensorShow = sensorShow;

    const onHashChange = () => { window.scrollTo(0,0); go(); };
    const onResize = () => { if(location.hash=='#/mc') go(); };
    addEventListener('hashchange', onHashChange);
    addEventListener('resize', onResize);
    go();

    return () => {
      removeEventListener('hashchange', onHashChange);
      removeEventListener('resize', onResize);
    };
  }, []);

  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: `
        :root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);--bg:#0a1224;--card:#111c36;--bd:#223256;--tx:#e8edf7;--mu:#98a6c3;--cy:#4fd1e8;--am:#f5b041;color-scheme:dark}
        html{scroll-padding-top:env(safe-area-inset-top,0px)}*{box-sizing:border-box}
        body{margin:0;background:linear-gradient(160deg,#0a1224,#0d1b3a 60%,#0a1224);color:var(--tx);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;min-height:100vh}
        a{color:var(--cy)}nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;gap:4px;flex-wrap:wrap;align-items:center;padding:8px 12px;background:#0a1224ee;border-bottom:1px solid var(--bd)}
        nav b{margin-right:auto;letter-spacing:.08em}nav a,button,select,input{font:inherit}
        nav a{color:var(--mu);text-decoration:none;padding:6px 10px;border-radius:8px}nav a.on,nav a:hover{color:var(--tx);background:var(--card)}
        main{max-width:1100px;margin:auto;padding:16px}h1{font-size:2rem;margin:.2em 0}h2{font-size:1.2rem;margin:.2em 0 .6em}h3{margin:.2em 0;font-size:1rem}
        .g{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}.c{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:14px;box-shadow:0 0 18px #4fd1e810}
        .mu{color:var(--mu);font-size:.85rem}button,.btn{background:var(--cy);color:#04101f;border:0;border-radius:8px;padding:8px 14px;cursor:pointer;font-weight:600;text-decoration:none;display:inline-block}
        button.s{background:transparent;color:var(--tx);border:1px solid var(--bd)}button:focus-visible,a:focus-visible,select:focus-visible,input:focus-visible{outline:2px solid var(--am);outline-offset:2px}
        select,input[type=text],input[type=search]{background:#0a1224;color:var(--tx);border:1px solid var(--bd);border-radius:8px;padding:7px}
        .demo{background:#3a2a05;color:var(--am);border:1px solid var(--am);border-radius:8px;padding:4px 8px;font-size:.78rem;display:inline-block;margin:4px 0}
        .tag{border:1px solid var(--bd);border-radius:99px;padding:1px 8px;font-size:.75rem;color:var(--mu);margin-right:4px;display:inline-block}
        .row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}canvas{width:100%;background:#0a1224;border-radius:8px;border:1px solid var(--bd)}
        .hero{padding:28px 0}.hero p{max-width:640px;color:var(--mu)}table{width:100%;border-collapse:collapse;font-size:.85rem}td,th{border-bottom:1px solid var(--bd);padding:5px;text-align:left;vertical-align:top}
        .ok{color:#6ee7a0}.warn{color:var(--am)}.na{color:var(--mu);font-style:italic}.wrap{overflow-x:auto}footer{color:var(--mu);font-size:.8rem;padding:24px 16px;max-width:1100px;margin:auto}
        @media print{nav,.noprint{display:none}body{background:#fff;color:#000}.c{background:#fff;border-color:#999}a{color:#000}}
      `}} />
      <nav aria-label="Main">
        <b>🔥 FIREWISE-X</b>
        <a href="#/">Home</a>
        <a href="#/mc">Mission Control</a>
        <a href="#/exp">Experiments</a>
        <a href="#/flame">Flame Studio</a>
        <a href="#/sensor">Sensors</a>
        <a href="#/evid">Evidence</a>
        <a href="#/cmp">Compare</a>
      </nav>
      <main id="app" aria-live="polite"></main>
      <footer>
        FIREWISE-X is an independent research/decision-support prototype made for NASA Space Apps Challenge 2026. It is <b>not</b> endorsed by, affiliated with, or certified by NASA, and is not a spacecraft fire detector. Sources: <a href="https://psi.nasa.gov/">NASA PSI</a> · <a href="https://ntrs.nasa.gov/">NASA NTRS</a> · <a href="https://www.nist.gov/publications">NIST publications</a>.
      </footer>
    </>
  );
}
