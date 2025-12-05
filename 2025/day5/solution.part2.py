import os

def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]
    for r in ranges[1:]:
        if r[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r[1]))
        else:
            merged.append(r)
    return merged


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n\n")

    ranges = []
    for r in data[0].split("\n"):
        start,end = r.split("-")
        ranges.append((int(start), int(end)))

    ranges = merge_ranges(ranges)
    # print(ranges)

    ans = sum(map(lambda x: x[1] - x[0] + 1,ranges))
    print(ans)

    



if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
