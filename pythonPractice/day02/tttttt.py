def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.capitalize(), end=' ')


if __name__ == "__main__":
    main()
