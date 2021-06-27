create database dept_join;

create table tbl_dept(
    id int(11) primary key auto_increment,
    deptName varchar(30) default null,
    locAdd varchar(40) default null
);

create table tbl_emp(
    id int(11) primary key auto_increment,
    name varchar(20) default null,
    deptId int(11) not null,
    key fk_dept_id (deptId)
);
--    constraint 'fk_dept_id' foreign key(deptId) references tbl_dept(id)

insert into tbl_dept(deptName, locAdd) values
('RD', '11'), ('HR', '12'),('MK', '13'), ('MIS', '14'),('FD', '15');

insert into tbl_emp(name, deptId) values
('z3', 1), ('z4', 1), ('z5', 1), ('w5', 2),('w6', 2),('s7', 3),('s8', 4),('s9', 51);

--1. inner join
select * from tbl_emp inner join tbl_dept on tbl_emp.deptId=tbl_dept.id;
--2. left join
select * from tbl_dept left join tbl_emp on tbl_emp.deptId=tbl_dept.id;
--3 right join
select * from tbl_dept right join tbl_emp on tbl_emp.deptId=tbl_dept.id;
--4 full join
select * from tbl_dept left join tbl_emp on tbl_emp.deptId=tbl_dept.id
union
select * from tbl_dept right join tbl_emp on tbl_emp.deptId=tbl_dept.id;
--5
select * from tbl_dept left join tbl_emp on tbl_emp.deptId=tbl_dept.id where tbl_emp.deptId is null;
--6
select * from tbl_dept right join tbl_emp on tbl_emp.deptId=tbl_dept.id where tbl_dept.id is null;
--7
select * from tbl_dept left join tbl_emp on tbl_emp.deptId=tbl_dept.id where tbl_emp.deptId is null
union
select * from tbl_dept right join tbl_emp on tbl_emp.deptId=tbl_dept.id where tbl_dept.id is null;