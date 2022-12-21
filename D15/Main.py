def manhattan(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def readinput():
    sc = []
    bc = []

    with open("input.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "")
            parts = line.split(" ")

            sx = int(parts[2].replace("x=", "").replace(",", ""))
            sy = int(parts[3].replace("y=", "").replace(":", ""))
            bx = int(parts[-2].replace("x=", "").replace(",", ""))
            by = int(parts[-1].replace("y=", ""))

            sc.append((sx, sy, manhattan(sx, bx, sy, by)))
            bc.append((bx, by))

    return sc, bc


def check(s, b, x, y):
    for sx, sy, d in s:
        if manhattan(x, sx, y, sy) <= d and (x, y) not in b:
            return True
    return False


def part1(s, b):
    count = 0
    y = 2_000_000
    for x in range(min(x - d for x, sy, d in s), max(x + d for x, sy, d in s)):
        if check(s, b, x, y) and (x, y) not in b:
            count += 1

    return count


def part2(s, b):
    dirs = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
    for sx, sy, d in s:
        for dx in range(d + 2):

            dy = (d + 1) - dx

            for multx, multy in dirs:
                x, y = sx + (dx * multx), sy + (dy * multy)

                if not(0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                    continue

                if not check(s, b, x, y):
                    return x * 4_000_000 + y


def main():
    sensor, beacons = readinput()
    print("Part1: ", part1(sensor, beacons))
    print("Part2: ", part2(sensor, beacons))


if __name__ == '__main__':
    main()
