# Pickle可以持久化Python的自定义数据类型，但是在反持久化的时候，必须能够读取到类的定义。

import pickle


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))


aa = Person("张三", 20)
# aa.show()
f = open('ex02.pkl', 'wb')
pickle.dump(aa, f)
f.close()
# del Person        # 注意这行被注释了
f = open('ex02.pkl', 'rb')
bb = pickle.load(f)
f.close()
bb.show()
