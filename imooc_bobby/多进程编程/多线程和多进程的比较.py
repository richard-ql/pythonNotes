import time
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor

def fib(n):
    if n<2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__=="__main__":
    with ThreadPoolExecutor(3) as excutor:
        start_time = time.time()
        all_tasks = [excutor.submit(fib, (num)) for num in range(25, 35)]
        for future in as_completed(all_tasks):
            data= future.result()
            print(f"exe result: {data}")
        print(f"last time is : {time.time()-start_time}")

    with ProcessPoolExecutor(3) as excutor:
        start_time = time.time()
        all_tasks = [excutor.submit(fib, (num)) for num in range(25, 35)]
        for future in as_completed(all_tasks):
            data= future.result()
            print(f"exe result: {data}")
        print(f"last time is : {time.time()-start_time}")

