from com.aowin.connect_library import DB_util

# 打开客户端
conn = DB_util.getConn()

# 打开一个游标
cursor = conn.cursor()

# 新增 files 数据表
sql = """
CREATE TABLE uploadfiles(
    ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FILEPATH VARCHAR(200),
    UPDATETIME TIMESTAMP 
)
"""

# 新增 barSimble 数据表
# sql = """
# CREATE TABLE basicLineChart(
#     ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     VALUE INT(10) NOT NULL DEFAULT 0,
#     NAME VARCHAR(30) NOT NULL
# )
# """

# 新增 barSimble 数据表
# sql = """
# CREATE TABLE barsimble(
#     ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     VALUE INT(10) NOT NULL DEFAULT 0,
#     NAME VARCHAR(30) NOT NULL
# )
# """

# 新增 doughnutChart 数据表
# sql = """
# CREATE TABLE doughnutChart(
#     ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     VALUE INT(10) NOT NULL DEFAULT 0,
#     NAME VARCHAR(30) NOT NULL
# )
# """

# 新增用户登录表
# sql = """
# CREATE TABLE backstage_login(
#     ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     USERNAME VARCHAR(32) NOT NULL,
#     USERPWD VARCHAR(32) NOT NULL
# )
# """

# 新增用户表
# sql = """
# CREATE TABLE user(
#     ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     NAME VARCHAR(32) NOT NULL,
#     PROVINCE VARCHAR(32),
#     CITY VARCHAR(32),
#     ADDRESS VARCHAR(128),
#     ZIP INT(6),
#     DATE DATE
# )
# """

# 发送sql语句
cursor.execute(sql)

# 关闭连接
conn.close()