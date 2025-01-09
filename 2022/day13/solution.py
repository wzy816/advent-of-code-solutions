import os


def split_list(l):
    if l[0] != "[" and l[-1] != "]":
        return [l]

    l = l[1:-1]
    lc, rc = 0, 0
    items = []
    i = 0
    while i < len(l):
        if l[i] == "[":
            lc += 1
        elif l[i] == "]":
            rc += 1
        elif l[i] == "," and lc == rc:
            items.append(l[:i])
            l = l[i + 1 :]
            i = 0
            lc = 0
            rc = 0
            continue
        i += 1

    items.append(l)
    return items


from functools import reduce


def compare(l1, l2):

    if l1 == "" and l2 == "":
        return None
    elif l1 == "":
        return True
    if l2 == "":
        return False

    if len(l1) <= 2 and len(l2) <= 2 and l1 != "[]" and l2 != "[]":
        if int(l1) < int(l2):
            return True
        elif int(l1) > int(l2):
            return False
        elif int(l1) == int(l2):
            return None

    items1 = split_list(l1)
    items2 = split_list(l2)

    while items1 and items2:
        i1 = items1.pop(0)
        i2 = items2.pop(0)
        if compare(i1, i2) is not None:
            return compare(i1, i2)

    if len(items2) > 0:
        return True
    elif len(items1) > 0:
        return False
    else:
        return None


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n\n")

    packets = reduce(lambda x, line: x + line.split("\n"), data, [])

    # part1
    ans = 0
    for i in range(0, len(packets), 2):
        if compare(packets[i], packets[i + 1]):
            ans += i // 2 + 1
    print(ans)

    # part2
    a, b = 0, 0
    for packet in packets:
        if compare(packet, "[[2]]"):
            a += 1
        elif compare(packet, "[[6]]"):
            b += 1
    print((a + 1) * (a + b + 2))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
