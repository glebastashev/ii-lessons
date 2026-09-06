# -*- coding: utf-8 -*-
"""Собирает разметку карусели: mkcar.py <урок> <id> <clip:подпись> ..."""
import json, sys, os, html
n, cid = sys.argv[1], sys.argv[2]
items = [a.split(':', 1) for a in sys.argv[3:]]
vids = ''.join(
    f'<video src="clip/l{n}/{c}.mp4" poster="clip/l{n}/{c}.jpg" autoplay muted loop playsinline '
    f'preload="metadata" data-cap="{html.escape(cap)}" aria-label="{html.escape(cap)}"></video>'
    for c, cap in items)
dots = ''.join(f'<button class="dot{" on" if i==0 else ""}" data-i="{i}" aria-label="слайд {i+1}"></button>'
               for i in range(len(items)))
mk = (f'<div class="car" id="car-{cid}">\n      <div class="car-view">\n'
      f'        <div class="car-track">{vids}</div>\n'
      f'        <button class="car-nav prev" aria-label="назад">‹</button>\n'
      f'        <button class="car-nav next" aria-label="вперёд">›</button>\n      </div>\n'
      f'      <div class="car-bar"><div class="car-dots">{dots}</div>'
      f'<span class="car-cnt">1 / {len(items)}</span></div>\n'
      f'      <div class="car-cap">{html.escape(items[0][1])}</div>\n    </div>')
p = f'l{n}/_car.json'
d = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
d[cid] = mk
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
print(f'карусель {cid}: {len(items)} слайдов')
