import math


def automate_split(ref_list, li, char, pos):
    elem = li.strip().split(char)

    if pos == "1":
        ref_list.append(elem[1])
    else:
        ref_list.append(elem[len(elem) - 1])

    return ref_list


def refine_data(data):
    monkey, rounds = {}, {}

    i = 0
    monkey[i] = []
    rounds[i] = 0

    for d in data:
        if d == "\n":
            i += 1
            monkey[i] = []
            rounds[i] = 0
        else:
            monkey[i].append(d)

    # ---------------------------------

    for k in monkey:
        refined_list = []

        for l in monkey[k]:
            splitter = " "
            pos = "1"

            if "Operation" in l:
                splitter = "="
            elif "Starting items" in l:
                splitter = ":"

            if "Test:" in l or "If" in l:
                pos = "final"

            refined_list = automate_split(refined_list, l, splitter, pos)

        refined_list.pop(0)

        for i in range(len(refined_list)):
            refined_list[i] = refined_list[i].replace(" ", "")

        refined_list[0] = [int(x) for x in refined_list[0].split(",")]

        monkey[k] = refined_list

    return monkey, rounds


def lcm_calc(monkey):
    lcm = 1
    for k in monkey.keys():
        lcm = math.lcm(lcm, int(monkey[k][2]))

    return lcm


def monkey_playing(monkey, m_b, rounds, lcm_num):
    round_c = 1

    while round_c != rounds + 1:
        for k in monkey:
            while len(monkey[k][0]) != 0:

                old = monkey[k][0].pop(0)
                m_b[k] = m_b[k] + 1

                new = eval(monkey[k][1])

                if lcm_num == 0:
                    new //= 3
                else:
                    new %= lcm_num

                if new % int(monkey[k][2]) == 0:
                    monkey[int(monkey[k][3])][0].append(new)
                else:
                    monkey[int(monkey[k][4])][0].append(new)

        round_c += 1

    return m_b


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    monkey, monkey_business = refine_data(data)

    lcm_num = lcm_calc(monkey)

    #monkey_business = monkey_playing(monkey, monkey_business, 20, 0) # Part 1
    monkey_business = monkey_playing(monkey, monkey_business, 10000, lcm_num) # Part 2

    for k in monkey_business:
        print(f"Monkey {k} did {monkey_business[k]} inspection")

    print(" ")

    monkey_business = dict(sorted(monkey_business.items(), key=lambda item: item[1]))

    print("-" * 25)

    print(f"Prod of the 2 monkey: {monkey_business[list(monkey_business)[-1]] * monkey_business[list(monkey_business)[-2]]}")


if __name__ == '__main__':
    main()
