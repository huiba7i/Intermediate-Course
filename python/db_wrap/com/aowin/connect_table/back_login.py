"""
    后台用户登录表
"""
from com.aowin.connect_library import DB_util


def back_insert(stu):
    """
        新增后台用户
    :param stu: 用户对象Tuple(全部列)
    :return: 返回新增条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO backstage_login (USERNAME, USERPWD) values (%s, %s)'
        cur.execute(sql, stu)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def back_login(name, pwd):
    """
        后台用户登录功能
    :param name: 用户姓名
    :param pwd: 用户登录密码
    :return: 查询到的用户信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM backstage_login WHERE USERNAME = %s AND USERPWD = %s'
        cur.execute(sql, (name, pwd))

        user = cur.fetchone()
        return user
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    back = back_login('admin', '111')
    print(back)

    # stu = ( 'admin', '111' )
    # b = back_insert(stu)
    # print(b)
