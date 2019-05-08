"""
    主题日报
"""
from com.aowin.connect_library import DB_util

def insert(con):
    """
        插入一条新闻
    :param con: 数据对象 Tuple
    :return: 返回行数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO thematicdaily (MAINTITLE, SUBTITLE, CONTENT, RELEASETIME, MODIFICATIONTIME) VALUES (%s, %s, %s, %s, %s)'
        cur.execute(sql, con)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()
