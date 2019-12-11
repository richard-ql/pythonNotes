# from itertools import dropwhile
#
# with open('somefile.txt', encoding='utf-8') as f:
#     for line in dropwhile(lambda line: line.startswith('#'), f):
#         print(line, end="")


from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]

for i in islice(items, 3, None):
    print(i)
