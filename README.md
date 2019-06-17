# example of python codes

## ex_slice.py
```
$ ./ex_slice.py
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[:5] = [1, 2, 3, 4, 5]
data[:15] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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
