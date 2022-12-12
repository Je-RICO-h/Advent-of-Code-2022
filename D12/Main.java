import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;

class pair {
    public int i1, i2, v, d;

    public pair(int f, int s, int v, int d)
    {
        this.i1 = f;
        this.i2 = s;
        this.v = v;
        this.d = d;
    }
}

public class Main {

    static List<Map<Character, Integer>> findStart(List<List<Character>> matrix, boolean part2)
    {
        List<Map<Character, Integer>> mapList = new ArrayList<>();
        Map<Character, Integer> pos = new HashMap<>();

        for(int i = 0; i < matrix.size(); i++)
            for(int j = 0; j < matrix.get(i).size(); j++)
            {
                if(part2)
                {
                    if(matrix.get(i).get(j) == 'a')
                    {
                        pos.put('x',i);
                        pos.put('y',j);
                        pos.put('v', (int) 'a');

                        mapList.add(pos);

                        pos = new HashMap<Character, Integer>();
                    }
                }

                if(matrix.get(i).get(j) == 'S')
                {
                    pos.put('x',i);
                    pos.put('y',j);
                    pos.put('v', (int) 'a');

                    mapList.add(pos);

                    pos = new HashMap<Character, Integer>();
                }

                if(matrix.get(i).get(j) == 'E')
                    matrix.get(i).set(j, '{');
            }

        return mapList;
    }

    static boolean isValid(List<List<Character>> matrix, boolean vis[][], int x, int y, int val)
    {
        if (x < 0 || y < 0 || x >= matrix.size() || y >= matrix.get(0).size())
            return false;
        
        if (vis[x][y])
            return false;

        if(val == 123)
            return true;

        if((int)matrix.get(x).get(y) - val > 1)
            return false;

        return true;
    }

    static int isSolution(List<List<Character>> matrix, Map<Character, Integer> start, boolean vis[][])
    {
        int[][] dir = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

        Queue<pair> q = new LinkedList<>();

        q.add(new pair(start.get('x'), start.get('y'), start.get('v'), 0));
        vis[start.get('x')][start.get('y')] = true;

        while (!q.isEmpty()) {
            pair p = q.peek();
            int x = p.i1;
            int y = p.i2;
            int v = p.v;

            q.remove();

            for(int i = 0; i < 4; i++)
            {
                int adjx = x + dir[i][0];
                int adjy = y + dir[i][1];

                if (isValid(matrix, vis, adjx, adjy, v))
                {
                    if((int)matrix.get(adjx).get(adjy) == 123)
                        return p.d+1;

                    q.add(new pair(adjx, adjy, (int)matrix.get(adjx).get(adjy), p.d + 1));
                    vis[adjx][adjy] = true;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws FileNotFoundException {
        File f = new File("input.txt");       
        Scanner sc = new Scanner(f);

        String line;

        List<List<Character>> matrix = new ArrayList<>();

        while(sc.hasNextLine())
        {
            List<Character> row = new ArrayList<>();

            line = sc.nextLine();

            for(char c : line.toCharArray())
            {
                row.add(c);
            }

            matrix.add(row);
        }

        sc.close();

        // ? ----------------------------------------------------

        var mapList = findStart(matrix, true); //! Set False for Part 1!

        boolean[][] vis = new boolean[matrix.size()][matrix.get(0).size()];

        List<Integer> distances = new ArrayList<>();

        for(Map<Character, Integer> pos : mapList)
        {
            distances.add(isSolution(matrix, pos, vis));
            vis = new boolean[matrix.size()][matrix.get(0).size()];
        }

        distances.removeIf(s -> s == -1);

        Collections.sort(distances);

        System.out.println("Least Distance: " + distances.get(0));
    }
}
