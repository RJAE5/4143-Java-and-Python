## Java and Python Notes
### 9-2-2025 (Arrays)

An array is an Abstract Data Type
* The array type has a set of values
* The array type has a set of operations that can be applied uniformly to each of these values

The array is most often held in sequential storage locations. Each component of the array has a fixed, unique index, and the size of the array is constant.

In C++ and Java, the array indices must be integers.

In some other languages, array indices may be other discrete data types like Pascal and Ada.

The lower bound in C++ and Java may be 0, but can be 1 (Fortran) or chosen by the programmer (Pascal, Ada).

Bounds in Java can also be undefined.

For Java, you can "fake" multidimensional arrays by maintaining an array of arrays.

In most languages, arrays are homogeneous (all components must have the same type). In some languages, the components may be heterogeneous (of varying types).

#### Operations
Java has whole array operations like clone and equality tests

Arrays may carry additional information about themselves, such as type and length, as seen in Java.
* The terms reflective and non-reflective, respectively refer to these two types of arrays.
    * This is not standard terminology, with other uses of the terms.

#### Java Array Standards
Array indicies are integers
* The bracket notation a[i] is used

Arrays are objects. They are allocated by `new`, manipulated by reference, and garbage collected
`int a[] = new int[100];`

Arrays are reflective (Array properties are known). `a.length` is the length of array `a`

```
for(int i = 0; i < a.length; i++)
    System.out.println(a[i]);
```

For visualization, imagine a pointer pointing to an array with an index for class tag, size, and then the rest of the array.

#### Copying Arrays
For copying, you must be careful, you cannot use the assignment operator willy nilly, that just creates an alias.

```
int [] luckyNumbers;
System.arraycopy(smallPrimes, 0, luckyNumbers, 0, smallPrimes.length);
```
> The format is `System.arraycopy(fromObject, fromIndex, toObject, toIndex, count);`

OR

```
int [] copiedLuckyNumbers = Arrays.copyOf(luckyNumbers, luckyNumbers.length);
```

#### Sorting Arrays
```
Arrays.sort(smallPrimes);
```
This is a variation of quickSort, it's nice because it's built in.

#### SubArrays
A subarray is a consecutive portion of the array
> (She skipped this slide really quickly)

#### 2D Arrays
`int x[][];` denotes an array `x` of *array* components, each of which is an array of *integer* components

#### Ragged (Nonrectangular) Arrays
```
int ragged[][] = new int[4][];

// Create the ragged structure
for(int i = 0; i < 0; i++)
{
    ragged[i] = new int[i+1];
}

// Fill each cell with a value
for(int i = 0; i < 4; i++)
{
    for(int j = 0; i < ragged[j].length; j++)
    {
        ragged[i][j] = 10 * i + j;
    }
}
```
> This creates a lower triangular 4x4 matrix with multiples of 11 along the main diagnol, multiples of 10

#### Inserting & Deleting
To insert or to delete elements from an array are very slow because to keep the same order, you must shift the element down or up depending on the operation, and either losing an element or having a null index.

#### FOREACH Repitition
```
for (int index : array)
{//something}
```
This creates the iterator `index` and will go through each element of `array`.
> This exists in C++ as well

#### Conclusion
Arrays have the following advantages:
* Accessing an element by its index is very fast (constant time)

Arrays have the following disadvantages:
* All elements must be of the same type
* The array size is fixed and can never be changed
* Insertion/deletions *into ordered* arrays is very slow