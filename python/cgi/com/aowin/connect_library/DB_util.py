import mysql.connector


def getConn():
    """
        连接数据库
    :return:
    """
    return mysql.connector.connect(user='root', passwd='6486813', host='localhost', database='user')
