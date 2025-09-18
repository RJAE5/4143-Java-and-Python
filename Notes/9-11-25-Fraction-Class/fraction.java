// In class program
// This java class is used for fraction arithmetic

import java.util.Scanner;
import java.util.Arrays;
public class fraction
{
    public static class Frac
    {
        private int num;
        private int den;

        // Default constructor
        public Frac()
        {
            this.num = 1;
            this.den = 1;
        }

        // Parameterized Constructor
        public Frac(int n, int d)
        {
            this.num = n;
            this.den = d;
        }

        // Copy Constructor
        public Frac(Frac f1)
        {
            this.num = f1.num;
            this.den = f1.den;
        }

        // Setter
        public void setNum(int n)
        {this.num = n;}

        public void setDen(int d)
        {this.den = d;}

        public int getNum()
        {return this.num;}

        public int getDen()
        {return this.den;}

        public float getDecVal()
        {return this.num / this.den;}

        public Frac multiply(Frac f1)
        {
            return new Frac(this.num * f1.num, this.den * f1.den);
        }

        public Frac add(Frac f1)
        {
            Frac temp = new Frac();
            temp.den = this.den * f1.den;
            temp.num = this.num * f1.den + f1.num * this.den;
            return temp;
            
        }

        public Frac divide(Frac f1)
        {
            Frac temp = new Frac();
            temp.num = this.num * f1.den;
            temp.den = this.den * f1.num;
            return temp;
        }

        public void printFrac()
        {
            System.out.print(this.num);
            System.out.print("/");
            System.out.print(this.den);
            System.out.println();
        }

        

    }

    public static void main(String[] args)
    {
        Frac f1 = new Frac(4, 2);
        Frac f2 = new Frac(2, 3);
        Frac f3 = f2.multiply(f1);
        Frac f4 = f1.add(f2);
        Frac f5 = f1.divide(f2);

        f1.printFrac();
        f2.printFrac();
        f3.printFrac();
        f4.printFrac();
        f5.printFrac();
        
    }
}