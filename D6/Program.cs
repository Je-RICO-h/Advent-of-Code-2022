using System;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

namespace SampleApp
{
    class Program
    {
        static int counter(String data, int tracer_end)
        {
            int tracer_begin = 0;

            while (tracer_end != data.Count())
            {
                bool is_unique = true;

                foreach (char c in data[tracer_begin..tracer_end])
                {
                    int char_count = data[tracer_begin..tracer_end].ToCharArray().Count(c2 => c2 == c);

                    if (char_count != 1)
                    {
                        is_unique = false;
                        break;
                    }
                }

                if (is_unique)
                    return tracer_end;
                else
                {
                    tracer_begin++;
                    tracer_end++;
                }
            }

            return -1;
        }

        public static void Main(string[] args)
        {
            StreamReader fr = new StreamReader("input.txt");

            String data;

            data = fr.ReadToEnd();

            fr.Close();

            WriteLine("Part1: " + counter(data, 4));
            WriteLine("Part2: " + counter(data, 14));
        }
    }
}