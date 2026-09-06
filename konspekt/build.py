# -*- coding: utf-8 -*-
"""Собирает страницу конспекта: build.py <номер урока>"""
import json, re, sys, os
import tables
n = sys.argv[1]
d = f'l{n}'
cfg = json.load(open(f'{d}/meta.json', encoding='utf-8'))
car = json.load(open(f'{d}/_car.json', encoding='utf-8')) if os.path.exists(f'{d}/_car.json') else {}

def shot(src, cap):
    return ('<div class="shot has"><video src="clip/l' + n + '/' + src + '.mp4" poster="clip/l' + n + '/'
            + src + '.jpg" autoplay muted loop playsinline preload="metadata" aria-label="' + cap
            + '"></video></div>\n      <div class="cap">' + cap + '</div>')

SHELL = open('_shell.html', encoding='utf-8').read()
BODY = open(f'{d}/_body.tpl', encoding='utf-8').read()
for k, v in car.items():
    BODY = BODY.replace('{{CAR_' + k + '}}', v)
BODY = re.sub(r'\{\{SHOT:(\w+)\|([^}]+)\}\}', lambda m: shot(m.group(1), m.group(2)), BODY)
BODY = tables.prepare(BODY)

toc = ''.join(f'<a href="#{i}">{t}</a>' for i, t in cfg['toc'])
pills = ''.join(f'<span class="pill{" on" if k==0 else ""}">{p}</span>' for k, p in enumerate(cfg['pills']))
html = (SHELL.replace('{{TITLE}}', cfg['title']).replace('{{H1}}', cfg['h1'])
             .replace('{{PILLS}}', pills).replace('{{TOC}}', toc)
             .replace('{{FOOT}}', cfg['foot']).replace('{{VIDEO}}', cfg.get('video', '')))
html = html.replace('{{BODY}}', BODY)
out = f'urok-{n}.html'
open(out, 'w', encoding='utf-8').write(html)
print(f'{out}: {len(html)} символов, роликов {html.count("<video")}')
