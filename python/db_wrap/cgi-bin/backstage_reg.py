"""
    后台用户注册
"""

import encoding
import cgi
import re
from com.aowin.connect_table import back_login

# 1、获取客户端数据
f = cgi.FieldStorage()  # 获得所有客户端发送过来的数据
print(f)
# 获取具体参数
name = f.getvalue('name')
password = f.getvalue('pwd')

# 2、格式校验
if not re.search('^[\u4E00-\u9FA50-9a-zA-Z_]{3,10}$', name):
    print('access-control-allow-origin: *')
    print('')
    print('用户名错误', end='')
elif not re.search('^[0-9a-zA-Z]{3,6}$', password):
    print('access-control-allow-origin: *')
    print('')
    print('用户密码错误', end='')
elif not name or not password:
    # 数据校验失败，不做业务处理，直接响应失败信息
    print('access-control-allow-origin: *')
    print('')
    print('error', end='')
else:
    u = (name, password)
    user = back_login.back_insert(u)
    if user:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')
