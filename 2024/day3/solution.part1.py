import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    d = "".join(data)
    import re

    match = re.findall(r"mul\((\d+),(\d+)\)", d)
    ans = sum([int(m[0]) * int(m[1]) for m in match])
    print(ans)


if __name__ == "__main__":
    main()
