## Java and Python Notes
### 9-30-2025 Python introduction

Python was invented by Guido van Rossum in late 1980's in the Netherlands.

It was created as a general-purpose, high-level language intended to be straightforward to read and write.

Python supports OOP, imperative *and* functional programming.

Python is a dynamically typed language with automatic memory management, that is **interpreted**, not compiled.

#### Modern History
Early Python was a descendant of ABC that would appeal to UNIX/C programmers.

Python 2.0 released in 2000 and had major new features:
* Garbage collector
* Support for Unicode

Python 3.0 released in 2008 was major, and backwards-incompatible.

#### Surface Semantics and Syntax
* Types are similar to C++.
* Common reserved words are also similar.
    * Exception to `else if` becoming `elif`
* Operators are also mostly similar.
* Type declarations are not necessary, it is implied. 
    * Casting becomes a lot more important due to this.
* Comments are done with `#`
* Input is handled by the `input()` function which always returns a string
    * You can put a prompt a parameter in the `input()` function that will be displayed.
* Boolean expressions are similar to C++ with minor exceptions
    * The first letter of `True` and `False` are capital.
    * And/or/not operators are spelled out ane not symbols.
* Indentation is crucial in python, determining seperate code blocks
* Python has short circuiting, with expressions evaluated left-to-right
* No switch statement in Python

#### See code file for examples