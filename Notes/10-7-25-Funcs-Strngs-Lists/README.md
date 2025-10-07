## Java and Python Notes
### 10-2-2025 Functions, Strings, and Lists

### Functions

Indentation is key for functions (and Python as a whole), as it defines the code block.

you begin a function with the `def` keyword, followed by the name of the function, with parameters in the parenthesis, and the beginning line must end with a colon `:`.

```py
def Repeat_lyrics(x):
    for i in range(x):
        print_lyrics()  # Note that you can call other functions from a function
```

As with the rest of Python, you do not need to declare which variable type will be needed in the parameters, but if there is a variable mismatch, it will happen inside the body of the function.

For functions that return values, they must end with the keyword `return`.

A fruitful function uses a return statement, and a non-fruitful function essentially means it is a void function.

Recursion is a feature for Python functions
```py
def countdown(n):
    # Base Case
    if n <= 0:
        print("Blastoff!")
    # Recursive call
    else:
        print(n)        # Having this before the call is important
        countdown(n-1)  # If reversed, it would print backwards

countdown(10)
```

### Strings
A string is a sequence of characters, there really is no character type.

In Python, strings have several built in functions:
1.  `stringName.len()` -> Returns the length of a string
2. `stringName[x:y]` -> Returns a slice of the string starting at index `x` and ending at `y`
> If you want to start at 0 or end at the last index, you can omit the respective bound: `s[:5]` or `s[4:]`
3. `stringName.upper()` -> converts all letters to uppercase
4. `stringName1 in stringName2` -> returns a bool to see if the entirety of `stringName1` occurs in `stringName2`

Strings in Python are immutable, meaning you cannot change a character within it. You can use string slicing to essentially change the string
```py
greeting = "helli"
greeting = greeting[0:4] + 'o'
print(greeting)
```

### Lists
While a string is a sequence of characters, a List is a sequence of values of varying types.

Lists use the square bracket notation:
```py
mixedList = [1, "abc", [5, 7]]
```
> Lists can contain other lists

A handy trick is that you can easily print the last item of a list using the index `-1`
```py
print(mixedList[-1])
```

You can traverse lists the same way you can traverse an array.

There are tons of list operations in Python, but some common ones are:
1. `list1 + list2` -> concatenates `list2` onto the end of `list1`
2. `listName[x:y]` -> List slices similar to strings
3. `listName.append(element)` -> Adds a single element to the end of a list
4. `listName.pop(index)` -> returns the value at a given index, or the last element if no index is provided
5. `listName.remove(x)` -> removes an element, or even a full slice, helpful if you don't know the index but know the element

Most List operations return void, so do not try to assign a list to the output of a list operation. The method operates on the list as is.

Several operations only work if the list contains the same type of elements.

**A List is mutable**, you can change individual elements of it, unlike a string.

#### Programs
```py
def nested_sum(t):
    sum = 0
    #t is a list of lists
    for i in range(len(t)):
        for j in range(len(t[i])):
            sum += t[i][j]
    return sum

rah = [[1,2],[3],[4,5,6],[7],[8,9]]

print(nested_sum(rah))

def middle(r):
    return r[1:len(r)-1]

har = [1,2,3,4]
newHar = middle(har)
print(newHar)
            
```