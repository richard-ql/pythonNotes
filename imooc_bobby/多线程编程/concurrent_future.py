import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED

def get_html(times):
    time.sleep(times)
    print(f"get page {times}")
    return times

excutor = ThreadPoolExecutor(max_workers=2)
# # 通过submit 提交函数到线程池，submit是立即返回
# task1 = excutor.submit(get_html, (3))
# task2 = excutor.submit(get_html, (2))
#
# # done方法是立即返回
# print(task1.done())
# # 正在执行或者已经执行完的任务无法cancel
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
# print(task1.result())

# 获取已经执行成功的task的返回
# 方法一
# urls = [2, 3, 4]
# all_tasks = [excutor.submit(get_html, (url)) for url in urls]
# for future in as_completed(all_tasks):
#     data = future.result()
#     print(f"get {data} page")
# 方法二
# urls = [2,3,4]
# for data in excutor.map(get_html, urls):
#     print(f"get {data} pgae")

# wait 用法
urls = [2, 3, 4]
all_tasks = [excutor.submit(get_html, (url)) for url in urls]
wait(all_tasks, return_when=FIRST_COMPLETED)
print("主线程")
