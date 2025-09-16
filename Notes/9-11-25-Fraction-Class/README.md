## Java and Python Notes
### 9-9-2025 (Coding Day)

Today started out by coding a simple fibonacci program and I got to presnt my program which was cool. 

#### Object-Oriented Programming in Java
Similar concept to C++:
* Encapsulation
* Inheritance
* Polymorphism

Remember a class is different from an instance of that class. 

Note that in Java, we cannot overloading operators, which results in awkward functions needed for different arithmetic.
> This was his personal choice because he didn't like how people abused it in C++.

**More Defs**
State: Current st of values of the object

Methods: Operate on objects; may change state; and state may affect behavior

Inheritance in Java: a class 'extends' another class. It has all of the properties and methods of class extended and new methods and data fields that apply to new class.

Mutator & Accessor Methods: Methods that change and read data respectively
> aka 'Setters' & 'Getters'

#### Using Existing Classes
Example: `Math`
* Only encapsulates methods, no data
* Do NOT construct an instance of class `Math`

Example: `Date`
* Construct them specifying initial state using `new`, then apply methods
* Without `new`, it won't work as intended because this class uses pointers to objects
* This contrasts with C++ in the sense that it does not use pointer notation.

#### Java Semantics
Pointers in Java are implicit, meaning they are not specified, they just happen. Additionally, garbage collection is automatically handled. 

Class creation in Java does not end with a semi-colon.

Multiple source files are all saved with the `.java` file type. You save other classes, but the MUST be `public`, and import them like regular and just run the main class file


Constructors have the same name as the class. Classes can have more than one constructor, and they may take zero, one or more parameters. A constructor has no return value.

**Difference:** Constructors in java are called with the `new` operator.

#### Fields
Final instance fields must be set before end of constructor andi s never changed again using the `final` keyword.
`private final String name;`

Static fields (class fields) are where only one such field per class, shared among all instances of the class.
`private static int nextID = 1;`

#### Code
The rest of lecture was spent cloding the [Fraction Class](./fraction.java) so refer to that for extra examples of default/parameterized constructor and other class items.



