"""
    操作用户信息表，增删改查功能
"""
from com.aowin.connect_library import DB_util
from com.aowin.modal import modal
from com.aowin.modal import Page
import json
import re


def inster(stu):
    """
        增加一条用户信息
    :param stu: 用户对象Tuple(全部列)
    :return: 返回新增条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO user (NAME, PROVINCE, CITY, ADDRESS, ZIP, DATE) VALUES (%s, %s, %s, %s, %s, %s)'
        cur.execute(sql, stu)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def delete(id):
    """
        删除一条用户信息
    :param id: 用户id
    :return: 返回已删除条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM user WHERE ID=%s'
        cur.execute(sql, (id,))
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def update(user):
    """
       修改用户信息
    :param user: 用户对象Tuple(全部列)
    :return: 返回已修改条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'UPDATE user SET NAME=%s, PROVINCE=%s, CITY=%s, ADDRESS=%s, ZIP=%s, DATE=%s WHERE ID=%s'
        cur.execute(sql, user)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def select_all():
    """
        查询全部用户信息
    :return: 返回全部信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM user'
        cur.execute(sql)

        # 将Tuple的list，转换成User对象的list
        users = []
        for u in cur.fetchall():
            user = {
                'id': u[0],
                'name': u[1],
                'province': u[2],
                'city': u[3],
                'address': u[4],
                'zip': u[5],
                'date': str(u[6])
            }
            users.append(user)
        return users
    finally:
        if conn:
            conn.close()


def select_condition_data(stu):
    """
        动态查询用户信息
    :param stu: 字典对象
    加入可能又以下key
        id,
        name,
        province,
        city,
        zip
        startDay,
        endDay,
    :return: 返回查询到的信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM user WHERE 1 = 1'
        params = []  # 用来存放具体的条件参数
        if 'id' in stu:
            if stu['id']:
                sql += ' AND ID = %s'
                params.append(stu['id'])
        if 'name' in stu:
            if stu['name']:
                sql += ' AND NAME LIKE concat("%", %s, "%")'
                params.append(stu['name'])
        if 'province' in stu:
            if stu['province']:
                sql += ' AND PROVINCE = %s'
                params.append(stu['province'])
        if 'city' in stu:
            if stu['city']:
                sql += ' AND CITY = %s'
                params.append(stu['city'])
        if 'zip' in stu:
            if stu['zip']:
                sql += ' AND ZIP = %s'
                params.append(stu['zip'])
        if 'startDay' in stu:
            if stu['startDay']:
                sql += ' AND DATE >= %s'
                params.append(stu['startDay'])
        if 'endDay' in stu:
            if stu['endDay']:
                sql += ' AND DATE <= %s'
                params.append(stu['endDay'])

        print(sql)
        cur.execute(sql, tuple(params))

        # 将tuple的list 转成Student对象的list
        users = []
        for u in cur.fetchall():
            user = {
                'id': u[0],
                'name': u[1],
                'province': u[2],
                'city': u[3],
                'address': u[4],
                'zip': u[5],
                'date': str(u[6])
            }
            users.append(user)
        return users
    finally:
        if conn:
            conn.close()


def select_data(stu, pageNum):
    """
       分页查询
    :param stu: 字典对象
    加入可能又以下key
        id,
        name,
        province,
        city,
        zip
        startDay,
        endDay,
    :return: page 对象
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sqlData = 'SELECT * FROM user'
        sqlCount = 'SELECT count(*) FROM user'

        sql = ' WHERE 1 = 1'

        params = []  # 用来存放具体的条件参数
        if 'id' in stu:
            if stu['id']:
                sql += ' AND ID = %s'
                params.append(stu['id'])
        if 'name' in stu:
            if stu['name']:
                sql += ' AND NAME LIKE concat("%", %s, "%")'
                params.append(stu['name'])
        if 'province' in stu:
            if stu['province']:
                sql += ' AND PROVINCE = %s'
                params.append(stu['province'])
        if 'city' in stu:
            if stu['city']:
                sql += ' AND CITY = %s'
                params.append(stu['city'])
        if 'zip' in stu:
            if stu['zip']:
                sql += ' AND ZIP = %s'
                params.append(stu['zip'])
        if 'startDay' in stu:
            if stu['startDay']:
                sql += ' AND DATE >= %s'
                params.append(stu['startDay'])
        if 'endDay' in stu:
            if stu['endDay']:
                sql += ' AND DATE <= %s'
                params.append(stu['endDay'])

        print(sql)

        page = Page.Page()

        # 查询总条数
        sqlCount += sql
        cur.execute(sqlCount, tuple(params))
        countTotal = cur.fetchone()[0]
        page.countTotal = countTotal

        # 计算总页数
        if countTotal % page.pageSize == 0:
            pageTotal = countTotal // page.pageSize
        else:
            pageTotal = countTotal // page.pageSize + 1
        page.pageTotal = pageTotal

        page.pageNum = pageNum

        # 查询记录
        sqlData += sql
        sqlData += ' LIMIT %s, %s'
        params.append((pageNum - 1) * page.pageSize)
        params.append(page.pageSize)

        cur.execute(sqlData, tuple(params))

        users = []
        for u in cur.fetchall():
            user = {
                'id': u[0],
                'name': u[1],
                'province': u[2],
                'city': u[3],
                'address': u[4],
                'zip': u[5],
                'date': str(u[6])
            }
            users.append(user)
        page.data = users

        return page
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    # n = re.search(r'(\d{4}-\d{2}-\d{2})', '2019-02-2')
    # print(n)
    # if not re.search('^[\u4E00-\u9FA50-9a-zA-Z_]{3,6}$', 'hahah'):
    #     print('error')
    # else:
    #     print('ok')

    stu = {'startDay': 'Wed May 01 2019 00:00:00 GMT+0800 (中国标准时间)', 'endDay': ' Thu May 30 2019 00:00:00 GMT+0800 (中国标准时间)'}
    n = select_condition_data(stu)
    print(n)
