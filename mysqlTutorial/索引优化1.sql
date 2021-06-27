create table if not exists article(
    id int(10) unsigned not null auto_increment primary key,
    author_id int(10) unsigned not null,
    category_id int(10) unsigned not null,
    views int(10) unsigned not null,
    comments int(10) unsigned not null,
    title varbinary(255) not null,
    content text not null
);

insert into article(author_id, category_id, views, comments, title, content) values
(1, 1, 1, 1, '1', '1'),
(2, 2, 2, 2, '2', '2'),
(1, 1, 3, 3, '3', '3');

--单表优化
explain select id, author_id from article where category_id=1 and comments > 1 order by views desc limit 0,1;
create index idx_ccv on article(category_id, comments, views);
show index from article;
explain select id, author_id from article where category_id=1 and comments > 1 order by views desc limit 0,1;
+----+-------------+---------+------------+-------+---------------+---------+---------+------+------+----------+---------------------------------------+
| id | select_type | table   | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                                 |
+----+-------------+---------+------------+-------+---------------+---------+---------+------+------+----------+---------------------------------------+
|  1 | SIMPLE      | article | NULL       | range | idx_ccv       | idx_ccv | 8       | NULL |    1 |      100 | Using index condition; Using filesort |
+----+-------------+---------+------------+-------+---------------+---------+---------+------+------+----------+---------------------------------------+
--没有解决Using filesort，因为comments>1 范围查询导致 索引 views 失效。

drop index idx_ccv on article;
show index from article;
--解决办法绕开comments，只给category_id 和 views建索引
create index idx_cv on article(category_id, views);
show index from article;
explain select id, author_id from article where category_id=1 and comments > 1 order by views desc limit 0,1;

--双表优化
create table if not exists class(
    id int(10) unsigned not null auto_increment primary key,
    card int(10) unsigned not null
);

create table if not exists book(
    bookid int(10) unsigned not null auto_increment primary key,
    card int(10) unsigned not null
);

insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));
insert into class(card) values(floor(1+(rand()*20)));

insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));
insert into book(card) values(floor(1+(rand()*20)));

--左连接在右表建索引
alter table book add index idx_card(card);
select * from class left join book on class.card = book.card;

--右连接在左表建索引
alter table class add index idx_card(card);
select * from class right join book on class.card = book.card;


-- 三表索引优化
create table if not exists phone(
    phoneid int(10) unsigned not null auto_increment primary key,
    card int(10) unsigned not null
);
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));
insert into phone(card) values(floor(1+(rand()*20)));

explain select * from class left join book on class.card=book.card left join phone on book.card=phone.card;
alter table book add index idx_card (card);
alter table phone add index idx_card (card);

--join 优化总结：
--减少join语句的循环总次数，小结果集驱动大结果集。
--被join的字段应该保证已创建索引
--内存资源充足的情况下，可以调整joinBuffer的设置。


--索引失效总结：
--1. 全值匹配最好
--2. 最佳左前缀法则，一定要带上最左边的索引查询，中间不能断开。
--3. 不在索引列上做任何操作（计算，函数, 自动或者手动的类型转换 都会导致索引失效从而转向全表扫描。
--4. where范围条件右边的索引全部失效。
--5. 尽量select 索引列，不要使用select *.
--6. 使用！= 或者 <> 的时候无法使用索引，导致全表扫描, 在mysql8.0以上不是全表扫描ALL，而是range。
--7. is null , is not null 也无法使用索引。
--8. like以通配符开头的 %abc sql语句索引会失效变为全表扫描。
--9. 字符串不加单引号导致索引失效，见2.自动的类型转换会导致索引失效。
--10. 少用or ，可能会导致索引失效。我自己测试的时候是没有失效。

create table staffs(
    id int not null primary key auto_increment,
    name varchar(24) not null default '' comment '姓名',
    age int not null default 0 comment '年龄',
    pos varchar(20) not null default '' comment '职位',
    add_time timestamp not null default current_timestamp comment '入职时间'
)comment '员工记录表';

insert into staffs(name, age, pos) values
('z3', 22, 'manager'),
('July', 23, 'dev'),
('2000', 23, 'dev');

alter table staffs add index idx_nap(name, age, pos);

explain select * from staffs where name='July';
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+
| id | select_type | table  | partitions | type | possible_keys | key     | key_len | ref   | rows | filtered | Extra |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+
|  1 | SIMPLE      | staffs | NULL       | ref  | idx_nap       | idx_nap | 98      | const |    1 |      100 | NULL  |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+

explain select * from staffs where name='July' and age=23;

+----+-------------+--------+------------+------+---------------+---------+---------+-------------+------+----------+-------+
| id | select_type | table  | partitions | type | possible_keys | key     | key_len | ref         | rows | filtered | Extra |
+----+-------------+--------+------------+------+---------------+---------+---------+-------------+------+----------+-------+
|  1 | SIMPLE      | staffs | NULL       | ref  | idx_nap       | idx_nap | 102     | const,const |    1 |      100 | NULL  |
+----+-------------+--------+------------+------+---------------+---------+---------+-------------+------+----------+-------+

