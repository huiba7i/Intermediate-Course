"""
    后台修改一条文章阅读量
"""

import encoding
import cgi
from com.aowin.connect_table import article

f = cgi.FieldStorage()

count = f.getvalue('readingVolume')
id = f.getvalue('id')

print('access-control-allow-origin: *')

if not count and not id:
    print('')
    print('请正确传入参数')
else:
    list = (count, id)
    up = article.update_readingVolume(list)
    if up:
        print('')
        print('success', end='')
    else:
        print('')
        print('error', end='')
