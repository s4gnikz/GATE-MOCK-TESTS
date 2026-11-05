// Offline artifact QA. Usage: node render_check.cjs [PLAYWRIGHT_PACKAGE_PATH] [--paper N]
const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const args=process.argv.slice(2);
let paper=1;
const paperIndex=args.indexOf('--paper');
if(paperIndex!==-1){
 const value=args[paperIndex+1];
 if(!value||!/^\d+$/.test(value)||Number(value)<1||Number(value)>100){
  throw Error('--paper must be an integer from 1 through 100');
 }
 paper=Number(value);
 args.splice(paperIndex,2);
}
if(args.length>1||args.some(a=>a.startsWith('--'))){
 throw Error('Usage: node render_check.cjs [PLAYWRIGHT_PACKAGE_PATH] [--paper N]');
}
const {chromium}=require(args[0] || 'playwright');
const root=path.resolve(__dirname,'..');
const folder=path.join(root,'reports','rendered','Mock_'+String(paper).padStart(3,'0'));
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage({viewport:{width:1000,height:1000}});
 const checks=[];
 for(const file of ['README.html','SOLUTIONS.html']){
  await page.goto(pathToFileURL(path.join(folder,file)).href);
  const result=await page.evaluate(()=>({
   headings:[...document.querySelectorAll('h2,h3')].map(e=>e.textContent),
   overflow:document.documentElement.scrollWidth>innerWidth,
   missingImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).length,
   tables:document.querySelectorAll('table').length,
   codeBlocks:document.querySelectorAll('pre').length,
   height:document.body.scrollHeight
  }));
  if(result.overflow||result.missingImages)throw Error('Layout/resource failure in '+file);
  const count=result.headings.filter(s=>/^Q\d+(\.|$)/.test(s)).length;
  if(count!==65)throw Error(file+' has '+count+' question headings');
  await page.screenshot({path:path.join(folder,file+'.top.png')});
  if(file==='README.html'){
   await page.getByRole('heading',{name:'Q27.',exact:false}).scrollIntoViewIfNeeded();
   await page.screenshot({path:path.join(folder,'question27.png')});
   await page.getByRole('heading',{name:'ANSWER KEY',exact:false}).scrollIntoViewIfNeeded();
   await page.screenshot({path:path.join(folder,'answer-key.png')});
  }
  checks.push({file,viewport:1000,...result});
  await page.setViewportSize({width:420,height:1000});
  const mobileOverflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
  if(mobileOverflow)throw Error('Narrow-screen overflow in '+file);
  checks.push({file,viewport:420,overflow:mobileOverflow});
  await page.setViewportSize({width:1000,height:1000});
 }
 fs.writeFileSync(path.join(folder,'render_checks.json'),JSON.stringify(checks,null,2));
 await browser.close();
 console.log('Both documents: 65 headings, no horizontal overflow at 1000px/420px, no missing images.');
})().catch(error=>{console.error(error);process.exit(1);});
