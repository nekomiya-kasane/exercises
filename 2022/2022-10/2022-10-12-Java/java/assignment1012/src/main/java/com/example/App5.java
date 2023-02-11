package com.example;

import java.io.IOException;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.Scanner;

import java.util.concurrent.ThreadLocalRandom;
import java.util.function.Function;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;


class Record {
    public String name;
    public Integer grade;
}

/**
 * Hello world!
 *
 */
public class App5
{
    public static void main( String[] args ) throws IOException
    {
        //String base = new File("").getAbsolutePath();
        //System.out.println("Dir: " + base);
        
        File file = new File("students-grades.txt");
        if (args.length != 0 || !file.exists() || !file.isFile()) {
            file = new File(args[0]);
            if (!file.exists() || !file.isFile()) {
                System.out.println("Invalid file.");
                System.exit(-1);
            }
        }
        
        ArrayList<Record> records = new ArrayList<Record>();

        try {
            InputStreamReader reader = new InputStreamReader(new FileInputStream(file));
            BufferedReader buffer = new BufferedReader(reader);

            String line;
            while ((line = buffer.readLine()) != null) {
                if (line.trim() == "") {
                    continue;
                }
                String item[] = line.split(" ");
                if (item.length < 2) {
                    System.out.println("Bad record: " + line + ". Ignored");
                    continue;
                }

                Record record = new Record();
                record.name = item[0];
                record.grade = Integer.parseInt(item[1]);

                records.add(record);
            }

            reader.close();
        } catch (Exception e) {
            System.out.println("Reading failed.");
            e.printStackTrace();
        }

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a minimum grade out of 100: ");
        Integer min = scanner.nextInt();

        Integer total = records.size();
        records.removeIf(rec -> (rec.grade < min));

        String line1 = String.format("The following %d students had a grade of %d or higher:", records.size(), min);
        String line2 = "";
        if (records.size() != 0) {
            line2 += Stringify(records.get(0));
            for (int i = 1; i < records.size(); ++i) {
                line2 += ", " + Stringify(records.get(i));
            }
            line2 += ".";
        }
        String line3 = String.format(
            "There were %d students below %d, for a total of %d students.",
                total - records.size(), min, total);

        System.out.println(line1);
        System.out.println(line2);
        System.out.println(line3);

        scanner.close();
    }

    public static String Stringify(Record record) {
        String res = record.name + " ";
        res += String.format("(%d)", record.grade);
        return res;
    }
}
