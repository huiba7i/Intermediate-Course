"""
    前台更新一条用户信息
"""
import encoding
import cgi
import re
from com.aowin.connect_table import userInfo

f = cgi.FieldStorage()

name = f.getvalue('name')
subTitle = f.getvalue('subTitle')
lastModificationTime = f.getvalue('lastModificationTime')
loginName = f.getvalue('loginName')
loginPwd = f.getvalue('loginPassword')
id = f.getvalue('id')

if not id:
    print('access-control-allow-origin: *')
    print("Content-type:text/plain;charset=utf-8")
    print('')
    print('必须传入ID', end='')
elif not re.search('^[\u4E00-\u9FA50-9a-zA-Z_]{3,10}$', name):
    print('access-control-allow-origin: *')
    print('')
    print('用户名格式错误', end='')
elif not re.search('^[\u4E00-\u9FA50-9a-zA-Z，。；！？’‘“”_!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~]{0,20}$', subTitle):
    print('access-control-allow-origin: *')
    print('')
    print('副标题错误', end='')
elif not re.search('^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$', lastModificationTime):
    print('access-control-allow-origin: *')
    print('')
    print('修改时间格式错误', end='')
elif not re.search('^[\u4E00-\u9FA50-9a-zA-Z_]{3,10}$', loginName):
    print('access-control-allow-origin: *')
    print('')
    print('用户名错误', end='')
elif not re.search('^[0-9a-zA-Z]{3,6}$', loginPwd):
    print('access-control-allow-origin: *')
    print('')
    print('用户密码错误', end='')
else:
    list = (name, subTitle, lastModificationTime, loginName, loginPwd, id)
    update = userInfo.update(list)
    if update:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')
