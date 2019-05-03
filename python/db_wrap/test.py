from com.aowin.connect_table import new_Login
from com.aowin.connect_table import new_user
from com.aowin.connect_table import back_login

# 新增一条用户登录信息
# stu = ('tom', '123', '12345678900', '女')
# n = new_Login.insert(stu)
# print(n)

# 查询一条用户登录表信息
# sel = ('橙橙', '123456')
# s = new_Login.select_data(sel)
# print(s)


# 新增一条用户信息
# stu = ('007', '四川省', '成都市', '四川省成都市同仁大厦一幢1908', '180000', '2011-04-28')
# n = new_user.inster(stu)
# print(n)

# 删除一条用户信息
# n = new_user.delete(3)
# print(n)

# 更新一条用户信息
# stu = ('heheheheh', '北京', '北京市', '北京市中心区同仁大厦一幢1908', '200000', '2000-04-28', 1)
# n = new_user.update(stu)
# print(n)

# 查询全部用户信息
# users = new_user.select_all()
# for i in users:
#     print(i)

# 分页查询
# stu = {'province': '四川省'}
# stus = new_user.select_data(stu, 2)
# for i in stus.data:
#     print(i)

# 带条件查询
# stu = { 'startDay': '2001-01-01', 'endDay': '2019-05-01' }
# stus = new_user.select_condition_data(stu)
# for i in stus:
#     print(i)
