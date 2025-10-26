/*****************************************************************************\
*
*  Author:           Rykir Evans
*  Email:            rjevans0408@my.msutexas.edu | rykirjoe@yahoo.com
*  Title:            Quadratic Formula - Java Introduction
*  Course:           CMPS 4143 Java and Python
*  Professor:        Dr. Tina Johnson
*  Semester:         Fall 2025
*
*  Description:
*         This program uses input from the user regarding the coefficients
*         of a degree 2 polynomial and uses the quadratic formula to
*         calculate the roots of said polynomial. There are handlers for the
*         cases of equal and imaginary roots as well as valid real roots.
*         
*  Usage:
*         To use this program, use some standard Java compiler and run the
*         executable. You will be prompted to enter the coefficients for
*         a degree 2 polynomial, first with A, then B, followed by C. This
*         represents the standard formula Ax^2 + Bx + C. If the coefficients
*         are valid, the program will output the roots, or declare that they
*         are imaginary. You may enter 0 for all prompts if you wish to exit.
*         
*  Files: 
*         Main.java
\******************************************************************************/

import java.util.Scanner;

public class Main 
{
    public static void main(String[] args) 
    {
        // Program output heading
        System.out.println("Rykir Evans");
        System.out.println("CMPS 4143 - Java and Python");
        System.out.println("Dr. Tina Johnson");
        System.out.println("Java Quadratic Formula Program");
        System.out.println("");

        // Prompt and input for program
        System.out.println("Please enter the coefficients to the 2nd degree polynomial");
        Scanner in = new Scanner(System.in);

        // Coefficient variable assignments
        System.out.print("Enter A: ");
        double a = in.nextDouble();

        System.out.print("Enter B: ");
        double b = in.nextDouble();

        System.out.print("Enter C: ");
        double c = in.nextDouble();

        // Early exit conditional
        // Check for dividing by zero and all zeros
        if( a == 0 || (a == 0 && b == 0 && c == 0))
        {
            System.out.println("Not a valid degree 2 polynomial, exiting the program");
        }

        else
        {
            // Performing the quadratic since a, b, and c are valid

            // Save square root of discriminant into value to save computation
            double rootDiscrim = Math.sqrt((b * b) - (4 * a * c));

            // Perform plus and minus operations to achieve roots x1 and x2
            double x1 = (-1 * b + rootDiscrim) / (2 * a);
            double x2 = (-1 * b - rootDiscrim) / (2 * a);

            // Imaginary roots conditional
            if(Double.isNaN(rootDiscrim))
            {
                System.out.println("The polynomial has imaginary roots!");
            }

            // Root with multiplicity 2 conditional
            else if (x1 == x2)
            {
                System.out.print("Root 1 = ");
                System.out.format("%.2f",x1); // Format to 2 decimal places and a new line
                System.out.print(" (Multiplicity 2)\n");
            }

            // Final valid and separate roots conditional
            else
            {
                System.out.print("Root 1 => ");
                System.out.format("%.2f%n",x1); // Format to 2 decimal places and a new line

                System.out.print("Root 2 => ");
                System.out.format("%.2f%n",x2); // Format to 2 decimal places and a new line
            }

        }// end primary else block
    }// end main
}// end Main