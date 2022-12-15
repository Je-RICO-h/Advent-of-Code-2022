def input():
    rocks = set({})
    lowest = 10
    with open("input.txt", "r") as f:
        for line in f:
            xy = line.replace(" ", "").replace("\n", "").split("->")

            for i in range(len(xy) - 1):
                x1, y1 = xy[i].split(",")
                x2, y2 = xy[i + 1].split(",")
                x1, y1 = int(x1), int(y1)
                x2, y2 = int(x2), int(y2)

                maxx, minx = max(x1, x2), min(x1, x2)
                maxy, miny = max(y1, y2), min(y1, y2)

                if maxx == minx:
                    for j in range(miny, maxy + 1):
                        rocks.add((x1, j))
                        if j > lowest:
                            lowest = j
                else:
                    for j in range(minx, maxx + 1):
                        rocks.add((j, y1))

    return rocks, lowest


def simulation(rocks, lowest):
    sands = set()
    void = True
    part1cont = False
    part1answ = 0

    while void:
        x, y = 500, 0

        while True:
            if y > lowest:
                if not part1cont:
                    part1answ = len(sands)
                    part1cont = True
                sands.add((x, y))
                break
            if (x, y + 1) not in rocks and (x, y + 1) not in sands:
                y = y + 1
                continue
            if (x - 1, y + 1) not in rocks and (x - 1, y + 1) not in sands:
                y = y + 1
                x = x - 1
                continue
            if (x + 1, y + 1) not in rocks and (x + 1, y + 1) not in sands:
                y = y + 1
                x = x + 1
                continue

            sands.add((x, y))

            if (x, y) == (500, 0):
                void = False
                break
            break

    return len(sands), part1answ


def main():
    rocks, lowest = input()
    part2answ, part1answ = simulation(rocks, lowest)
    print(f"Part1: {part1answ}")
    print(f"Part2: {part2answ}")


if __name__ == '__main__':
    main()
