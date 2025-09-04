## Java and Python Notes
### 9-4-2025 (Methods)

#### The Block
The method body is Java code enclosed within a block `{ }`. Additionally, curly braces include the same statements as seen in main methods.

Sometimes, the term "messages" are used to describe method calls. Method bodies have access to parameters, and hence, methods are general enough to be reused with many different somethings.

#### Return Statements
All non-void methods must return a value. The type of the value is defined in the method heading. Java's return statement is exactly the same as C++: `return expression;`

#### Example
```java
public static void evenOdd(int num)
{
    if(num % 2 == 0)
        System.out.println(num + " is even");
    else
        System.out.println(num + " is odd");
}
```

Here, the keyword `static` is used for memory management. Static methods cannot be overriden. This is good for utility functions, such as I/O or math operations.

#### Summaray
* Method headings provide information on usage. 
* The block is where your algorithm gets implemented. 
* The parameters are accessible within the block. 
* Methods should return a value of the correct type. 
* Methods should be fully tested.

#### Detailed Example
```java
import java.util.Arrays;

public static void printArr()
{
    for(int i = 0; i < this.length; i++)
        System.out.print(this[i] + " ");

    System.out.println("\n");
}
```
> The above currently does not work.