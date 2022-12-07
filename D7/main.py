from collections import OrderedDict

def part12():
    cwd = ""
    dirsize = {}

    with open("input.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "")

            if line[0] == "$":
                parts = line.split(" ")

                if "cd" in parts:

                    if "/" == parts[2]:
                        cwd = "/"

                    elif ".." == parts[2]:
                        parts = cwd.split("/")

                        if len(parts) != 2:
                            parts.pop()
                            parts.pop()

                        cwd = "/".join(parts)
                        cwd += "/"

                    else:
                        cwd += parts[2] + "/"
            else:
                inp = line.split(" ")

                if inp[0][0].isdigit():
                    num = int(inp[0])
                    aux = cwd[:len(cwd)-1].split("/")

                    while len(aux) != 0:
                        if (len(aux) == 1):
                            size_num = dirsize.get("/", 0)
                            size_num += num
                            dirsize["/"] = size_num

                        aux = "/".join(aux)

                        size_num = dirsize.get(aux, 0)
                        size_num += num
                        dirsize[aux] = size_num

                        aux = aux.split("/")
                        aux.pop()

    total = 0

    for k in dirsize.keys():

        if dirsize[k] < 100000:
            total += dirsize[k]

        print(f"{k} = {dirsize[k]}")

    print("-" * 15, f"\nTotal: {total}")

    # --Part2--
    print("\n", "-" * 15)
    print("Part2")
    print("-" * 15)

    dirsize = dict(sorted(dirsize.items(), key=lambda i: i[1]))

    for k in dirsize.keys():
        if 70000000 - dirsize["/"] + dirsize[k] >= 30000000:
            print(f"{k} = {dirsize[k]} Needs to be deleted to have enough space!")
            break

def main():
    part12()

if __name__ == '__main__':
    main()