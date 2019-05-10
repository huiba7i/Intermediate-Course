"""
    前台台显示文章所有信息
"""
import encoding
import cgi
import json
from com.aowin.connect_table import article

fs = cgi.FieldStorage()

art = article.select_all()
if art:
    print('Access-Control-Allow-Origin: *')
    print("Content-type:text/plain;charset=utf-8")
    print('')
    art = json.dumps(art, ensure_ascii=False)
    print(art)
else:
    print('Access-Control-Allow-Origin: *')
    print('')
    print('error', end='')
