package com.example;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final ByteArrayOutputStream errContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    private final PrintStream originalErr = System.err;

    @Before
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @After
    public void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }

    public static boolean compare_array(long[] A, long[] B) {
        if (A.length != B.length) {
            return false;
        }
        for (int i = 0; i < A.length; ++i) {
            if (A[i] != B[i]) {
                return false;
            }
        }
        return true;
    }

    /**
     * Rigorous Test :-)
     */
    @Test
    public void Q1Test_1() {
        long[] res = com.example.App1.get_partition(125);
        long[] expected = { 1, 1, 0, 0, 0 };

        assertTrue(compare_array(res, expected));
    }

    @Test
    public void Q1Test_2() {
        long[] res = com.example.App1.get_partition(987);
        long[] expected = { 9, 3, 1, 0, 2 };

        assertTrue(compare_array(res, expected));
    }

    @Test
    public void Q4Test() {
        App4.main(null);

        String tar1 = "0        1         2\n" +
                "12345678901234567890\n" +
                "X                  X\n" +
                " X                X \n" +
                "  X              X  \n" +
                "   X            X   \n" +
                "    X          X    \n" +
                "     X        X     \n" +
                "      X      X      \n" +
                "       X    X       \n" +
                "        X  X        \n" +
                "         XX         \n";
        String tar2 = "0        1         2\r\n" +
                "12345678901234567890\r\n" +
                "X                  X\r\n" +
                " X                X \r\n" +
                "  X              X  \r\n" +
                "   X            X   \r\n" +
                "    X          X    \r\n" +
                "     X        X     \r\n" +
                "      X      X      \r\n" +
                "       X    X       \r\n" +
                "        X  X        \r\n" +
                "         XX         \r\n";

        String res = outContent.toString();
        assertTrue(res.equals(tar1) || res.equals(tar2));
    }
}
