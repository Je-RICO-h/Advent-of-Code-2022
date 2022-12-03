using System;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

namespace SampleApp
{
    class Program
    {

        //Part 1
        static char Check_Both(String s1, String s2)
        {
            foreach (char c1 in s1)
                foreach (char c2 in s2)
                {
                    if (c1 == c2)
                        return c1;
                }

            return '0';
        }
        //Part 2
        static char Check_Three(String s1, String s2, String s3)
        {
            foreach (char c1 in s1)
                foreach (char c2 in s2)
                    foreach(char c3 in s3)
                {
                    if ((c1 == c2) && (c1 == c3) && (c2 == c3))
                        return c1;
                }

            return '0';
        }

        static int Check_Alpha(char c)
        {
            if (Char.IsLower(c))
                        return (int)c - 96;
                    else
                        return (int)c - 38;
        }

        static int Part1()
        {
            String line;
            String b1, b2;
            int sum = 0;

            using (StreamReader f = new StreamReader("input.txt"))
            {
                while ((line = f.ReadLine()) != null)
                {
                    if (line.Count() % 2 == 0)
                    {
                        b1 = line[..(line.Count() / 2)];
                        b2 = line[(line.Count() / 2)..];
                    }
                    else
                    {
                        b1 = line[..(line.Count() / 2 + 1)];
                        b2 = line[((line.Count() / 2 + 1))..];
                    }

                    char c = Check_Both(b1, b2);

                    sum += Check_Alpha(c);
                }

                return sum;
            }
        }

        static int Part2()
        {
             String line, line1, line2, line3;
            int sum = 0;

            using (StreamReader f = new StreamReader("input.txt"))
            {
                while ((line = f.ReadLine()) != null)
                {
                    line1 = line;
                    line2 = f.ReadLine();
                    line3 = f.ReadLine();

                    char c = Check_Three(line1, line2, line3);

                    sum += Check_Alpha(c);
                }

                return sum;
            }
        }

        public static void Main(string[] args)
        {
           WriteLine($"Part 1 sum: {Part1()}");
           WriteLine($"Part 2 sum: {Part2()}");
        }
    }
}