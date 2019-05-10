"""
    后台用户信息表
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

def delete(id):
    """
        删除一条后台用户信息
    :param id: 用户id
    :return: 返回已删除条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM backstage_login WHERE ID=%s'
        cur.execute(sql, (id,))
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()

def update(user):
    """
       修改后台用户信息
    :param user: 用户对象Tuple(全部列)
    :return: 返回已修改条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'UPDATE backstage_login SET NAME=%s, USERPWD=%s WHERE ID=%s'
        cur.execute(sql, user)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()

def select_all():
    """
        查询全部后台用户信息
    :return: 返回全部信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM backstage_login'
        cur.execute(sql)

        # 将Tuple的list，转换成User对象的list
        users = []
        for u in cur.fetchall():
            user = {
                'id': u[0],
                'name': u[1],
                'pwd': u[2],
            }
            users.append(user)
        return users
    finally:
        if conn:
            conn.close()


# if __name__ == '__main__':
    # back = back_login('admin', '111')
    # print(back)

    # stu = ( 'admin', '111' )
    # b = back_insert(stu)
    # print(b)
