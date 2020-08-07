import hashlib

md5 = hashlib.md5()
md5.update(b"asdfasasdfsdf")
print(md5.hexdigest())

md5.update("我爱中国".encode(encoding='utf-8'))
print(md5.hexdigest())