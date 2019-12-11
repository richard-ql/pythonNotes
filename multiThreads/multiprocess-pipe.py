import os
import multiprocessing

def sub_pipe(conn:multiprocessing.Pipe):
    print(os.getpid(), conn.recv())
    conn.send([1,2,3,4,5,6])



if __name__ == "__main__":
    conn_a, conn_b = multiprocessing.Pipe()
    p = multiprocessing.Process(target=sub_pipe, args=(conn_a,))
    p.start()
    conn_b.send(["a", "b", "c", "d"])
    p.join()
    print(os.getpid(), conn_b.recv())
