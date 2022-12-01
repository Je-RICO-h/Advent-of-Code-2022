import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //? "--Part 1--"

        try {
            File f = new File("input.txt");
            Scanner sc = new Scanner(f);

            List<Integer> ls = new ArrayList<>();

            int sum = 0;
            String line;

            while (sc.hasNextLine())
            {
                line = sc.nextLine();

                if(line.isEmpty())
                {
                    ls.add(sum);
                    sum = 0;
                }
                else
                    sum += Integer.parseInt(line);
            }

            sc.close();

            System.out.println("The top elf carrying the most: ");
            System.out.print(Collections.max(ls) + "\n");

            //? --- PART 2 ---

            sum = 0;

            Collections.sort(ls);

            System.out.println("Top 3 elves with most food total: ");

            for(int i = ls.size() - 1; i > ls.size() - 4; i--)
                sum += ls.get(i);
            
            System.out.print(sum + "\n");
                

        } 
        catch (FileNotFoundException e) 
        {
            System.out.println("File not found!");
            System.exit(1);
        }
    }
}