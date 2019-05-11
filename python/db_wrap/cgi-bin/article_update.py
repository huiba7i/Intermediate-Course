"""
    后台修改一条文章信息表
"""

import encoding
import cgi
import re
from com.aowin.connect_table import article

f = cgi.FieldStorage()

title = f.getvalue('title')
content = f.getvalue('content')
modificationTime = f.getvalue('modificationTime')
id = f.getvalue('id')

print('access-control-allow-origin: *')

if not re.search('^[\u4e00-\u9fa50-9a-zA-Z]{0,30}$', title):
    print('')
    print('文章标题错误', end='')
if not content:
    print('')
    print('文章内容错误', end='')
elif not re.search('^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$', modificationTime):
    print('')
    print('修改时间错误', end='')
else:
    list = (title, content, modificationTime, id)
    up = article.update(list)
    if up:
        print('')
        print('success', end='')
    else:
        print('')
        print('error', end='')
