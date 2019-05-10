"""
    vue-blog 前台用户信息
"""
from com.aowin.connect_library import DB_util


def insert(user):
    """
        添加一条用户信息
    :param stu: 用户对象Tuple(全部列，除了上次修改时间列)
    :return: 返回新增条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO userinfo (NAME, SUBTITLE, CREATIONTIME) VALUES' \
              '(%s, %s, %s)'
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
        sql = 'UPDATE userinfo SET NAME=%s, SUBTITLE=%s, LASTMODIFICATIONTIME=%s WHERE ID=%s'
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
            }
            users.append(user)
        return users

    finally:
        if conn:
            conn.close()

# if __name__ == '__main__':
    # u = ('~~企鹅跑的慢~~', '常在河海走，哪有不湿脚', '2019-05-10 10:21:00', '2019-05-10 10:21:00')
    # c = insert(u)
    # print(c)

    # c = select_all()
    # print(c)