--2. 索引列 中间 断开的话 只使用到 最左边的一个索引
mysql> explain select * from staffs where name='July' and pos='dev';
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-----------------------+
| id | select_type | table  | partitions | type | possible_keys | key     | key_len | ref   | rows | filtered | Extra                 |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-----------------------+
|  1 | SIMPLE      | staffs | NULL       | ref  | idx_nap       | idx_nap | 98      | const |    1 |    33.33 | Using index condition |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-----------------------+

--3.
mysql> explain select * from staffs where name='July';
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+
| id | select_type | table  | partitions | type | possible_keys | key     | key_len | ref   | rows | filtered | Extra |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+
|  1 | SIMPLE      | staffs | NULL       | ref  | idx_nap       | idx_nap | 98      | const |    1 |      100 | NULL  |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+
1 row in set

mysql> explain select * from staffs where left(name,4)='July';
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table  | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | staffs | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    3 |      100 | Using where |
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+

--4.
explain select * from staffs where name='July' and age > 11 and pos='dev';
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+
| id | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                 |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+
|  1 | SIMPLE      | staffs | NULL       | range | idx_nap       | idx_nap | 102     | NULL |    1 |    33.33 | Using index condition |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+

explain select name, age, pos from staffs where  name='July' and age=23 and pos='dev';
+----+-------------+--------+------------+------+---------------+---------+---------+-------------------+------+----------+-------------+
| id | select_type | table  | partitions | type | possible_keys | key     | key_len | ref               | rows | filtered | Extra       |
+----+-------------+--------+------------+------+---------------+---------+---------+-------------------+------+----------+-------------+
|  1 | SIMPLE      | staffs | NULL       | ref  | idx_nap       | idx_nap | 184     | const,const,const |    1 |      100 | Using index |
+----+-------------+--------+------------+------+---------------+---------+---------+-------------------+------+----------+-------------+

explain select name, age, pos from staffs where name!='July';
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
| id | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                    |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
|  1 | SIMPLE      | staffs | NULL       | range | idx_nap       | idx_nap | 98      | NULL |    2 |      100 | Using where; Using index |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+


mysql> explain select * from staffs where name like '%July';
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table  | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | staffs | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    3 |    33.33 | Using where |
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set

mysql> explain select * from staffs where name like 'July%';
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+
| id | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                 |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+
|  1 | SIMPLE      | staffs | NULL       | range | idx_nap       | idx_nap | 98      | NULL |    1 |      100 | Using index condition |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+

--覆盖索引可以解决 百分号like匹配
mysql> explain select name, age, pos from staffs where name like '%July%';
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
| id | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                    |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
|  1 | SIMPLE      | staffs | NULL       | index | NULL          | idx_nap | 184     | NULL |    3 |    33.33 | Using where; Using index |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
1 row in set

mysql> explain select name, age, pos from staffs where name like '%July';
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
| id | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                    |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
|  1 | SIMPLE      | staffs | NULL       | index | NULL          | idx_nap | 184     | NULL |    3 |    33.33 | Using where; Using index |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
1 row in set

mysql> explain select name, age, pos from staffs where name like 'July%';
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
| id | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                    |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
|  1 | SIMPLE      | staffs | NULL       | range | idx_nap       | idx_nap | 98      | NULL |    1 |      100 | Using where; Using index |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
1 row in set

mysql> explain select * from staffs where name = 2000;
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table  | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | staffs | NULL       | ALL  | idx_nap       | NULL | NULL    | NULL |    3 |    33.33 | Using where |
+----+-------------+--------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set

mysql> explain select * from staffs where name = '2000';
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+
| id | select_type | table  | partitions | type | possible_keys | key     | key_len | ref   | rows | filtered | Extra |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+
|  1 | SIMPLE      | staffs | NULL       | ref  | idx_nap       | idx_nap | 98      | const |    1 |      100 | NULL  |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------+

mysql> explain select name, age, pos from staffs where name = 2000;
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
| id | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                    |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
|  1 | SIMPLE      | staffs | NULL       | index | idx_nap       | idx_nap | 184     | NULL |    3 |    33.33 | Using where; Using index |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+--------------------------+
1 row in set

mysql> select * from staffs;
+----+------+-----+---------+---------------------+
| id | name | age | pos     | add_time            |
+----+------+-----+---------+---------------------+
|  1 | z3   |  22 | manager | 2020-08-10 14:59:52 |
|  2 | July |  23 | dev     | 2020-08-10 14:59:52 |
|  3 | 2000 |  23 | dev     | 2020-08-10 14:59:52 |
+----+------+-----+---------+---------------------+
3 rows in set

mysql> explain select name, age, pos from staffs where name = '2000';
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------------+
| id | select_type | table  | partitions | type | possible_keys | key     | key_len | ref   | rows | filtered | Extra       |
+----+-------------+--------+------------+------+---------------+---------+---------+-------+------+----------+-------------+
|  1 | SIMPLE      | staffs | NULL       | ref  | idx_nap       | idx_nap | 98      | const |    1 |      100 | Using index |

mysql> explain select * from staffs where name='July' or name='2000';
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+
| id | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                 |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+
|  1 | SIMPLE      | staffs | NULL       | range | idx_nap       | idx_nap | 98      | NULL |    2 |      100 | Using index condition |
+----+-------------+--------+------------+-------+---------------+---------+---------+------+------+----------+-----------------------+
1 row in set
