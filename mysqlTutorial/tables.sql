--mysql> select * from course;
--+-------+-----------------+-----+
--| cno   | cname           | tno |
--+-------+-----------------+-----+
--| 3-105 | 计算机导论      | 825 |
--| 3-245 | 操作系统        | 804 |
--| 6-166 | 数字电路        | 856 |
--| 9-888 | 高等数学        | 831 |
--+-------+-----------------+-----+
--
--mysql> select * from score;
--+-----+-------+--------+
--| sno | cno   | degree |
--+-----+-------+--------+
--| 103 | 3-105 |     92 |
--| 103 | 3-245 |     86 |
--| 103 | 6-166 |     85 |
--| 105 | 3-105 |     88 |
--| 105 | 3-245 |     75 |
--| 105 | 6-166 |     79 |
--| 109 | 3-105 |     76 |
--| 109 | 3-245 |     68 |
--| 109 | 6-166 |     81 |
--+-----+-------+--------+
--
--mysql> select * from student;
--+-----+-----------+------+---------------------+-------+
--| sno | sname     | ssex | sbirthday           | class |
--+-----+-----------+------+---------------------+-------+
--| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
--| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
--| 103 | 王丽      | 女   | 1976-01-23 00:00:00 | 95033 |
--| 104 | 李军      | 男   | 1976-02-20 00:00:00 | 95033 |
--| 105 | 王芳      | 女   | 1975-02-10 00:00:00 | 95031 |
--| 106 | 陆军      | 男   | 1974-06-03 00:00:00 | 95031 |
--| 107 | 王尼玛    | 男   | 1976-02-20 00:00:00 | 95033 |
--| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
--| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
--+-----+-----------+------+---------------------+-------+
--
--mysql> select * from teacher;
--+-----+--------+------+---------------------+-----------+-----------------+
--| tno | tname  | tsex | tbirthday           | prof      | depart          |
--+-----+--------+------+---------------------+-----------+-----------------+
--| 804 | 李诚   | 男   | 1958-12-02 00:00:00 | 副教授    | 计算机系        |
--| 825 | 王萍   | 女   | 1972-05-05 00:00:00 | 助教      | 计算机系        |
--| 831 | 刘冰   | 女   | 1977-08-14 00:00:00 | 助教      | 电子工程系      |
--| 856 | 张旭   | 男   | 1969-03-12 00:00:00 | 讲师      | 电子工程系      |
--+-----+--------+------+---------------------+-----------+-----------------+