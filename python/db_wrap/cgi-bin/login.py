"""
    前台登录
"""
import encoding
import cgi
from com.aowin.connect_table import new_Login

# 1、获取客户端数据
f = cgi.FieldStorage()    # 获得所有客户端发送过来的数据
print(f)
# 获取具体参数
name = f.getvalue('name')
password = f.getvalue('pwd')

# 2、格式校验
if not name or not password:
    # 数据校验失败，不做业务处理，直接响应失败信息
    print()
    print('error', end='')
else:
    user = new_Login.login(name, password)
    if user:
        print("Content-type:text/html;charset=utf-8")  # 设置响应头

        print('')
        print('seccess', end='')
    else:
        print("用户名不存在，或者密码错误！")
        print('')
        print('error', end='')

