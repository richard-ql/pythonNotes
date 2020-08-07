--索引是一种数据结构mysql的索引是BTree，所以优势是 检索 和 排序，where 和 order by。
--索引本身也很大，不可能全部存储在内存种，因此索引往往以索引文件的形式存储在磁盘上。

--索引的分类：
--1.单值索引，即一个索引只包含一个列，一个表可以有多个单值索引。
--2.唯一索引，索引的值必须唯一，但允许有空值。
--3.复合索引，即索引包含多个列。
--
--mysql索引结构：
--1.BTree索引
--2.Hash索引
--3.full-text索引
--4.RTree索引

--性能分析
--explain sql语句；
--执行计划包含的信息
--a)id 数字越大越先执行
--b) select_type:
            --    1. SIMPLE 最简单的select查询，查询中不包含子查询或者union
            --    2. PRIMARY 包含子部分的情况下，最外层被标记为primary
            --    3.SUBQUERY 在select或者where中有子查询
            --    4.DERIVED 在from语句中包含的的子查询被标记为DERIVED，mysql会递归这些子查询将结果保存在临时表中。
            --    5. UNION 若第二个select出现在UNION之后，则被标记为UNION。
            --    6. UNION RESULT 从UNION表获取结果的select。
            mysql> explain select * from tbl_dept left join tbl_emp on tbl_emp.deptId=tbl_dept.id where tbl_emp.deptId is null
            union
            select * from tbl_dept right join tbl_emp on tbl_emp.deptId=tbl_dept.id where tbl_dept.id is null;
            +------+--------------+------------+------------+------+---------------+------+---------+------+------+----------+--------------------------------------------------------+
            | id   | select_type  | table      | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra                                                  |
            +------+--------------+------------+------------+------+---------------+------+---------+------+------+----------+--------------------------------------------------------+
            |    1 | PRIMARY      | tbl_dept   | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    5 |      100 | NULL                                                   |
            |    1 | PRIMARY      | tbl_emp    | NULL       | ALL  | fk_dept_id    | NULL | NULL    | NULL |    8 |     12.5 | Using where; Not exists; Using join buffer (hash join) |
            |    2 | UNION        | tbl_emp    | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    8 |      100 | NULL                                                   |
            |    2 | UNION        | tbl_dept   | NULL       | ALL  | PRIMARY       | NULL | NULL    | NULL |    5 |       20 | Using where; Not exists; Using join buffer (hash join) |
            | NULL | UNION RESULT | <union1,2> | NULL       | ALL  | NULL          | NULL | NULL    | NULL | NULL | NULL     | Using temporary                                        |
            +------+--------------+------------+------------+------+---------------+------+---------+------+------+----------+--------------------------------------------------------+
            5 rows in set
-- c)type 访问类型，是较为重要的一个指标，从好到坏以次为：
        -- system > const >eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery> index_subquery> range > index > all
        -- system > const> eq_ref > ref > range > index > ALL
        -- 一般来说，至少保证查询能达到range，最好能到ref。
-- d)possible_keys:
        -- 显示可能在这张表上使用到的索引，一个或者多个，但实际查询不一定会使用。
-- e)key:
        -- 查询实际上使用的索引，如果为null，则没有使用索引。
        -- 查询中若使用了覆盖所以，则该索引仅出现在key列表中。
-- f)key_len: 同等精度的查询，key_len越短越好。
-- g)ref： 显示索引的那一列被使用，如果可能的话，是一个常数。哪些列或常量被用于查找索引列上的值。
-- h) rows: 此表有多少行被优化器查询。
-- i) extra: 不适合在其他列显示，但是十分重要的额外信息。
        --1.Using filesort: 使用文件排序，即没有使用到索引排序，需要优化。
        --2.Using temporary：使用了临时表保存中间结果。常见于order by 和 group by
        --3.Using index: 表示相应的select操作中使用了覆盖索引，避免访问表的数据行，效率不错！
            --如果同时出现using where，索引被用做执行索引键的查找。
            --覆盖索引：select的数据只用从索引就能获取，不必读取数据行。换句话说，查询的列要被
            --所建的索引覆盖。