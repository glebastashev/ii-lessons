# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
import _tpl, doc_privacy, doc_marketing, doc_offer

DATE = '5 сентября 2026 года'
PAGES = [
  ('offer.html', 'Публичная оферта · ИП Заварзин М. С.',
   'Публичная оферта на заключение договора возмездного оказания информационно-консультационных услуг',
   f'Редакция от {DATE}', doc_offer.BODY, 'offer'),
  ('privacy.html', 'Политика обработки персональных данных · ИП Заварзин М. С.',
   'Политика обработки персональных данных',
   f'Редакция от {DATE}', doc_privacy.BODY, 'privacy'),
  ('marketing.html', 'Согласие на получение рекламных материалов · ИП Заварзин М. С.',
   'Согласие на получение рекламных и информационных материалов',
   f'Редакция от {DATE}', doc_marketing.BODY, 'marketing'),
]
for fn, title, h1, sub, body, cur in PAGES:
    head = _tpl.HEAD.format(title=title, h1=h1, sub=sub,
        n_offer='on' if cur=='offer' else '',
        n_privacy='on' if cur=='privacy' else '',
        n_marketing='on' if cur=='marketing' else '')
    open(fn,'w',encoding='utf-8').write(head + body + _tpl.FOOT)
    print(f'{fn}: {len(head+body+_tpl.FOOT)} символов')

idx = _tpl.HEAD.format(title='Правовые документы · ИП Заварзин М. С.',
    h1='Правовые документы', sub=f'Редакция от {DATE}',
    n_offer='', n_privacy='', n_marketing='')
idx += """
<p>Здесь собраны документы, которые регулируют отношения с учениками и подписчиками: на что вы соглашаетесь при оплате, что происходит с вашими данными и на что вы подписываетесь, оставляя телефон.</p>
<div class="tariff"><h3><a href="offer.html">Публичная оферта</a></h3>
<p>Условия договора: что входит в услугу, как оплатить, в какой срок и в каком размере вернуть деньги, кто за что отвечает. Приложение № 1 содержит перечень тарифов и состав программы.</p></div>
<div class="tariff"><h3><a href="privacy.html">Политика обработки персональных данных</a></h3>
<p>Какие данные собираются, зачем, кому передаются, сколько хранятся и как их удалить.</p></div>
<div class="tariff"><h3><a href="marketing.html">Согласие на рекламные и информационные материалы</a></h3>
<p>Отдельное согласие на звонки, СМС и сообщения в мессенджерах. Отзывается в любой момент.</p></div>
""" + _tpl.REQ
open('index.html','w',encoding='utf-8').write(idx + _tpl.FOOT)
print('index.html готов')
