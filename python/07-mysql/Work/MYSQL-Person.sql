-- 新建表
CREATE TABLE person(
	ID INT(10) PRIMARY KEY AUTO_INCREMENT NOT NULL,
	PNAME VARCHAR(10) NOT NULL,
	SEX CHAR(1) DEFAULT '男',
	AGE INT(5)
);

-- 新增数据
INSERT INTO person (PNAME, SEX, AGE) VALUES ('张三', '男', 19);
INSERT INTO person (PNAME, SEX, AGE) VALUES ('王菲', '女', 49);
INSERT INTO person (PNAME, SEX, AGE) VALUES ('王小小', '女', 18);
 
-- 增加编号为3、名字为梁朝伟、性别为男的记录
INSERT INTO person VALUES (3, '梁朝伟', '男', 56);

-- 删除性别为女的记录。
DELETE FROM person WHERE SEX = '女';

-- 删除性别为女，且名字为王菲的记录
DELETE FROM person WHERE SEX = '女' AND PNAME = '王菲';

-- 把编号为4的记录名字改为 刘德华
UPDATE person SET PNAME = '刘德华' WHERE ID = 4;

-- 查询所有性别为女，且年龄小于25的记录
SELECT * FROM person WHERE SEX = '女' AND AGE < 25;
