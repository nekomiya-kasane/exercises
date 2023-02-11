package com.example;

import java.io.IOException;
import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App3
{
    public static int func(int lf, int rt, char op) {
        switch (op) {
            case '+':
                return lf + rt;
            case '-':
                return lf - rt;
            case '*':
                return lf * rt;
            case '/':
                return lf / rt;
        }
        return 0;
    }
    public static void main( String[] args ) throws IOException
    {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Please enter an integer for the size of the table: ");
        int size = scanner.nextInt();
        System.out.print("Please enter a legal operator from *, /, +, -: ");
        char op = scanner.next().charAt(0);

        String header = "  ", deli = "--";
        String[] table = new String[size];
        for (int i = 0; i < size; ++i) {
            table[i] = "";
        }
        for (int i = 1; i <= size; ++i) {
            header += String.format("%4d", i);
            table[i - 1] += String.format("%2d", i);
            for (int j = 1; j <= size; ++j) {
                table[i - 1] += String.format("%4d", func(i, j, op));
            }
            deli += "----";
        }
        System.out.println(header);
        System.out.println(deli);
        for (String row : table) {
            System.out.println(row);
        }

        scanner.close();
    }
}
