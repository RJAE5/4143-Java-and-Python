## Java and Python Notes
### 9-9-2025 (Coding Day)

Today was primarily coding some basic programs in class. Please review [code.java](./code.java) for all of the programs we did today. 

Some things worth noting that I discovered today:
* String equality does not work with `==`, instead you must use `stringName.equals(otherString)` (Program 3)
* If your scanner reads in numbers prior to reading in a string, a new line character will get stuck in the buffer, and can simply be cleared by doing `scannerName.nextLine();` prior to what you need to read to clear the buffer. (Program 3)
* To calculate a non-integer number through division, the constituate numbers must be floats or doubles (Program 4)
    * For example `int x1, x2;` and `double x3 = x1/x2` will always be an integer regardless if the actual division yield an integer or not, but with `.0` concatinated.