"""
    后台删除一条用户信息
"""
import encoding
import cgi
import re
from com.aowin.connect_table import new_user

f = cgi.FieldStorage()

id = f.getvalue('id')

if not id:
    print('access-control-allow-origin: *')
    print('')
    print('必须传入ID', end='')
elif not re.search('[0-9]', id):
    print('access-control-allow-origin: *')
    print('')
    print('传入ID错误', end='')
else:
    d = new_user.delete(id)
    if d:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')
