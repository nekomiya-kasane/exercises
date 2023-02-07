package com.example;

import java.io.IOException;
import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App1 
{
    public static void main( String[] args ) throws IOException
    {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Input the amount of money: ");
        double dollars = scanner.nextDouble();
        long[] parts = get_partition(Math.round(dollars * 100));

        print_result(dollars, parts);

        scanner.close();
    }

    public static long[] get_partition(long value) {
        long parts[] = { 0, 0, 0, 0, 0 };
        for (int i = 0; i < denominations.length; ++i) {
            parts[i] = value / denominations[i];
            value = value % denominations[i];
        }

        return parts;
    }

    public static void print_result(double dollars, long[] parts) {
        String out = String.format(
            "The amount $%.2f consists of " + 
            "%d dollar(s), %d quarter(s), %d dime(s), %d nickel(s), and %d pennies.",
                dollars, parts[0], parts[1], parts[2], parts[3], parts[4]);
        System.out.println(out);
    }
    
    public static final long denominations[] = { 100, 25, 10, 5, 1 };
}
