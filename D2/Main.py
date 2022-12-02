DECIDE = {
        "A" : 1, #Rock
        "B" : 2, #Paper
        "C" : 3, #Scissor
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

OUTCOME = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

def check_round(x1, x2):
    if DECIDE[x1] == DECIDE[x2]:
        return 0
    elif (DECIDE[x2] == 1 and DECIDE[x1] == 3) or \
            (DECIDE[x2] == 2 and DECIDE[x1] == 1) or \
            (DECIDE[x2] == 3 and DECIDE[x1] == 2):
        return 1
    else:
        return -1

def check_round2(x1, x2):
    if DECIDE[x1] == 1:
        if OUTCOME[x2] == 0:
            return 3
        elif OUTCOME[x2] == 3:
            return 1
        else:
            return 2
    elif DECIDE[x1] == 2:
        if OUTCOME[x2] == 0:
            return 1
        elif OUTCOME[x2] == 3:
            return 2
        else:
            return 3
    else:
        if OUTCOME[x2] == 0:
            return 2
        elif OUTCOME[x2] == 3:
            return 3
        else:
            return 1

def main():

    score = 0

    with open("input.txt", "r") as f:
        for round in f:
            rounds = round.replace("\n", "").split(" ")

            if check_round(rounds[0], rounds[1]) == 1:
                score += DECIDE[rounds[1]] + 6
            elif check_round(rounds[0], rounds[1]) == 0:
                score += DECIDE[rounds[1]] + 3
            else:
                score += DECIDE[rounds[1]] + 0

    print(f"Part one score: {score}")

    #--------------Part2-------------------

    score = 0

    with open("input.txt", "r") as f:
        for round in f:
            rounds = round.replace("\n", "").split(" ")

            score += check_round2(rounds[0], rounds[1]) + OUTCOME[rounds[1]]

    print(f"Part2 score: {score}")

if __name__ == '__main__':
    main()