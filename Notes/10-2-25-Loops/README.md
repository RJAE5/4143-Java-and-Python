## Java and Python Notes
### 10-2-2025 Python Loops

Loops are fairly different syntax-wise from other languages.

An example for a while loop:
```py
x = 1
while x <= 5:
    print(x)
    x = x + 1
```
Notice the colon at the end of the conditional and the indentation of the block statements.

In this example, `x` is a *"loop control variable"*.

A *counter* is a variable that increments by a set amount each iteration

An *accumulator* is a variable that increases by a dynamic amount depending on the iteration.

A *sentinel* is a value in a list that indicates the end of the list. It must be distinct from anything that could be a valid value.

#### The range() Function
The function `range()` has 3 parameters:
1. if `range(n)` is called, it will iterate from 0 up to n-1, but it still iterates `n` times
2. If `range(begin, end)` is called, it will start at `begin` and go up to `end`-1
3. If `range(start, stop, step)` is called, it will begin at `start`, go up to `stop`-1, but increment by `step` each time

#### See code for Examples