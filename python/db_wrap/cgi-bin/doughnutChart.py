"""
    后台首页 饼图
"""
import encoding
import cgi
import json
from com.aowin.connect_table import doughnut_chart

f = cgi.FieldStorage()

data = doughnut_chart.select_all()
if data:
    print('Access-Control-Allow-Origin: *')
    print("Content-type:text/plain;charset=utf-8")
    print('')
    data = json.dumps(data, ensure_ascii='utf-8')
    print(data)
else:
    print('Access-Control-Allow-Origin: *')
    print('')
    print('error', end='')
