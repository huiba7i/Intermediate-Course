"""
    前台增加一条用户信息表
"""

import encoding
import cgi
import re
import json
from com.aowin.connect_table import userInfo

f = cgi.FieldStorage()

name = f.getvalue('name')
subTitle = f.getvalue('subTitle')
createionTime = f.getvalue('createionTime')

if not re.search('^[\u4E00-\u9FA50-9a-zA-Z_]{3,10}$', name):
    print('access-control-allow-origin: *')
    print('')
    print('用户名错误', end='')
elif not re.search('^[\u4e00-\u9fa50-9a-zA-Z],{0,20}$', subTitle):
    print('access-control-allow-origin: *')
    print('')
    print('副标题错误', end='')
elif not re.search('^(d{4})-(d{2})-(d{2}) (d{2}):(d{2}):(d{2})$', createionTime):
    print('access-control-allow-origin: *')
    print('')
    print('创建时间错误', end='')
else:
    list = (name, subTitle, createionTime)
    info = userInfo.insert(list)
    if info:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')
