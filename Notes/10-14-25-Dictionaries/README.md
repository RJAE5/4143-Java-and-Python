## Java and Python Notes
### 10-14-2025 Python Dictionaries

#### Definitions
A dictionary is more general than a list, the indices do not have to be integer, practically every type can be.

A dictionary is a mapping between keys and a set of values. Key-value pairs are sometimes called items.

Note: You cannot have multiple keys map to one value, but you can have a key map to multiple values.

#### Creation
Dictionaries can be created using the `dict()` function or by using `{}`

To add items, you must have square bracket notation `[]`

```py
eng2sp['one'] = "uno"
```

#### Access
You can access the key-value pair by checking the key.

Dictionaries have the `get()` method that takes a key and default value which searches the dictionary and returns the value if found, returns the default value if not.

You can iterate through a dictionary just like an array

```py
def print_items(d):
    for c in d:
        print(c, d[c])
```

the `keys()` method returns a *list* of all keys, and conversely, the `values()` methods returns a *list* of all values.

The `items()` function returns a list of all KV pairs (items).

#### Reverse-Lookup
Sometimes you want to find a value's key, this is not a built-in function, but it is possible to create:

```py
def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return l
    return ValueError('Value not found')
```

However, it is important to remember there might be two keys with the same value.

#### Exceptions
Lists cannot be keys in a dictionary, but they can be values. This is due to the need for keys to be hashable, which lists are not since they are mutable.