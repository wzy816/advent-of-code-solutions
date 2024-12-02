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
    dist = 0
    heapq.heapify(left)
    heapq.heapify(right)
    while left and right:
        dist += abs(heapq.heappop(left) - heapq.heappop(right))
    print(dist)


if __name__ == "__main__":
    main()
