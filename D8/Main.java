import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main
{
    static int check_4_scores(List<List<Integer>> m, int i, int j)
    {
        int up = i-1; 
        int down = i+1;
        int left = j-1; 
        int right = j+1;

        int upscore = 0;
        int downscore = 0;
        int leftscore = 0;
        int rightscore = 0;

        while(up != -1) // Check up
        {
            if(m.get(i).get(j) <= m.get(up).get(j))
            {
                upscore++;
                break;
            }
            up--;
            upscore++;
        }

        while(down != m.size()) // Check down
        {
            if(m.get(i).get(j) <= m.get(down).get(j))
            {
                downscore++;
                break;
            }
            down++;
            downscore++;
        }

        while(left != -1) // Check left
        {
            if(m.get(i).get(j) <= m.get(i).get(left))
            {
                leftscore++;
                break;
            }
            left--;
            leftscore++;
        }

        while(right != m.get(i).size()) // Check right
        {
            if(m.get(i).get(j) <= m.get(i).get(right))
            {
                rightscore++;
                break;
            }
            right++;
            rightscore++;
        }

        return upscore * leftscore * downscore * rightscore;
    }

    static boolean check_4_sides(List<List<Integer>> m, int i, int j)
    {
        int up = i-1; 
        int down = i+1;
        int left = j-1; 
        int right = j+1;

        boolean u_vis = true;
        boolean d_vis = true;
        boolean r_vis = true;
        boolean l_vis = true;

        while(up != -1) // Check up
        {
            if(m.get(i).get(j) <= m.get(up).get(j))
            {
                u_vis = false;
                break;
            }
            up--;
        }

        while(down != m.size()) // Check down
        {
            if(m.get(i).get(j) <= m.get(down).get(j))
            {
                d_vis = false;
                break;
            }
            down++;
        }

        while(left != -1) // Check left
        {
            if(m.get(i).get(j) <= m.get(i).get(left))
            {
                l_vis = false;
                break;
            }
            left--;
        }

        while(right != m.get(i).size()) // Check right
        {
            if(m.get(i).get(j) <= m.get(i).get(right))
            {
                r_vis = false;
                break;
            }
            right++;
        }

        if(u_vis || d_vis || r_vis || l_vis)
            return true;
        else
            return false;
    }

    public static void main(String[] args) throws FileNotFoundException{

        File f = new File("input.txt");
        Scanner sc = new Scanner(f);

        List<List<Integer>> m = new ArrayList<>();
        String line;

        while(sc.hasNextLine())
        {
            line = sc.nextLine();
            m.add(new ArrayList<Integer>());

            for(char c : line.toCharArray())
                m.get(m.size()-1).add(Integer.parseInt(Character.toString(c)));
        }

        sc.close();

        int count = 0;
        int maxscore = 0;
        int currentScore = 0;

        for(int i = 0; i < m.size(); i++)
            for(int j = 0; j < m.get(i).size(); j++)
            {
                if(check_4_sides(m, i, j))
                    count++;  

                currentScore = check_4_scores(m, i, j);

                if(maxscore < currentScore)
                    maxscore = currentScore;              
            }

        System.out.println("Visible Trees: " + count);
        System.out.println("Highest scenic score: " + maxscore);
    }
}