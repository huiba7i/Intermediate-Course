"""
    前台登录
"""

import encoding
import cgi
from com.aowin.connect_table import userInfo
import json

# 1、获取客户端数据
f = cgi.FieldStorage()  # 获得所有客户端发送过来的数据

# 获取具体参数
name = f.getvalue('name')
password = f.getvalue('pwd')

# 2、格式校验
print('access-control-allow-origin: *')
print("Content-type:text/plain;charset=utf-8")

if not name or not password:
    # 数据校验失败，不做业务处理，直接响应失败信息
    print('')
    print('error', end='')
else:
    user = userInfo.userInfo_login(name, password)
    if user:
        print('')
        userInfo = json.dumps(user, ensure_ascii=False)
        print(userInfo)
    else:
        print('')
        print('error', end='')
