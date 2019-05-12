"""
    vue-blog 前台用户信息
"""
from com.aowin.connect_library import DB_util
import re

def insert(user):
    """
        添加一条用户信息
    :param stu: 用户对象Tuple(全部列，除了上次修改时间列)
    :return: 返回新增条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO userinfo (NAME, SUBTITLE, CREATIONTIME, LOGINNAME, LOGINPASSWORD) VALUES' \
              '(%s, %s, %s, %s, %s)'
        cur.execute(sql, user)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def delete(id):
    """
        删除一条用户信息
    :param id: 用户 id
    :return: 返回已删除条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM userinfo WHERE ID = %s'
        cur.execute(sql, (id,))
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def update(list):
    """
       修改用户信息
    :param user: 用户对象Tuple(全部列，除了创建时间)
    :return: 返回已修改条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'UPDATE userinfo SET NAME=%s, SUBTITLE=%s, LASTMODIFICATIONTIME=%s, LOGINNAME=%s, LOGINPASSWORD=%s WHERE ID=%s'
        cur.execute(sql, list)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def select_all():
    """
        查询所有用户信息
    :return: 返回所有用户信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM userinfo'
        cur.execute(sql)

        # 将Tuple的list，转换成User对象的list
        users = []
        for u in cur.fetchall():
            user = {
                'id': u[0],
                'name': u[1],
                'subTitle': u[2],
                'creationTime': str(u[3]),
                'lastModificationTime': str(u[4]),
                'loginName': u[5],
                'loginPassword': u[6]
            }
            users.append(user)
        return users

    finally:
        if conn:
            conn.close()


def userInfo_login(name, pwd):
    """
        前台用户登录功能
    :param name: 用户姓名
    :param pwd: 用户登录密码
    :return: 查询到的用户信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM userInfo WHERE LOGINNAME = %s AND LOGINPASSWORD = %s'
        cur.execute(sql, (name, pwd))

        # user = cur.fetchone()

        users = []
        for u in cur.fetchall():
            s2 = re.sub(r'<.*?>', '', u[2])
            # 再用str.replace()函数去掉'\n'
            s2 = s2.replace('\n', '')
            user = {
                'id': u[0],
                'name': u[1],
                'subTitle': s2,
                'creationTime': str(u[3]),
                'lastModificationTime': str(u[4]),
                'loginName': u[5],
                'loginPassword': u[6]
            }
            users.append(user)

        return users
    finally:
        if conn:
            conn.close()


# if __name__ == '__main__':
#     # a = ('aa', 'aa', '2019-05-12 20:28:29', 'hahah', '1111')
#     # aa = insert(a)
#     # print(aa)
#
#     c = select_all()
#     print(c)
