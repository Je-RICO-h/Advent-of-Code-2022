def direction(direct):
    if direct == "U" or direct == "L":
        return -1
    else:
        return 1


def move_head(direct, head):
    if direct == "U" or direct == "D":
        head[0] += direction(direct)
    else:
        head[1] += direction(direct)

    return head


def move_tail(head, tail, visited):
    move = [0, 0]

    move[0] = head[0] - tail[0]
    move[1] = head[1] - tail[1]

    if abs(move[0]) <= 1 and abs(move[1]) <= 1:
        pass
    elif abs(move[0]) == 2 and abs(move[1]) == 2:
        tail[0] += move[0] / 2
        tail[1] += move[1] / 2
    elif abs(move[0]) == 2:
        tail[0] += move[0] / 2
        tail[1] = head[1]
    elif abs(move[1]) == 2:
        tail[1] += move[1] / 2
        tail[0] = head[0]

    if (tail[0], tail[1]) not in visited:
        visited.append((tail[0], tail[1]))

    return tail, visited


def main():
    head = [0, 0]
    knots = [[0, 0] for _ in range(9)]
    visited = [[(0, 0)] for _ in range(9)]

    with open("input.txt", "r") as f:
        for line in f:
            line.strip()
            parts = line.split(" ")

            for i in range(int(parts[1])):
                head = move_head(parts[0], head)
                headknot = head

                for j in range(len(knots)):
                    knots[j], visited[j] = move_tail(headknot, knots[j], visited[j])
                    headknot = knots[j]

        print(f"Part 1 Visited: {len(visited[0])}")
        print(f"Part 2 Visited: {len(visited[8])}")


if __name__ == '__main__':
    main()
