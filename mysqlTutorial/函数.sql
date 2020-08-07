--函数：有且仅有一个返回值

SET GLOBAL log_bin_trust_function_creators = 1
delimiter $

create function myf1() returns int
begin
    declare c int default 0;
    set c = c*2;
    return c;
end $

select myf1() $

--查看函数
show create function myf1 $