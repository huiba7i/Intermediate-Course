"""
    后台根据id，获取个人用户信息
"""

import encoding
import cgi
import json
from com.aowin.connect_table import new_user

f = cgi.FieldStorage()

id = f.getvalue('id')
name = f.getvalue('name')
province = f.getvalue('province')
city = f.getvalue('city')
zip = f.getvalue('zip')
startDay = f.getvalue('startDay')
endDay = f.getvalue('endDay')

users = {
    'id': id,
    'name': name,
    'province': province,
    'city': city,
    'zip': zip,
    'startDay': startDay,
    'endDay': endDay
}

page = new_user.select_condition_data(users)
if page:
    print('Access-Control-Allow-Origin: *')
    print("Content-type:text/plain;charset=utf-8")
    print('')
    page = json.dumps(page, ensure_ascii=False)
    print(page)
else:
    print('Access-Control-Allow-Origin: *')
    print('')
    print('error', end='')




