import os

print("hello world")

pid = os.fork()

print("多进程会拷贝os.fork之后的代码")

print(pid)

if pid == 0:
    print("son process")
else:
    print("father process")
