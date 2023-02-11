package com.example;

/**
 * Hello world!
 *
 */
public class App4
{
    public static void main( String[] args )
    {
        System.out.println("0        1         2");
        System.out.println("12345678901234567890");

        String row = "                    ";
        for (int i = 0; i < 10; ++i) {
            String ln = row;
            StringBuffer sb = new StringBuffer(ln);
            sb.setCharAt(i, 'X');
            sb.setCharAt(20 - i - 1, 'X');
            ln = sb.toString();
            System.out.println(ln);
        }
    }
}
