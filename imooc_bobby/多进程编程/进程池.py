import time
import multiprocessing

def get_html(n):
    time.sleep(n)
    print("subprocess run")
    return n

if __name__=="__main__":
    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    # # 方法一
    # result = pool.apply_async(get_html, args=(3,))
    #
    # # 等待所有任务完成
    # pool.close()
    # # pool.join 之前需要关闭进程池
    # pool.join()
    # print(result.ge)

    # 方法二 imap

    for result in pool.imap(get_html, [1, 5, 3]):
        print(f"{result} sleep")

    for result in pool.imap_unordered(get_html, [1,5,3]):
        print(f"{result} sleep")
