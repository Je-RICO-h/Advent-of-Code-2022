counters = {
    "part1" : 0,
    "part2" : 0
}

def Part2(elf1, elf2):
    for x in elf1:
        if x in elf2:
            counters["part2"] += 1
            return

    for y in elf2:
        if y in elf1:
            counters["part2"] += 1
            return

def Part1():
    with open("input.txt","r") as f:
        for line in f:
            parts = line.replace("\n","").split(",")

            f1,t1 = parts[0].split("-")
            f2,t2 = parts[1].split("-")

            elf1 = set(range(int(f1),int(t1)+1))
            elf2 = set(range(int(f2),int(t2)+1))

            Part2(elf1, elf2) # Part 2

            if elf1.issubset(elf2) or elf2.issubset(elf1):
                counters["part1"] += 1

def main():
    Part1() # Part 2 is inside of Part1 for optimization

    print(f"Part1: {counters['part1']} \nPart2: {counters['part2']}")


if __name__ == '__main__':
    main()