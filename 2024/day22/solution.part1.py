import os


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    # mix : a ^ b
    # prune a % 16777216
    # print(42 ^ 15)
    # print(100000000 % 16777216)

    from functools import cache

    def step(s):
        s = ((s << 6) ^ s) & 0b111111111111111111111111
        s = ((s >> 5) ^ s) & 0b111111111111111111111111
        s = ((s << 11) ^ s) & 0b111111111111111111111111
        return s

    ans = 0
    for line in data:
        num = int(line)
        for _ in range(2000):
            num = step(num)
        ans += num
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    # main("input_demo1.txt")
    main("input.txt")
