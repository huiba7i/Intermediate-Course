"""
    饼图数据
"""
from com.aowin.connect_library import DB_util


def insert(data):
    """
        新增一条饼图数据
    :param stu: 数据对象 Tuple(全部列)
    :return: 返回新增条数
    """
    con = DB_util.getConn()
    try:
        cur = con.cursor()
        sql = 'INSERT INTO doughnutChart (VALUE, NAME) VALUES (%s, %s)'
        cur.execute(sql, data)
        con.commit()
        return cur.rowcount
    finally:
        if con:
            con.close()


def select_all():
    """
        查询全部数据信息
    :return: 全部信息
    """
    con = DB_util.getConn()
    try:
        cur = con.cursor()
        sql = 'SELECT * FROM doughnutChart'
        cur.execute(sql)

        datas = []
        for d in cur.fetchall():
            d = {
                'id': d[0],
                'value': d[1],
                'name': d[2]
            }
            datas.append(d)
        return datas
    finally:
        if con:
            con.close()

if __name__ == '__main__':
    # d = ('599', '搜索引擎')
    # n = insert(d)
    # print(n)

    n = select_all()
    print(n)
