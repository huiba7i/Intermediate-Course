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
id = f.getvalue('id')

if not id:
    print('access-control-allow-origin: *')
    print('')
    print('必须传入ID', end='')
elif not re.search('[\u4E00-\u9FA50-9a-zA-Z_]{3,10}', name):
    print('access-control-allow-origin: *')
    print('')
    print('用户名格式错误', end='')
elif not re.search('^[\u4e00-\u9fa5],{0,20}$', subTitle):
    print('access-control-allow-origin: *')
    print('')
    print('副标题错误', end='')
elif not re.search('^(d{4})-(d{2})-(d{2}) (d{2}):(d{2}):(d{2})$', lastModificationTime):
    print('access-control-allow-origin: *')
    print('')
    print('修改时间格式错误', end='')
else:
    list = (name, subTitle, lastModificationTime, id)
    update = userInfo.update(list)
    if update:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')
