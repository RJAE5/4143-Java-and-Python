// In class program
// This java class is used for fraction arithmetic

import java.util.Scanner;
import java.util.Arrays;
public class fraction
{
    public static void main(String[] args)
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

            // Setter
            public void setNum(int n)
            {
                this.num = n;
            }

            public float getDecVal()
            {
                float fn = this.num;
                float fd = this.den;
                return fn / fd;
            }


        }

        Frac f1 = new Frac(1, 2);
        System.out.println(f1.getDecVal());
    }
}