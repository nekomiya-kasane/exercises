package com.example;

import java.io.IOException;
import java.util.Scanner;

import java.util.concurrent.ThreadLocalRandom;

/**
 * Hello world!
 *
 */
public class App2
{
    public static void main( String[] args ) throws IOException
    {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Guess the Midpoint.");
        System.out.println("Two random integers between 1 and 100 (inclusive) have been generated.");

        int min = 1, max = 100;
        int a = ThreadLocalRandom.current().nextInt(min, max + 1);
        int b = ThreadLocalRandom.current().nextInt(min, max + 1);
        if (a > b) { // swap
            int tmp = a;
            a = b;
            b = tmp;
        }
        double mid = (a + b) / 2.;

        while (true) {
            System.out.print("Enter a guess: ");
            int guess = scanner.nextInt();
            if (Math.abs(guess - mid) <= 1) { // if 'within' means endpoint excluded, change <= for <.
                System.out.println(String.format(
                        "%d is within 1 of the midpoint, which is %.1f.", guess, mid));
                break;
            }
            if (guess < a) {
                System.out.println(String.format(
                        "%d is below the two numbers.", guess));
            }
            else if (guess > b) {
                System.out.println(String.format(
                        "%d is above the two numbers.", guess));
            }
            else if (guess == b || guess == a) {
                System.out.println(String.format(
                        "%d is equal to one of the numbers.", guess));
            }
            else {
                System.out.println(String.format(
                    "%d is between the two numbers.", guess));
            }
        }

        scanner.close();
    }
}
