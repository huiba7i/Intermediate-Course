"""
    后台登录
"""

import encoding
import cgi
from com.aowin.connect_table import back_login
import json

# 1、获取客户端数据
f = cgi.FieldStorage()  # 获得所有客户端发送过来的数据
print(f)
# 获取具体参数
name = f.getvalue('name')
password = f.getvalue('pwd')

# 2、格式校验
if not name or not password:
    # 数据校验失败，不做业务处理，直接响应失败信息
    print('access-control-allow-origin: *')
    print('')
    print('error', end='')
else:
    user = back_login.back_login(name, password)
    if user:
        print('access-control-allow-origin: *')
        print('')
        dUser = {
            'isOk': 'success',
            'name': user[1]
        }
        userInfo = json.dumps(dUser)
        print(userInfo)
    else:
        print('access-control-allow-origin: *')
        print('')
        dUser = {
            'isOk': 'error',
        }
        userInfo = json.dumps(dUser)
        print(userInfo)
