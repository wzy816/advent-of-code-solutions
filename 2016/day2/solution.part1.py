import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input_demo.txt"), "r") as f:
        data = f.read().split("\n")

    # 1 2 3
    # 4 5 6
    # 7 8 9

    n = {
        (1, "U"): 1,
        (1, "L"): 1,
        (1, "D"): 4,
        (1, "R"): 2,
        (2, "U"): 2,
        (2, "L"): 1,
        (2, "D"): 5,
        (2, "R"): 3,
        (3, "U"): 3,
        (3, "L"): 2,
        (3, "D"): 6,
        (3, "R"): 3,
        (4, "U"): 1,
        (4, "L"): 4,
        (4, "D"): 7,
        (4, "R"): 5,
        (5, "U"): 2,
        (5, "L"): 4,
        (5, "D"): 8,
        (5, "R"): 6,
        (6, "U"): 3,
        (6, "L"): 5,
        (6, "D"): 9,
        (6, "R"): 6,
        (7, "U"): 4,
        (7, "L"): 7,
        (7, "D"): 7,
        (7, "R"): 8,
        (8, "U"): 5,
        (8, "L"): 7,
        (8, "D"): 8,
        (8, "R"): 9,
        (9, "U"): 6,
        (9, "L"): 8,
        (9, "D"): 9,
        (9, "R"): 9,
    }

    pos = 5

    ans = []
    for line in data:
        for move in line:
            pos = n[(pos, move)]

        ans.append(pos)
    print(ans)


if __name__ == "__main__":
    main()
