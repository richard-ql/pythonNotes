import os

num = 100

pid = os.fork()

if pid == 0:
    num += 100
    print("son ", num)
else:
    num += 1000
    print("father ", num)
