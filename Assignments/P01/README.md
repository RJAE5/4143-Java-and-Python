## P01 - Java Quadratic Formula Program
### Rykir Evans
### Description:

This program introduces us to the Java Programming Language via the implementation of a quadratic polynomial solver. The program prompts the user to enter the coefficients `A`, `B`, and `C` for the traditional degree 2 polynomial of the form `Ax^2 + Bx + C.`. The quadratic formula is used to solve the degree 2 polynomial and formatting is used to ensure the roots are displayed using 2 decimal places.

Additionally, the program is capable of handling various errors that might arise when entering coefficients. For instance, if the user enters `0` for `A`, the program will not execute the formula as this would result in dividing by zero. Another example is the case of imaginary roots. A handler will indicate the roots are imaginary. Finally, if the roots are equal, a handler will only output one root and indicate `(Multiplicity 2)`.

The program ends after one iteration and must be executed again to perform another root calculation.

### Usage
For WSL, the following instructions may be used to run the program:
1. Navigate to the directory of the program
2. Use the javac compiler* along with the program name `javac Main.java`
3. Run the program using `java Main`
4. Follow the program prompts to determine the root(s) of the quadratic.

*If you have not installed the javac compiler, you may do so following these steps:
1. Ensure you are using WSL
2. Use `sudo apt install openjdk-17-jdk`
3. Verify installation with `java -version`