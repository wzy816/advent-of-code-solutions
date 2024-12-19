import os


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n\n")

    available = {t: 1 for t in data[0].split(", ")}

    ans = 0
    for towel in data[1].split("\n"):
        n = len(towel)
        p = [1] + [0 for _ in range(n)]
        for start in range(n):
            for end in range(start + 1, n + 1):
                if p[start] and towel[start:end] in available:
                    p[end] = 1
            if p[n] == 1:
                ans += 1
                break
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
