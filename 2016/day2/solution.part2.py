import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    #     1
    #   2 3 4
    # 5 6 7 8 9
    #   A B C
    #     D

    n = {
        1: [1, 1, 3, 1],
        2: [2, 2, 6, 3],
        3: [1, 2, 7, 4],
        4: [4, 3, 8, 4],
        5: [5, 5, 5, 6],
        6: [2, 5, "A", 7],
        7: [3, 6, "B", 8],
        8: [4, 7, "C", 9],
        9: [9, 8, 9, 9],
        "A": [6, "A", "A", "B"],
        "B": [7, "A", "D", "C"],
        "C": [8, "B", "C", "C"],
        "D": ["B", "D", "D", "D"],
    }
    d = {"U": 0, "L": 1, "D": 2, "R": 3}

    pos = 5

    ans = []
    for line in data:
        for move in line:

            pos = n[pos][d[move]]

        ans.append(pos)
    print(ans)


if __name__ == "__main__":
    main()
