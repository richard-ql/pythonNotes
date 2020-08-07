--存储过程：一组预先编译好的sql语句的集合

delimiter $
create procedure myp1()
begin
    insert into user5(id, name)
    values(1,'jack'),(2, 'rose'), (3,'tom');
end $

--调用procedure：  call myp2() $

create procedure myp2(in beautyname varchar(20))
begin
    select bo.*
    from boys bo
    right join beauty b on bo.id = b.boyfriend_id
    where b.name=beautyname;
end $

call myp2('Liuyan') $

create procedure myp3(in beautyName varchar(20), out boyName varchar(20))
begin
    select bo.boyName into boyName
    from boys as bo
    inner join beauty b on bo.id=b.boyfriend_id
    where b.name = beautyName;
end $

call myp3('xiaozhao', @boyName)$


create procedure myp4(inout a int, inout b int)
begin
    set a = a*2;
    set b = b*2;
end $

set @m = 10 $
set @n = 20 $
call myp4(@m, @n)$
select @m, @n $

--删除存储过程
drop procedure myp1;

--查看存储过程
show create procedure myp1；