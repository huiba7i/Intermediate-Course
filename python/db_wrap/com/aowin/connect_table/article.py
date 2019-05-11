"""
    前台文章列表
"""
from com.aowin.connect_library import DB_util
from com.aowin.modal import Page
import json
import re


def inster(stu):
    """
        增加一条文章 信息
    :param stu: 文章对象Tuple(全部列，除了阅读数和修改时间)
    :return: 返回新增条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO article (TITLE, CONTENT, RELEASETIME)' \
              'VALUES (%s, %s, %s)'
        cur.execute(sql, stu)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def delete(id):
    """
        删除一条文章信息
    :param id: 文章 id
    :return: 返回已删除条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM article WHERE ID=%s'
        cur.execute(sql, (id,))
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def update(user):
    """
       修改文章信息
    :param user: 文章对象Tuple(全部列，除了阅读数和文章发布时间)
    :return: 返回已修改条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'UPDATE article SET TITLE=%s, CONTENT=%s, MODIFICATIONTIME=%s WHERE ID=%s'
        cur.execute(sql, user)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def select_all():
    """
        查询全部文章信息
    :return: 返回全部信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM article'
        cur.execute(sql)

        # 将Tuple的list，转换成User对象的list
        users = []
        for u in cur.fetchall():
            s2 = re.sub(r'<.*?>', '', u[2])
            # 再用str.replace()函数去掉'\n'
            s2 = s2.replace('\n', '')
            user = {
                'id': u[0],
                'title': u[1],
                'content': s2,
                'readingVolume': u[3],
                'releaseTime': str(u[4]),
                'modificationTime': str(u[5]),
            }
            users.append(user)
        return users
    finally:
        if conn:
            conn.close()


def select_all_page(list, pageNum):
    """
        分页查询
    :param list: 字典对象
    加入可能又以下key
        id,
        title,
        readingVolume    # 阅读数量
        startDete,
        endDate,
        isConvertFormat     # 是否转换成字符串(默认内容带有标签) true/false
    :param pageNum: 页数
    :return: 查询到的数据对象
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sqlData = 'SELECT * FROM article'
        sqlCount = 'SELECT count(*) FROM article'

        sql = ' WHERE 1 = 1'

        params = []  # 用来存放具体的条件参数
        if 'id' in list:
            if list['id']:
                sql += ' AND ID = %s'
                params.append(list['id'])
        if 'title' in list:
            if list['title']:
                sql += ' AND TITLE = %s'
                params.append(list['title'])
        if 'readingVolume' in list:
            if list['readingVolume']:
                sql += ' AND READINGVOLUME = %s'
                params.append(list['readingVolume'])
        if 'startDay' in list:
            if list['startDay']:
                sql += ' AND RELEASETIME >= %s'
                params.append(list['startDay'])
        if 'endDay' in list:
            if list['endDay']:
                sql += ' AND RELEASETIME <= %s'
                params.append(list['endDay'])

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

        # 判断是否转换为字符串
        if 'isConvertFormat' in list:
            if list['isConvertFormat']:
                isTrue = True
            else:
                isTrue = False
        else:
            return 'isConvertFormat'

        lists = []
        for u in cur.fetchall():
            if isTrue == True:
                s2 = re.sub(r'<.*?>', '', u[2])
                s2 = s2.replace('\n', '')
            else:
                s2 = u[2]

            list = {
                'id': u[0],
                'title': u[1],
                'content': s2,
                'readingVolume': u[3],
                'releaseTime': str(u[4]),
                'modificationTime': str(u[5]),
            }
            lists.append(list)
        page.data = lists

        return page
    finally:
        if (conn):
            conn.close()

# if __name__ == '__main__':
#     n = select_all_page({}, 1)
#     page = json.dumps(n.__dict__, ensure_ascii=False)
#     # print(page)
