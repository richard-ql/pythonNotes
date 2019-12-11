import multiprocessing

def share_value(digit: multiprocessing.Value):
    digit.value = 11.0


if __name__ == "__main__":
    num = multiprocessing.Value("d", 10.0)
    print(num.value)
    p = multiprocessing.Process(target=share_value, args=(num,))
    p.start()
    p.join()
    print(num.value)
