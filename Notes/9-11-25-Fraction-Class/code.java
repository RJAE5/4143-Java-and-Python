// In class program
// This program will computer the fib sequence n times and print out the numbers

import java.util.Scanner;
import java.util.Arrays;
public class code 
{
    public static void main(String[] args)
    {
        // User prompt and input storage 
        Scanner in = new Scanner(System.in);
        System.out.println("Please enter the nth term of the fib sequence:");
        int n = in.nextInt();

        // Input validation
        while(n <= 2)
        {
            System.out.println("Invalid number, please enter a number larger than 1:");
            n = in.nextInt();
        }

        // Start array with first two numbers
        int[] arr = new int[n];
        arr[0] = 1;
        arr[1] = 1;

        // Fill array starting at 3rd spot 
        for(int i = 2; i < n; i++)
        {
            // Add last two numbers to make the current number
            arr[i] = arr[i - 2] + arr[i - 1];
        }

        // For loop to print out array in normal way
        for(int i = 0; i < n; i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println("");


        // Alternate method to print easily and in array notation
        System.out.println(Arrays.toString(arr));





    }
}