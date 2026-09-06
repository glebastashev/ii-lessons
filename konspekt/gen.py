import json, sys
sys.path.insert(0,'.')
import tables
car=json.load(open('_car.json'))
def shot(src,cap): return ('<div class="shot has"><video src="clip/'+src+'.mp4" poster="img/'+src
    +'.jpg" autoplay muted loop playsinline preload="metadata" aria-label="'+cap+'"></video></div>\n      <div class="cap">'+cap+'</div>')
HEAD=open('_head.html',encoding='utf-8').read()
BODY=open('_body.tpl',encoding='utf-8').read()
for k,v in car.items(): BODY=BODY.replace('{{CAR_'+k+'}}', v)
import re
BODY=re.sub(r'\{\{SHOT:(\w+)\|([^}]+)\}\}', lambda m: shot(m.group(1),m.group(2)), BODY)
BODY=tables.prepare(BODY)
open('urok-1.html','w',encoding='utf-8').write(HEAD+BODY)
print('собрано, символов:', len(HEAD+BODY))
