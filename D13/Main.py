import json


def check_integer(n1, n2):
    if n1 == n2:
        return -1
    elif n1 < n2:
        return 1
    else:
        return 0


def parse_input(s1, s2):

    for e1, e2 in zip(s1, s2):
        if isinstance(e1, int) and isinstance(e2, int):
            if check_integer(e1, e2) == 1:
                return True
            elif check_integer(e1, e2) == 0:
                return False

        elif isinstance(e1, list) and isinstance(e2, list):
            if parse_input(e1, e2) is not None:
                return parse_input(e1, e2)

        else:
            if isinstance(e1, int):
                if parse_input([e1], e2) is not None:
                    return parse_input([e1], e2)
            else:
                if parse_input(e1, [e2]) is not None:
                    return parse_input(e1, [e2])

    if len(s1) < len(s2):
        return True
    elif len(s1) > len(s2):
        return False


def part1(lines):
    sumindx = 0
    curpair = 0

    for i in range(0, len(lines), 3):
        l1 = lines[i]
        l2 = lines[i + 1]
        curpair += 1

        x = json.loads(l1)
        y = json.loads(l2)

        if parse_input(x, y):
            sumindx += curpair

    print("Sum of indexes: " + str(sumindx))


def part2(lines):
    lines.append("[[2]]")
    lines.append("[[6]]")

    for line in lines:
        if line.strip() == "":
            lines.remove(line)

    for l1 in range(len(lines)):
        for l2 in range(len(lines)):
            if lines[l1] == lines[l2]:
                continue

            x = json.loads(lines[l1])
            y = json.loads(lines[l2])

            if not parse_input(x, y):
                lines[l2], lines[l1] = lines[l1], lines[l2]

    lines = lines[::-1]

    print("Decoder key: " + str((lines.index('[[6]]') + 1) * (lines.index('[[2]]') + 1)))


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    print("-" * 10 + "Part1" + "-" * 10)
    part1(lines)
    print("-"*10 + "Part2" + "-"*10)
    part2(lines)


if __name__ == '__main__':
    main()
