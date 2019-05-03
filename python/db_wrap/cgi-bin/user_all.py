"""
    后台分页显示用户信息
"""
import encoding
import cgi
import json
from com.aowin.connect_table import new_user

fs = cgi.FieldStorage()

pageNum = fs.getvalue('pageNum')  # 获取当前页码
id = fs.getvalue('id'),
name = fs.getvalue('name')
province = fs.getvalue('province')
city = fs.getvalue('city')
zip = fs.getvalue('zip')
startDay = fs.getvalue('startDay')
endDay = fs.getvalue('endDay')

users = {
    'id': id,
    'name': name,
    'province': province,
    'city': city,
    'zip': zip,
    'startDay': startDay,
    'endDay': endDay
}

page = new_user.select_data(users, int(pageNum))
if page:
    print('Access-Control-Allow-Origin: *;Content-type:text/plain;charset=utf-8')
    print('')
    page = json.dumps(page.__dict__, ensure_ascii=False)
    print(page)
else:
    print('Access-Control-Allow-Origin: *;Content-type:text/plain;charset=utf-8')
    print('')
    print('error', end='')
