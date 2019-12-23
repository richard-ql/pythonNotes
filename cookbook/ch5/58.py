from functools import partial

RECORD_SIZE = 32

with open('somefile.txt', 'rt', encoding='utf-8') as f:
    lines = iter(partial(f.read, RECORD_SIZE), '')
    for line in lines:
        print(line)
