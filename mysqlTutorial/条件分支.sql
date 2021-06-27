--if(exp1, exp2, exp3)
--如果exp1为真，返回exp2， 否则返回exp3

--case 变量|表达式|字段
--when 要判断的值 then 返回的值1
--when 要判断的值 then 返回的值2
--else 返回的值3
--end
--
--case
--when 条件1 then 返回的值1
--when 条件2 then 返回的值2
--else 返回的值3
--end

--else可以省略， 如果when条件都不满足，则返回null。

--案例创建存储过程，根据传入的成绩，来显示等级， 90-100显示A， 80-90显示B,70-80显示C， 60-70显示D,否则E
delimiter $

create procedure grade(in score int)
begin
    case
        when score >=90 and score<=100 then select 'A' as level;
        when score >=80 then select 'B' as level;
        when score >=70 then select 'C' as level;
        when score >=60 then select 'D' as level;
        else select 'E' as level;
    end case;
end $

call grade(95) $


--if结构，只能在begin end中使用

create function test_if(score int) returns char
begin
    if score >=90 and score<=100 then return 'A';
    elseif score >=80 then return 'B';
    elseif score >=70 then return 'C';
    elseif score >=60 then return 'D';
    else return 'E';
    end if;
end $

select test_if(80) $

--循环结构
--    分类：
--    while loop repeat
--    循环控制：
--    iterate 类似于continue 结束本次循环开始下一次循环
--    leave 类似于break 结束当前循环

--案例： 根据次数插入admin表多条记录
create procedure pro_while(in insertNum int)
begin
    declare i int default 1;
    a: while i<=insertNum do
        insert into user5(name) values(concat('mike',i));
        set i = i+1;
    end while a;
end $

call pro_while(100) $

--案例：根据次数插入user表多条记录，如果次数>20离开
truncate user5;

create procedure pro_while1(in insertNum int)
begin
    declare i int default 1;
    b: loop
        insert into user5(id, name) values(i, concat('mike', i));
        set i = i+1;
        if i>insertNum then leave b;
        end if;
    end loop b;
end $

call pro_while1(20) $

--案例：根据次数插入user表多条记录直插入偶数id，如果次数>20离开

truncate user5;$
drop procedure pro_while2 $

create procedure pro_while2(in insertNum int)
begin
    declare i int default 0;
    c: while i<=insertNum do
        set i = i+1;
        if mod(i, 2) !=0 then iterate c;
        end if;
        insert into user5(id, name) values(i, concat('mike', i));
    end while c;
end $

call pro_while2(20) $