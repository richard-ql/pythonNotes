# docker安装gitlab

docker run -d -p 2222:22 -p 8888:80 -p 8443:443 --volume /srv/gitlab/config:/etc/gitlab --volume /srv/gitlab/logs:/var/log/gitlab --volume /srv/gitlab/data:/var/opt/gitlab --restart always --name gitlab gitlab/gitlab-ce:latest

-p 2222:22 是暴露2222 ssh端口

-p 8888:80 是暴露8888 http端口

--restart always 容器实例总是随虚拟机启动

默认用户名是root