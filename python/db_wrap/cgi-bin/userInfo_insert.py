"""
    前台增加一条用户信息表
"""

import encoding
import cgi
import re
import json
from com.aowin.connect_table import userInfo

f = cgi.FieldStorage()

loginName = f.getvalue("loginName")
loginPwd = f.getvalue('loginPassword')
name = f.getvalue('name')
subTitle = f.getvalue('subTitle')
createionTime = f.getvalue('createionTime')

print("Content-type:text/plain;charset=utf-8")
print('access-control-allow-origin: *')

if not re.search('^[\u4E00-\u9FA50-9a-zA-Z\s_]{3,10}$', loginName):
    print('')
    print('用户名错误', end='')
elif not re.search('^[0-9a-zA-Z]{3,6}$', loginPwd):
    print('')
    print('用户密码错误', end='')
elif not re.search('^[\u4E00-\u9FA50-9a-zA-Z\s_]{3,10}$', name):
    print('')
    print('用户名(主标题)错误', end='')
elif not re.search('^[\u4E00-\u9FA50-9a-zA-Z\s，。；！？’‘“”_!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~]{0,20}$', subTitle):
    print('')
    print('副标题错误', end='')
elif not re.search('^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$', createionTime):
    print('')
    print('创建时间错误', end='')
else:
    list = (name, subTitle, createionTime, loginName, loginPwd)
    info = userInfo.insert(list)
    if info:
        print('')
        print('success', end='')
    else:
        print('')
        print('error', end='')
