# example of python codes

## ex_slice.py
```
$ ./ex_slice.py
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[:5] = [1, 2, 3, 4, 5]
data[:15] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## contextlib
* [input\(\)など標準入出力が使われた処理のテストにcontextlibの関数が便利かもしれない]( https://qiita.com/podhmo/items/70a78c1429525dde0a48 )
```
$ python -m unittest ex_contextlib.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

----

## FYI

shell
```
find . -name '*.py' | sort | head -n 4
```

python
```
file_list = sorted(glob.glob('**/*.py'))[:4]
```
