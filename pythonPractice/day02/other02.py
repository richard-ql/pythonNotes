"""
    私有属性和方法
"""


class Person:
    __nick_name = "qinl"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def nick_name(cls):
        return cls.__nick_name

    def __play(self):
        if self.__age < 19:
            print("正在玩飞行旗")
        else:
            print("正在斗地主")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade

    def lesson(self, course):
        print('%s的%s正在学习%s.' % (self.__grade, self.nick_name, course))


def main():
    p1 = Person("ql", 20)
    print(p1._Person__name)
    p1._Person__play()


def main1():
    p1 = Person("ql", 20)
    print(p1.__name)
    p1.__play()


def main3():
    p1 = Person("ql", 20)
    s1 = Student("wang", 16, "初三")
    s1.lesson("数学")
    # print(Person.nick_name)


if __name__ == "__main__":
    main3()
