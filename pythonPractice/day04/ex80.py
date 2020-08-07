t1 = [1, [1, 2, 3], (4, 5, 6)]
t2 = list(t1)
t3 = t1[:]

import copy

t4 = copy.deepcopy(t1)
t1[1].append(9)
print(t1)
print(t4)
print(t2)
print(t3)
