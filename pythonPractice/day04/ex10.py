"""
上下文管理器对象存在的目的是管理 with 语句
with 语句的目的是简化 try/finally 模式。这种模式用于保证一段代
码运行完毕后执行某项操作，即便那段代码由于异常、return 语句或
sys.exit() 调用而中止，也会执行指定的操作。finally 子句中的代
码通常用于释放重要的资源，或者还原临时变更的状态。

上下文管理器协议包含 __enter__ 和 __exit__ 两个方法。with 语句
开始运行时，会在上下文管理器对象上调用 __enter__ 方法。with 语
句运行结束后，会在上下文管理器对象上调用 __exit__ 方法，以此扮
演 finally 子句的角色。
"""

with open("text01.py", encoding="utf-8") as fp:
    src = fp.read(120)


# print(src)
print(fp)
print(fp.closed, fp.encoding)
print(fp.read(60))
