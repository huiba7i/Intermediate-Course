"""
    后台增加一条文章信息表
"""
import encoding
import cgi
import re
from com.aowin.connect_table import article

f = cgi.FieldStorage()

title = f.getvalue('title')
content = f.getvalue('content')
releaseTime = f.getvalue('releaseTime')

if not re.search('^[\u4e00-\u9fa50-9a-zA-Z]{0,30}$', title):
    print('access-control-allow-origin: *')
    print('')
    print('文章标题错误', end='')
if not content:
    print('access-control-allow-origin: *')
    print('')
    print('文章内容错误', end='')
elif not re.search('^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$', releaseTime):
    print('access-control-allow-origin: *')
    print('')
    print('创建时间错误', end='')
else:
    list = (title, content, releaseTime)
    inse = article.inster(list)
    if inse:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')
