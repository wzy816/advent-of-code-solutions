import os
from itertools import combinations


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")
    ans = 0
    for bank in data:
        ans += max([int(e[0]+e[1]) for e in combinations(bank, 2)])
    print(ans)
        


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
