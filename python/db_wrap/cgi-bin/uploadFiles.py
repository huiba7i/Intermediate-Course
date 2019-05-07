"""
    后端上传文件
"""
import encoding
import cgi
from com.aowin.connect_table import upload_files

form = cgi.FieldStorage()
name = form.getvalue('name')
file = form.getvalue('file')
time = form.getvalue('time')

new_name = "D:/file/" + name
file_ = open(new_name, mode="wb")
file_.write(file.encode('utf-8'))
file_.close()

opt = (new_name, time)
f = upload_files.insert(opt)
if f:
    print('access-control-allow-origin: *')
    print('')
    print('success', end='')
else:
    print('access-control-allow-origin: *')
    print('')
    print('error', end='')
