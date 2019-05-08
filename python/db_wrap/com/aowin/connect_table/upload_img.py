"""
    上传图片（上传路径方式）
"""
from com.aowin.connect_library import DB_util


def insert(imgs):
    """
        新增图片
    :param imgs: 数据对象 Tuple(全部列)
    :return: 返回新增条数
    """
    con = DB_util.getConn()
    try:
        cur = con.cursor()
        sql = 'INSERT INTO uploadImages (IMGCOUNT, IMGPATH, UPDATETIME) VALUES (%s, %s, %s)';
        cur.execute(sql, imgs)
        con.commit()
        return cur.rowcount
    finally:
        if con:
            con.close()
