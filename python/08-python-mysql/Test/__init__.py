import mysql.connector
import time

conn = mysql.connector.connect(
    user='root',
    passwd='6486813',
    host='localhost',
    database='mytest'
)

# 打开一个游标
cursor = conn.cursor()

# 创建表
# sql = """
# CREATE TABLE teacher(
#     TID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#     TNAME VARCHAR(10) NOT NULL
# )
# """

# 新增数据
# sql = 'INSERT INTO teacher (TID, TANME) VALUES (%s, %s)'
# val = (1, '杨过')

# 批量增加数据
# sql = 'INSERT INTO teacher (TID, TNAME) VALUES (%s, %s)'
# vals = [(2, 'haha'), (3, 'zzzz'), (4, 'aaaa')]

# 修改数据
sql = 'UPDATE teacher SET TNAME=%s WHERE TID=%s'
vals = ('吃吃吃', 2)

cursor.execute(sql, vals)

# 提交事务
conn.commit()

print('成功修改了', cursor.rowcount, '条数据')

# print('成功新增', cursor.rowcount, '条数据')

# 关闭连接
cursor.close()
