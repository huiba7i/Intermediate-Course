"""
    后台首页 柱状图
"""
import encoding
import cgi
import json
from com.aowin.connect_table import bar_simble

f = cgi.FieldStorage()

data = bar_simble.select_all()
if data:
    print('Access-Control-Allow-Origin: *')
    print('')
    data = json.dumps(data, ensure_ascii=False)
    print(data)
else:
    print('Access-Control-Allow-Origin: *')
    print('')
    print('error', end='')

