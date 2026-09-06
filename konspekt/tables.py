# -*- coding: utf-8 -*-
"""Готовит таблицы к телефону: подписи колонок в data-th плюс обёртка со скроллом."""
import re, html

def prepare(s):
    def one(m):
        tbl = m.group(0)
        heads = [re.sub(r'<[^>]+>', '', h).strip()
                 for h in re.findall(r'<th[^>]*>(.*?)</th>', tbl, re.S)]
        if not heads:
            return tbl
        def row(rm):
            body = rm.group(0)
            i = [0]
            def cell(cm):
                k = i[0]; i[0] += 1
                inner = cm.group(2)
                lab = html.escape(heads[k]) if k < len(heads) else ''
                empty = ' data-empty="1"' if not re.sub(r'<[^>]+>|&nbsp;|\s', '', inner) else ''
                return f'<td{cm.group(1)} data-th="{lab}"{empty}>{inner}</td>'
            return re.sub(r'<td([^>]*)>(.*?)</td>', cell, body, flags=re.S)
        tbl = re.sub(r'(?s)<tr>(?:(?!</tr>).)*</tr>', row, tbl)
        return '<div class="tblwrap">' + tbl + '</div>'
    return re.sub(r'(?s)<table[^>]*>.*?</table>', one, s)
