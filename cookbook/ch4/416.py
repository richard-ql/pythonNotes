import sys


with open('somefile.txt', encoding='utf-8') as f:
    for i in iter(lambda :f.read(10), ''):
        # sys.stdout.write(i)
        print(i, end='\n')
        