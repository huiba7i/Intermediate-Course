"""
    后端上传图片
"""
import encoding
import cgi
from com.aowin.connect_table import upload_img


form = cgi.FieldStorage()

img = form.getvalue('imgData')
name = form.getvalue('name')
time = form.getvalue('time')

new_name = "D:/file/" + name
file_ = open(new_name, mode="wb")
file_.write(img.encode('utf-8'))
file_.close()

opt = (img, new_name, time)
f = upload_img.insert(opt)
if f:
    print('access-control-allow-origin: *')
    print('')
    print('success', end='')
else:
    print('access-control-allow-origin: *')
    print('')
    print('error', end='')
