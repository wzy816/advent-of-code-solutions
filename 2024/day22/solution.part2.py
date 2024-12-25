import os


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    from functools import cache

    @cache
    def step(s):
        s = ((s << 6) ^ s) & 0b111111111111111111111111
        s = ((s >> 5) ^ s) & 0b111111111111111111111111
        s = ((s << 11) ^ s) & 0b111111111111111111111111
        return s

    from collections import Counter, deque

    bananas = Counter()
    for line in data:
        b = {}
        num = int(line)
        changes = deque()
        prev_p = num % 10

        for i in range(1, 2001):  # generate 2000 new
            num = step(num)
            cur_p = num % 10
            changes.append(cur_p - prev_p)
            if i > 4:
                changes.popleft()

            k = tuple(changes)
            if k not in b and len(k) == 4:
                b[k] = cur_p

            # print(i, num, cur_p, cur_p - prev_p, changes)

            prev_p = cur_p
        bananas += Counter(b)

    print(bananas.most_common(1))


if __name__ == "__main__":
    # main("input_demo2.txt")
    main("input.txt")
