import inspect

t2 = __import__("getmembers_01")
result = inspect.getmembers(t2,inspect.isclass)
result2 = inspect.getmembers(t2,inspect.isfunction)
result3 = inspect.getmembers(t2,inspect.ismodule)
result4 = inspect.getmembers(t2,inspect.ismethod)
result5 = inspect.getmembers(t2,inspect.isgeneratorfunction)
result6 = inspect.getmembers(t2,inspect.isbuiltin)
print("1:"+ str(result))
print("2:"+ str(result2))
print("3:"+ str(result3))
print("4:"+ str(result4))
print("5:"+ str(result5))
print("6:"+ str(result6))