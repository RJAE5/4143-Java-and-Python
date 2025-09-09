// In class program
// This program will classify a number as positive/negative, odd/even, or zero

import java.util.Scanner;
public class code 
{
    public static void main(String[] args)
    {
        // Initial heading
        System.out.println("Rykir Evans");
        System.out.println("Program 1:");
        System.out.println("This program will classify a number \n");

        // Input functionality
        int num;
        Scanner in = new Scanner(System.in);        

        // Prompt and storage
        System.out.println("Please enter an integer number: ");
        num = in.nextInt();

        // Classification using if/else
        if(num == 0)
        {
            System.out.println("The number is 0!");
        }
        else 
        {
            if(num > 0)
            {System.out.print("The number is positive and ");}
            else
            {System.out.print("The number is negative and ");}

            if(num % 2 == 0)
            {System.out.println("even!");}
            else
            {System.out.println("odd!");}
        }
        System.out.println("\n");


        // Initial heading for program 2
        System.out.println("Rykir Evans");
        System.out.println("Program 2:");
        System.out.println("This program will print the square of 1 to N \n");

        // Prompt and storage
        System.out.println("Please enter an integer number: ");
        num = in.nextInt();

        // Table header
        System.out.println("X          X^2");
        for(int i = 1; i <= num; i++)
        {
            // Output of number and its square
            System.out.println(i + "          " + i*i);
        }
        System.out.println('\n');

        // Initial heading for program 3
        System.out.println("Rykir Evans");
        System.out.println("Program 3:");
        System.out.println("This program will print an appropriate response if first name is same as last name \n");

        // Prompt and storage
        String fname, lname;
        System.out.println("Please enter your first name:");
        in.nextLine(); // Consume new line character to clear buffer
        fname = in.nextLine();

        System.out.println("Please enter your last name:");
        lname = in.nextLine();

        // Response generation
        if(fname.equalsIgnoreCase(lname))
        {System.out.println("WHAT?!?! Your first name is the same as your last?");}
        else
        {System.out.println("Nice to meet you, " + fname + " " + lname);}
        System.out.println('\n');

        // Initial heading for program 4
        System.out.println("Rykir Evans");
        System.out.println("Program 4:");
        System.out.println("This program will let you know how many slices of pizza each person in a party will get, assuming 8 slices per pizza \n");

        double people, pizzas;
    
        // Prompt and storage
        System.out.println("Please enter the number of people coming to your party:");
        people = in.nextInt();

        System.out.println("Please enter the number of pizzas being bought for your party:");
        pizzas = in.nextInt();

        // Mild input validation to avoid division by 0
        if(people == 0 || pizzas == 0)
        {System.out.println("Thats a depressing party");}
        else
        {
            // Variable calculation for pizzas per person
            double ppp = (pizzas * 8) / people;

            // Initial statement with formatting to have an integer number for slices
            System.out.print("Each person will have at least ");
            System.out.format("%.0f", Math.floor(ppp));
            System.out.print(" slice(s) of pizza");

            // If slices is a non-integer, notify that there will be some left over
            if(ppp - Math.floor(ppp) > 0)
            {System.out.print(" with some leftover!\n");}
            else
            {System.out.print("!\n");}
        }
    }
}
