"""
    上传文件（上传路径方式）
"""
from com.aowin.connect_library import DB_util


def insert(files):
    """
        上传文件
    :param files: 数据对象 Tuple(全部列)
    :return: 返回新增条数
    """
    con = DB_util.getConn()
    try:
        cur = con.cursor()
        sql = 'INSERT INTO uploadfiles (FILEPATH, UPLOADTIME) VALUES (%s, %s)'
        cur.execute(sql, files)
        con.commit()
        return cur.rowcount
    finally:
        if con:
            con.close()
