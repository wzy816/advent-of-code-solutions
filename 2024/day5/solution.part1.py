import os


def is_right_order(rules, update):
    for i, num in enumerate(update):
        js = update[i + 1 :]
        if num in rules.keys():
            if len(rules[num].intersection(set(js))) > 0:
                return False
    return True


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")
    rules = {}
    updates = []
    for line in data:
        if line == "":
            continue
        elif "|" in line:
            p1, p2 = line.split("|")
            if int(p2) not in rules.keys():
                rules[int(p2)] = set()
            rules[int(p2)] = rules[int(p2)].union(set([int(p1)]))
        else:
            updates.append([int(num) for num in line.split(",")])

    ans = 0
    for update in updates:
        if is_right_order(rules, update):
            half = (len(update) - 1) / 2
            ans += update[int(half)]
    print(ans)


if __name__ == "__main__":
    main()
