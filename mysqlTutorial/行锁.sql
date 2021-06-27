create table test_innodb_lock(
    id int,
    val varchar(20)
) engine=innodb;

insert into test_innodb_lock(id, val)
values(1, '100'), (2, '200'),(3, '300'),(4, '400'),(5, '500'),(6, '600');

create index test_innodb_lock_id on test_innodb_lock(id);
create index test_innodb_lock_val on test_innodb_lock(val);


--行锁转表锁的场景， 当update val=300 val列无索引,系统会自动将300转成char类型，但是带来的危害就是此时
--行锁会转换成表锁，造成系统性能的下降。

--间隙锁， 当时用范围条件检索数据，innodb会把范围之内不存在的索引也加上行锁，导致其他终端正好操作
--此行时会阻塞。

--如何手动锁定一行

begin;
update test_innodb_lock set val='1000' where id=6 for udpate;
commit;

--查看行锁
show status like 'innodb_row_lock%';
