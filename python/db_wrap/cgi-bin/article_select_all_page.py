"""
    后台分页显示文章信息
"""
import encoding
import cgi
import json
from com.aowin.connect_table import article

f = cgi.FieldStorage()

id = f.getvalue('id')
title = f.getvalue('title')
readingVolume = f.getvalue('readingVolume')
startDate = f.getvalue('startDate')
endDate = f.getvalue('endDate')
pageNum = f.getvalue('pageNum')

isConvertFormat = f.getvalue('isConvertFormat')

list = {
    'id': id,
    'title': title,
    'readingVolume': readingVolume,
    'startDate': startDate,
    'endDate': endDate,
    'isConvertFormat': isConvertFormat
}

page = article.select_all_page(list, int(pageNum))
if page:
    print('Access-Control-Allow-Origin: *')
    print("Content-type:text/plain;charset=utf-8")
    print('')
    page = json.dumps(page.__dict__, ensure_ascii=False)
    print(page)
else:
    print('Access-Control-Allow-Origin: *')
    print('')
    print('error', end='')
