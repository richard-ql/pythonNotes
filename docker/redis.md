# docker 安装redis

docker search redis

docker pull redis

docker run -d -p 6379:6379 -v
/usr/local/etc/redis/redis.conf:/usr/local/etc/redis/redis.conf -v
/var/data:/data --name dht-redis redis redis-server
/usr/local/etc/redis/redis.conf --appendonly yes