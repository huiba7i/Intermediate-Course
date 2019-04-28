-- 新建学生表
CREATE TABLE student(
	STUID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	STUNAME VARCHAR(10) NOT NULL,
	STUSEX CHAR(1) DEFAULT '男',
	STUHEIGHT DOUBLE(3, 2),
  STUBIRTHDAY DATE
);

-- 新建备份学生表
CREATE TABLE student_backup(
	STUID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	STUNAME VARCHAR(10) NOT NULL,
	STUSEX CHAR(1) DEFAULT '男',
	STUHEIGHT DOUBLE(3, 2),
  STUBIRTHDAY DATE
);

-- 新增数据
/*
	一、inster into 表名|列名 values (值);
	二、inster into 表名 select ...
			(用于表复制)
*/
-- 1-1、按顺序填入内容
INSERT INTO student VALUES(1, '张三', '男', 1.75, '2000-01-01');
INSERT INTO student VALUES(2, '张22', '男', 1.85, '2002-01-01');
INSERT INTO student VALUES(3, '33', '女', 1.78, '2003-01-01');
INSERT INTO student VALUES(4, '张33', '男', 1.88, '2004-01-01');
INSERT INTO student VALUES(5, 'jom', '男', 1.80, '2005-01-01');
-- 1-2、按列名添加内容
INSERT INTO student (STUNAME, STUHEIGHT, STUBIRTHDAY) VALUES ('小小', 1.33, '1999-03-03');
INSERT INTO student (STUNAME, STUHEIGHT, STUBIRTHDAY) VALUES ('张小娴', 1.83, '2000-03-03');
INSERT INTO student (STUNAME, STUHEIGHT, STUBIRTHDAY) VALUES ('李晓小', 1.93, '2009-03-03');
INSERT INTO student (STUNAME, STUHEIGHT, STUBIRTHDAY) VALUES ('小红', 1.73, '1997-03-03');

-- 2-1、复制数据
INSERT INTO student (STUNAME, STUHEIGHT, STUBIRTHDAY) SELECT STUNAME, STUHEIGHT, STUBIRTHDAY FROM student;
-- 2-2、复制整张表
INSERT INTO student_backup SELECT * FROM student;


-- 修改数据
UPDATE student SET STUNAME='哈哈' WHERE STUID=3;
UPDATE student SET STUBIRTHDAY='1999-01-10' WHERE STUID=2;
UPDATE student SET STUSEX='女' WHERE STUID=4;
UPDATE student SET STUSEX='女' WHERE STUID=6;





-- 查询数据
/*
	主句 不能省略
		select 
			*（查询表中的所有列）|列名1,列名2,....|表达式 1+1 ,列名*2 |函数
		from 表名

	子句
		where
			条件
		group by 列名 (分组)
			分组
		having
			分组后的条件
		order by (排序)
			排序
		limit (限制)
			限制条件
*/
-- 一、不带条件查询
SELECT * FROM student;


-- 二、给列或表取别名查询
SELECT 1+1 A,STUID,STUID*2 B FROM student;
-- 2-1、取别名，注意空格
SELECT STUID A FROM student;
SELECT STUID,STUNAME FROM student;


-- 三、where 条件
-- 3-1、关系运算符 =、!=(<>)、>、<、>=、<=
-- 3-1-1、查询 STUID 是1的学生基本信息
SELECT * FROM student WHERE STUID = 1; 
SELECT * FROM student WHERE STUID <> 1;
-- 3-1-2、查询出生日期在2000年之后的学生信息
SELECT * FROM student WHERE STUBIRTHDAY > '2000';
-- 3-1-3、查询身高大于1.8的学生信息
SELECT * FROM student WHERE STUHEIGHT > 1.8;


-- 3-2、between a and b 查询在[a,b]范围内的数据
SELECT * FROM student WHERE STUID BETWEEN 2 AND 4;


