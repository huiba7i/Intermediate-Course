"""
    新增一条主题日报
"""
import encoding
import cgi
from com.aowin.connect_table import thematic_daily

f = cgi.FieldStorage()

mainTitle = f.getvalue('mainTitle')                 # 主标题
subTitle = f.getvalue('subTitle')                   # 副标题
content = f.getvalue('content')                     # 文章内容
releaseTime = f.getvalue('releaseTime')             # 发布时间
modificationTime = f.getvalue('modificationTime')   # 修改时间

con = (mainTitle, subTitle, content, releaseTime, modificationTime)

d = thematic_daily.insert(con)
if con:
    print('access-control-allow-origin: *')
    print('')
    print('success', end='')
else:
    print('access-control-allow-origin: *')
    print('')
    print('error', end='')
