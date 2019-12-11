import os
import multiprocessing

def info(title):
    print(title)
    print(__name__)
    print(os.getpid())
    print(os.getppid())

if __name__ == "__main__":
    info("hello")
    p = multiprocessing.Process(target=info, args=("subprocess",))
    p.start()
    p.join() # 父进程必须等待子进程结束，才能继续执行下面的代码
    print("father process is end")
