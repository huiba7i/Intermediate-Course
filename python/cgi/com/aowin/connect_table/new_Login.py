"""
    操作用户登录表，增加和查询功能
"""
from com.aowin.connect_library import DB_util
from com.aowin.modal import modal


def insert(stu):
    """
        新增用户
    :param stu: 用户对象Tuple(全部列)
    :return: 返回新增条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO login (USERNAME, USERPWD, USERTEL, USERSEX) values (%s, %s, %s, %s)'
        cur.execute(sql, stu)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def select_data(stu):
    """
        查询用户信息
    :param stu: 用户对象Tuple(用户名列和用户信息列)
    :return: 返回查询到的信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM login WHERE USERNAME=%s AND USERPWD=%s'
        print(sql)
        cur.execute(sql, stu)
        return cur.fetchall()
    finally:
        if conn:
            conn.close()
