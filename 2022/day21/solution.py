import os
import re


def consume(q):
    d = {}
    while q:
        new_q = []
        for item in q:
            id, left, op, right, val = item
            if left in d and right in d:
                if op == "+":
                    d[id] = d[left] + d[right]
                elif op == "-":
                    d[id] = d[left] - d[right]
                elif op == "*":
                    d[id] = d[left] * d[right]
                elif op == "/":
                    d[id] = d[left] / d[right]
            elif op is None:
                d[id] = int(val)
            else:
                new_q.append(item)
        q = new_q
    return int(d["root"])


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    ms = []
    for line in data:
        if any([op in line for op in "+-*/"]):
            regex = r"(\w+): (\w+) ([\+\-*\/]) (\w+)"
            id, left, op, right = re.findall(regex, line)[0]
            ms.append((id, left, op, right, None))
        else:
            regex = r"(\w+): (\d+)"
            id, val = re.findall(regex, line)[0]
            ms.append((id, None, None, None, val))

    # part1
    print(consume(ms.copy()))

    # part2
    # modify job but keep tree structure
    q2 = []
    for m in ms:
        if m[0] == "root":
            q2.append(("root", m[1], "-", m[3], None))
        elif m[0] == "humn":
            continue
        else:
            q2.append(m)

    # note that humn to root relation is Monotonic
    # so use binary search to find humn so that root = 0
    low = 0
    high = 1e20
    while low < high:
        mid = (low + high) // 2
        if consume(q2 + [("humn", None, None, None, mid)]) > 0:
            low = mid + 1
        else:
            high = mid
    print(int(low))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
