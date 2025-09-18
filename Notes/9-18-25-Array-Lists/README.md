## Java and Python Notes
### 9-18-2025 Array Lists (Quiz Day)

#### Array Reminders
* Can set size at run time (Same as C++)
* Does not completely resolve problem of dynamically modifying arrays, that is, once the size is set, it cannot change easily.

#### Introducing Array Lists
Array Lists are similar to C++ vectors, as you can resize them dynammically. Defined in the `java.util` package. The lower bound is 0.



**Add method**
`.add()` will append an element to the end of the array list.

When it gets full, it can automatically create a bigger array and copies objects in the smaller array to the bigger array.

**Size method**
`.size()` returns the number of elements in the array list, not the actual length.

`.trimToSize()` will automatically reduce the array list to the minimum size to hold all elements. This is used when you know it has reached its maximum size and you can save.

**Element Method**
`.set(i, 81)` Automatically sets the ith element to the number `81`

`.get(i)` Automatically gets the ith element.