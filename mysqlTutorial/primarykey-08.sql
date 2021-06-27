-- 主键约束
-- 使某个字段不重复且不得为空，确保表内所有数据的唯一性。
create table user(
    id int primary key,
    name varchar(20));

-- 联合主键
-- 联合主键中的每个字段都不能为空，并且加起来不能和已设置的联合主键重复。
create table user2(
    id int,
    name varchar(20),
    primary key(id, name));

insert into user2 values(1, '张三');
insert into user2 values(1, '李四');

-- 自增约束
-- 自增约束的主键由系统自动递增分配。
create table user3(
    id int primary key auto_increment,
    name varchar(20));

-- 添加主键约束
-- 如果忘记设置主键，还可以通过SQL语句设置（两种方式）：
create table user4(
    id int,
    name varchar(20));

alter table user4 add primary key(id);
alter table user4 modify id int primary key;

-- 删除主键
alter table user4 drop primary key;

-- 建表时创建唯一主键 unique(id, name) id+name组合 起来不重复即可, unique可以为空，主键必须非空。
CREATE TABLE user (
    id INT,
    name VARCHAR(20),
    UNIQUE(id, name)
);

-- 添加唯一主键
-- 如果建表时没有设置唯一建，还可以通过SQL语句设置（两种方式）：
ALTER TABLE user ADD UNIQUE(name);
ALTER TABLE user MODIFY name VARCHAR(20) UNIQUE;

-- 删除唯一主键
ALTER TABLE user DROP INDEX name;

-- 建表时添加非空约束
-- 约束某个字段不能为空
create table user5(
    id int,
    name varchar(20) not null);

-- 移除非空约束
alter table user5 modify name varchar(20);

-- 建表时添加默认约束
-- 约束某个字段的默认值
CREATE TABLE user2 (
    id INT,
    name VARCHAR(20),
    age INT DEFAULT 10
);

-- 移除非空约束
ALTER TABLE user MODIFY age INT;

--外键约束
-- 1. 主表（父表）classes 中没有的数据值，在副表（子表）students 中，是不可以使用的；
-- 2. 主表中的记录被副表引用时，主表不可以被删除。
-- 班级主表
create table classes(
    id int primary key,
    name varchar(20));

--学生副表
create table students(
    id int primary key,
    name varchar(20),
    class_id int,
    constraint foreign key (class_id) references classes(id));

--check检查约束，mysql不支持，用来限定值得范围。
