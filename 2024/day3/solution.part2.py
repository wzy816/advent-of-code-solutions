import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    d = "".join(data)
    import re

    match = re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", d)

    ans = 0
    i = 0
    enable = True
    while i < len(match):
        m = match[i]
        if m == "don't()":
            enable = False
        elif m == "do()":
            enable = True
        elif enable:
            m = m[4:-1].split(",")
            ans += int(m[0]) * int(m[1])
        i = i + 1
    print(ans)


if __name__ == "__main__":
    main()
