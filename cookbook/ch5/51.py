import sys

print(sys.getdefaultencoding())

with open('somefile.txt', 'rt', encoding='utf-8') as fp:
    f = fp.read()
    print(f)


# with open('somefile.txt', 'rt', encoding='utf-8') as fp:
#     for line in fp:
#         print(line)
#
# text1 = "hello world"
# text2 = "nihaoshijie"
# with open('somefile.txt', 'wt', encoding='utf-8') as fp:
#     fp.write(text1+'\n')
#     fp.write(text2+'\n')

with open('somefile.txt', 'at', encoding='utf-8') as fp:
    fp.write('disanhangle\n')
