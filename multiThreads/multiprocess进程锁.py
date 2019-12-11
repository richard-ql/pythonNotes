import time
import multiprocessing

def show_data(lock, index):
    with lock:
        time.sleep(2)
        print(index)

if __name__ == "__main__":
    lock = multiprocessing.RLock()
    for i in range(10):
        multiprocessing.Process(target=show_data, args=(lock, i)).start()
