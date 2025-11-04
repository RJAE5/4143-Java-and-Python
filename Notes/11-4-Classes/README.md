## Java and Python Notes
### 11-4-2025 Python Classes

#### Why use classes?
* Structure large programs
* Reuse and extend code
* Group related data and functions
* Improve readability and maintainability

In Python, you use the keyword `class` followed by the name.

The `__init__` method is the constructor that initializes an object when it is created.

Creating an instance is just calling the name of the class.

Class attributes store data, methods define behavior.

In the methods of a class, the first parameter is always the `self` object.
```py
class Point:
    def __init__(self, x = 1, y = 2):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

Python OOP supports inheritance and operator overloading

