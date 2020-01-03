# docker 安装mysql

+ docker pull mysql

## 一般来说数据库容器不需要建立目录映射

sudo docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql
–nam：容器名，此处命名为mysql
-e：配置信息，此处配置mysql的root用户的登陆密码
-p：端口映射，此处映射 主机3306端口 到 容器的3306端口
-d：源镜像名，此处为 mysql

## 如果要建立目录映射
sudo docker run -p 3306:3306 --name spider-mysql \
-v /usr/local/docker/mysql/conf:/etc/mysql \
-v /usr/local/docker/mysql/logs:/var/log/mysql \
-v /usr/local/docker/mysql/data:/var/lib/mysql \
-v /usr/local/docker/mysql/mysql-files:/var/lib/mysql-files \
-e MYSQL_ROOT_PASSWORD=123456 \
-d mysql


-v：主机和容器的目录映射关系，":"前为主机目录，之后为容器目录

## 进入docker本地连接mysql客户端

sudo docker exec -it mysql bash
mysql -uroot -p123456

## 使用 Navicat 远程连接mysql

## 如果你的容器运行正常，但是无法访问到MySQL，一般有以下几个可能的原因：

1.防火墙阻拦

# 开放端口：
$ systemctl status firewalld
$ firewall-cmd  --zone=public --add-port=3306/tcp -permanent
$ firewall-cmd  --reload
# 关闭防火墙：
$ sudo systemctl stop firewalld


## navicat连接MySQL报错1130

需要进入docker本地客户端设置远程访问账号

$ sudo docker exec -it mysql bash
$ mysql -uroot -p123456
mysql> grant all privileges on *.* to root@'%' identified by "password";
原理：

# mysql使用mysql数据库中的user表来管理权限，修改user表就可以修改权限（只有root账号可以修改）

mysql> use mysql;
Database changed

mysql> select 'host' from user where user='root';
mysql> update user set host = '%' where user ='root';
mysql> flush privileges;
mysql> select 'host'   from user where user='root';

## navicat连接MySQL报错1251

+ mysql8 之前的版本中加密规则是mysql_native_password,而在mysql8之后,加密规则是caching_sha2_password,
解决问题方法有两种,一种是升级navicat驱动,一种是把mysql用户登录密码加密规则还原成mysql_native_password.
由于用的是破解版的navicat，所以只能用第二种方法解决了.

1. ALTER USER 'root'@'%' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER;
2. ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码';
3. FLUSH PRIVILEGES;

## 参考资料[https://www.jianshu.com/p/49f7e46cf4c6]
