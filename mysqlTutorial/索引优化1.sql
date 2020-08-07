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
--被join的字段应该保证以创建索引
--内存资源充足的情况下，可以调整joinBuffer的设置。