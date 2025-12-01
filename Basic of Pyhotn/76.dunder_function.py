# The word dunder is Python slang for d = double and under = underscore (__), so:
#dunder function is a function (or method) in Python whose name starts and ends with two underscores.

#These are some special function that give some special built in behaviors to the objects

"""

|   Dunder method          | When Python calls it                     | Example                |
| ------------------------ | ---------------------------------------- | ---------------------- |
| `__init__`               | When creating a new object               | `obj = MyClass()`      |
| `__str__`                | When converting to string                | `print(obj)`           |
| `__len__`                | When using len(obj)                      | `len(my_list)`         |
| `__getitem__`            | When indexing/slicing                    | `my_list[0]`           |
| `__call__`               | When calling an instance like a function | `obj()`                |
| `__enter__` & `__exit__` | Context managers                         | `with open(...) as f:` |
| '__add__'                |Power operator overloading                |                        |
| '__eq__'                 |Power operator overloading                |                        |
|'__new__                  |Control object lifecycle                  |                        |
|'__del__                  |Control object lifecycle                  |                        |
|--------------------------|------------------------------------------|------------------------|

"""