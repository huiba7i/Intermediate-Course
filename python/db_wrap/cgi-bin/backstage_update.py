"""
    后台修改一条后台用户信息表
"""

import encoding
import cgi
import re
from com.aowin.connect_table import back_login

f = cgi.FieldStorage()

name = f.getvalue('name')
pwd = f.getvalue('pwd')
id = f.getvalue('id')

if not id:
    print('access-control-allow-origin: *')
    print('')
    print('必须传入ID', end='')
elif not re.search('^[\u4E00-\u9FA50-9a-zA-Z_]{3,6}$', name):
    print('access-control-allow-origin: *')
    print('')
    print('用户名错误', end='')
elif not re.search('^[0-9a-zA-Z]{3,6}$', pwd):
    print('access-control-allow-origin: *')
    print('')
    print('用户密码错误', end='')
else:
    up = (name, pwd, id)
    update = back_login.update(up)
    if up:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')

