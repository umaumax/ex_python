#!/usr/bin/env python3
import difflib
a = '''
abc
def
ghi
hello
'''
b = '''
abc
ddf
ghi
world
'''
list_a = a.splitlines()
list_b = b.splitlines()
list_a = list(map(lambda l: l + '\n', list_a))
list_b = list(map(lambda l: l + '\n', list_b))
print('# input data')
print(list_a)  # ['', 'abc', 'def', 'ghi' ]
print(list_b)  # ['', 'abc', 'ddf', 'ghi' ]
print()

print("# NG")
for line in difflib.unified_diff(a, b):
    print(line, end='')
print()

print("# NG")
for line in difflib.unified_diff('\n'.join(list_a), '\n'.join(list_b)):
    print(line, end='')
print()

print("# OK")
# NOTE: 各listの要素は改行コードを含むことが前提
# これは，openしたファイルに対して，readlines()した結果に対して，処理を行うことを想定?
for line in difflib.unified_diff(list_a, list_b):
    print(line, end='')
