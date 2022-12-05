import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main
{
    static List<String> s1 = new ArrayList<>(List.of("D","M","S","Z","R","F","W","N"));
    static List<String> s2 = new ArrayList<>(List.of("W","P","Q","G","S"));
    static List<String> s3 = new ArrayList<>(List.of("W","R","V","Q","F","N","J","C"));
    static List<String> s4 = new ArrayList<>(List.of("F","Z","P","C","G","D","L"));
    static List<String> s5 = new ArrayList<>(List.of("T","P","S"));
    static List<String> s6 = new ArrayList<>(List.of("H","D","F","W","R","L"));
    static List<String> s7 = new ArrayList<>(List.of("Z","N","D","C"));
    static List<String> s8 = new ArrayList<>(List.of("W","N","R","F","V","S","J","Q"));
    static List<String> s9 = new ArrayList<>(List.of("R","M","S","G","Z","W","V"));

    static List<List<String>> stacks = new ArrayList<>(List.of(s1,s2,s3,s4,s5,s6,s7,s8,s9));

    static void change_order(int q, int f, int t)
    {
        for(int i = 0; i < q; i++)
        {
            String elem = stacks.get(f-1).get(stacks.get(f-1).size()-1);
            stacks.get(f-1).remove(stacks.get(f-1).size()-1);
            stacks.get(t-1).add(elem);
        }
    }

    static void change_order2(int q, int f, int t)
    {
        List<String> aux_stack = new ArrayList<>();

        for(int i = 0; i < q; i++)
        {
            String elem = stacks.get(f-1).get(stacks.get(f-1).size()-1);
            aux_stack.add(elem);
            stacks.get(f-1).remove(stacks.get(f-1).size()-1);
        }

        for(int i = aux_stack.size() - 1; i >= 0; i--)
        {
            stacks.get(t-1).add(aux_stack.get(i));
            aux_stack.remove(i);
        }
    }

    public static void main(String[] args) throws FileNotFoundException{

        File f = new File("input.txt");

        Scanner sc = new Scanner(f);

        for(int i = 0; i < 10; i++)
           sc.nextLine();
        
        while(sc.hasNextLine())
        {
            String[] order = sc.nextLine().split(" ");
            //change_order(Integer.parseInt(order[1]), Integer.parseInt(order[3]), Integer.parseInt(order[5])); //!Part1
            change_order2(Integer.parseInt(order[1]), Integer.parseInt(order[3]), Integer.parseInt(order[5])); //!Part2

        }

        sc.close();

        String output = "";

        for(int i = 0; i < 9; i++)
           output += stacks.get(i).get(stacks.get(i).size()-1);

        System.out.println("Output : " + output);
    }
}