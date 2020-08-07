--锁的分类
--按操作分类： 1.读锁（共享锁）：针对同一份数据，多个读操作可以同时进行，不会互相影响.
--               当前写操作没有完成前，会阻塞其他写锁
--             2.写锁（排它锁）：当前写操作没有完成前，会阻塞其他读锁和写锁。

create table mylock(
    id int primary key auto_increment,
    name varchar(20)
) engine myisam;

insert into mylock(name)
values('a'),('b'),('c'),('d'),('e');

--session 1 读锁 锁住表mylock
lock table mylock read;

--查看是否锁住 mylock
show open tables;

--session 1, 2 可以查看mylock
select * from mylock;

--session 1 在没有释放锁之前 除了了读mylock，不可以做其他操作。需要释放锁才可以做其他操作。
select * from user5;
update mylock set name='a1' where id =1;

--session 2 写入mylock会被阻塞。
update mylock set name='a2' where id =1;
--session 1
unlock tables;

--表锁分析 show status like 'table%';