-- 新增列
ALTER TABLE student ADD STUAGE INT(5);
ALTER TABLE student ADD STUDEPARTMENT VARCHAR(20);
ALTER TABLE student ADD STUCLASS INT(5);

-- 删除 student 表中原有的数据
DELETE FROM student;

-- 新增数据
INSERT INTO student VALUES( 80101, 'zhangsan', '女', 1.59, '1990-01-01', 18, 'math', 1);
INSERT INTO student VALUES( 80103, 'lili', '女', 1.88, '1991-01-02', 20, 'computer', 2);
INSERT INTO student VALUES( 80104, 'wangwu', '女', 1.88, '1995-02-03', 23, 'english', 3);
INSERT INTO student VALUES( 80105, 'xuli', '女', 1.78, '2001-02-01', 22, 'math', 1);

-- 查出班级为1的人的信息
SELECT * FROM student WHERE STUCLASS = 1;

-- 查出系别为math的人的名字
SELECT STUNAME FROM student WHERE STUDEPARTMENT = 'math';

-- 查出年龄大于21的人的id
SELECT STUID FROM student WHERE STUAGE > 21;

-- 查出各个班级的平均年龄
SELECT STUCLASS,AVG(STUAGE) AverageAge FROM student GROUP BY STUCLASS;

-- 查出名字中有i的人的信息
SELECT * FROM student WHERE STUNAME LIKE '%i%';

-- 查询班级1的小于平均年龄的人的信息
SELECT * FROM student WHERE STUCLASS = 1 AND STUAGE < (SELECT AVG(STUAGE) FROM student WHERE STUCLASS = 1);
