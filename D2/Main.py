PART1 = { # Every Posibility
    ("A","X") : 4,
    ("A","Y") : 8,
    ("A","Z") : 3,
    ("B","X") : 1,
    ("B","Y") : 5,
    ("B","Z") : 9,
    ("C","X") : 7,
    ("C","Y") : 2,
    ("C","Z") : 6
}

PART2 = { # Every Posibility
    ("X","A") : 3,
    ("X","B") : 1,
    ("X","C") : 2,
    ("Y","A") : 4,
    ("Y","B") : 5,
    ("Y","C") : 6,
    ("Z","A") : 8,
    ("Z","B") : 9,
    ("Z","C") : 7
}

def main():

    score = 0

    with open("input.txt", "r") as f:
        for round in f:
            r = round.replace("\n", "").split(" ")
            score += PART1[(r[0], r[1])]

    print(f"Part one score: {score}")

    #--------------Part2-------------------

    score = 0

    with open("input.txt", "r") as f:
        for round in f:
            r = round.replace("\n", "").split(" ")
            score += PART2[(r[1], r[0])]

    print(f"Part2 score: {score}")

if __name__ == '__main__':
    main()