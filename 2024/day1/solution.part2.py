import heapq
import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    left = []
    right = []
    for line in data:
        l = line.split(" ")
        left.append(int(l[0]))
        right.append(int(l[-1]))

    from collections import Counter

    cnt = Counter(right)
    sim = 0
    for l in left:
        if cnt[l] > 0:
            sim += l * cnt[l]
    print(sim)


if __name__ == "__main__":
    main()
