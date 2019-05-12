"""
    显示后天所有用户信息
"""
import encoding
import cgi
import json
from com.aowin.connect_table import back_login

fs = cgi.FieldStorage()

page = back_login.select_all()
if page:
    print('Access-Control-Allow-Origin: *')
    print("Content-type:text/plain;charset=utf-8")
    print('')
    page = json.dumps(page, ensure_ascii=False)
    print(page)
else:
    print('Access-Control-Allow-Origin: *')
    print('')
    print('error', end='')