-- 3-3、模糊查询 like
-- 			% 匹配0个或多个任意字符
-- 			_ 匹配一个任意字符
-- 3-3-1、查询学生姓名中包含'小'的学生信息
SELECT * FROM student WHERE STUNAME LIKE '%小%';
-- 3-3-2、查询姓'李'的学生
SELECT * FROM student WHERE STUNAME LIKE '李%';
-- 3-3-3、查询第二个字是'小'的学生
SELECT * FROM student WHERE STUNAME LIKE '_小%';


-- 四 多条件查询(and, or) and 的优先级会大于or
-- 		and 必须同时满足条件菜可以查出来
-- 		or 只要满足其中一个条件，就可以被查出来
-- 4-1、查询姓名中包含'小'并且性别是女的学生
SELECT * FROM student WHERE STUNAME LIKE '%小%' and STUSEX='女';
SELECT * FROM student WHERE STUNAME LIKE '%小%' OR STUSEX='女';

SELECT * FROM student WHERE (STUNAME LIKE '%小%' or STUSEX='女') and STUBIRTHDAY='2000-03-03';
SELECT * FROM student WHERE STUNAME LIKE '%小%' or STUSEX='女' and STUBIRTHDAY='2000-03-03';


-- 五 统计查询 统计函数
/*
			count(列|*) 统计查询结果的总条数，指定列时，统计该列不为null的总行数
			max(列名) 取列的最大值
			min(列名) 取列的最小值
			sum(列名) 求所有列的和
			avg(列名) 求列的平均数
*/
/*
	5-1、查询统计函数时，如果不带group by子句，那么select后的结果只能统计函数，
			 不要去获取指定列的数据
			 注意：不添加group by时，把所有记录当做一个组来统计的
*/
SELECT COUNT(*),COUNT(STUBIRTHDAY),MAX(STUHEIGHT) FROM student;

-- 5-2、group by 分组统计
-- 5-2-1、统计男生人数和女生人数
-- 注意：添加group by子句时，select后面的结果可以是统计函数以及group by后列名
SELECT COUNT(*),STUSEX FROM student GROUP BY STUSEX;
-- 5-2-2、按照性别和身高做分组
SELECT COUNT(*),STUSEX,STUHEIGHT FROM student GROUP BY STUSEX, STUHEIGHT;

-- 5-2、having 分组后条件筛选 注意:统计函数作为条件
-- 5-2-1、查询总人数>3的性别以及总人口数
SELECT COUNT(*),STUSEX FROM student GROUP BY STUSEX HAVING COUNT(*) > 3;


-- 六 order by 排序(升序(asc 默认)、降序(desc))
SELECT * FROM student ORDER BY STUHEIGHT;
SELECT * FROM student ORDER BY STUHEIGHT DESC;

-- 6-1、按照两列排序，身高一样时，在安装日期降序排列
SELECT * FROM student ORDER BY STUHEIGHT,STUBIRTHDAY DESC;


-- 七 limit n,m
-- 7-1、limit n 取查询结果的前n条记录
SELECT * FROM student LIMIT 5;

-- 7-2、limit n,m 从查询结果的前n(0开始)行开始，获取m条记录(可以用来做分页查询)
SELECT * FROM student LIMIT 0, 2;

-- 7-3、假如页码n，每页显示m条记录
SELECT * FROM student LIMIT (n-1)*m,m;


-- 八 语句执行顺序
-- from > where > group by > having > select > order by > limit
SELECT
	STUSEX,COUNT(*) CON
FROM
	student
WHERE STUID >= 1
GROUP BY STUSEX
HAVING COUNT(*) > 3
ORDER BY CON
LIMIT 1;


-- 九 子查询 将一个语句的查询结果作为一个条件接着去查询
-- 查询身高大于平均身高的学生信息
SELECT * FROM student WHERE STUHEIGHT > (SELECT AVG(STUHEIGHT) FROM student);

-- 查询身高大于平均升高的学生信息以及平均身高
SELECT * FROM (SELECT AVG(STUHEIGHT) AVGHEIGHT FROM student) A, student B WHERE B.STUHEIGHT > A.AVGHEIGHT;




