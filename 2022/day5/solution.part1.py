import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    from collections import deque

    q = {}
    s = "init"
    max_q_id = 0
    for line in data:
        if line == "":
            s = "instruction"
            continue
        if s == "init":
            for i in range(1, len(line), 4):
                q_id = i // 4 + 1
                max_q_id = max(max_q_id, q_id)
                if q_id not in q:
                    q[q_id] = deque()

                if line[i] == " " or line[i].isdigit():
                    continue

                q[q_id].appendleft(line[i])
        elif s == "instruction":
            _, count, _, from_, _, to_ = line.split(" ")
            count = int(count)
            from_ = int(from_)
            to_ = int(to_)
            for _ in range(count):
                a = q[from_].pop()
                q[to_].append(a)
    print(q)

    print("".join([q[i][-1] for i in range(1, max_q_id + 1)]))


if __name__ == "__main__":
    main()
