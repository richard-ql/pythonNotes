import inspect

# 不使用模块inspect，仅使用内置函数，也能实现自省和反射的功能。
# 自省意味着获取对象的属性和方法；反射通过字符串映射的方式获取
# 或者修改对象的方法或者属性（比如以某个属性的名字字符串作为参
# 数传入某个函数），是自省的一种具体实现方法。python中相关功能
# 的内置函数如下：

# dir(obj)->将对象的所有属性、方法以列表形式返回
# hasattr(obj,name_str)->判断objec是否有name_str这个方法或者属性
# getattr(obj,name_str)->获取object对象中与name_str同名的方法或者函数
# setattr(obj,name_str,value)->为object对象设置一个以name_str为名的value方法或者属性
# delattr(obj,name_str)->删除object对象中的name_str方法或者属性

# 但是使用inspect.getmembers(obj)这个方法能够获取到更详尽的自省信息，且可读性更佳，
# 下面将其和dir内置函数进行比较：

def foo(a:int, b:str) ->int:
    return a + int(b)

print(dir(foo))
print(inspect.getmembers(foo))

# 2.更高的类型检查
# 我们知道可以使用type(),isinstance()等内置函数进行类型检查，
# 常用于基本数据类型或者对象实例的class判别，比如:
# type(1)==int #比较数据类型
# isinstance(cat,Cat) #比较对象实例是否属于某个类
# 但如果要进行更"元"一点的类型比较呢？比如判断一个对象是否为一个模组，
# 一个内置函数，一个生成器，甚至一个 await 表达式：
print(inspect.ismodule(inspect))    # 检查 inspect 是否为模组
print(inspect.ismethod(inspect))    # 检查 inspect 是否为对象方法
print(inspect.isfunction(len))      # 检查 len 是否为函数
print(inspect.isbuiltin(len))       # 检查 len 是否为内置函数
print(inspect.isgenerator(inspect)) # 检查 inspect 是否为生成器
print(inspect.isawaitable(inspect)) # 检查 inspect 是否可用于 await 表达式
