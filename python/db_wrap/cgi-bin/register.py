"""
    前台注册
"""
import encoding
import cgi
from com.aowin.connect_table import new_Login
import re

f = cgi.FieldStorage()

username = f.getvalue('username')
userpwd = f.getvalue('userpwd')
usertel = f.getvalue('usertel')
usersex = f.getvalue('usersex')

if not re.search('^[\u4E00-\u9FA50-9a-zA-Z_]+$', username):
    print('access-control-allow-origin: *')
    print('')
    print('用户名错误', end='')
elif not re.search('^[0-9a-zA-Z]{6,10}$', userpwd):
    print('access-control-allow-origin: *')
    print('')
    print('用户密码错误', end='')
elif not re.search('^[1][0-9]{10}$', usertel):
    print('access-control-allow-origin: *')
    print('')
    print('用户手机号错误', end='')
elif not re.search('^[男|女]$', usersex):
    print('access-control-allow-origin: *')
    print('')
    print('用户性别错误', end='')
else:
    users = (username, userpwd, usertel, usersex)
    reg = new_Login.insert(users)
    if reg:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')






