import dis


def add_list():
    li1 = list(range(3))
    li2 = li1
    li2 += [3]
    return li1, li2


def add_list2():
    li1 = list(range(3))
    li2 = li1
    li2 = li2 + [3]
    return li1, li2


if __name__ == "__main__":
    print(add_list())
    print("--------")
    print(add_list2())
    print(dis.dis(add_list))
    # print(dis.dis(add_list2))
