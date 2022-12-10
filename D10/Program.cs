using System;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

namespace SampleApp
{
    public class Program
    {
        static int x = 1;
        static int x2 = 1;
        static int sum = 0;
        static int cycle = 0;
        static int cycle2 = 0;

        static string[,] display = new string[6, 41];
        static int cursorx = 0;
        static int cursory = 1;

        static int check_cycle(int x, int cycle)
        {
            var cycles = new List<int> { 20, 60, 100, 140, 180, 220 };

            if (cycles.Contains(cycle))
                return x * cycle;

            return 0;
        }

        static void CPU(string line)
        {
            var parts = line.Split(" ");
            int to, adder = 0;

            if (parts[0] == "noop")
                to = 1;
            else
            {
                to = 2;
                adder = int.Parse(parts[1]);
            }

            for (int i = 0; i < to; i++)
            {
                cycle++;
                sum += check_cycle(x, cycle);
            }

            x += adder;
        }

        static void CRT(string line)
        {
            if (cursorx == 5 && cursory == 40)
                return;

            var parts = line.Split(" ");
            int to, adder = 0;

            if (parts[0] == "noop")
                to = 1;
            else
            {
                to = 2;
                adder = int.Parse(parts[1]);
            }

            for (int i = 0; i < to; i++)
            {
                cycle2++;
                if (cycle2 % 40 == 0)
                {
                    cursorx++;
                    cursory = 0;
                    cycle2 = 0;
                }

                if (cycle2 == x2 || cycle2 == x2 + 1 || cycle2 == x2 + 2)
                    display[cursorx, cursory] = "#";
                else
                    display[cursorx, cursory] = ".";

                cursory++;
            }

            x2 += adder;
        }

        public static void Main(string[] args)
        {
            var f = new StreamReader("input.txt");
            String line;

            while (f.Peek() >= 0)
            {
                line = f.ReadLine();

                line.Trim();

                CPU(line);
                CRT(line);

            }

            f.Close();

            WriteLine($"Total: {sum}");

            WriteLine($"-----------------------");

            for (int i = 0; i < 6; i++)
            {
                WriteLine("");
                for (int j = 0; j < 40; j++)
                {
                    if (j == 0)
                        continue;

                    Write(display[i, j]);
                }
            }
        }
    }
}