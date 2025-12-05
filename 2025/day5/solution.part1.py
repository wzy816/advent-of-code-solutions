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

    ids = [int(i) for i in data[1].split("\n")]
    # print(ids)

    ans = 0
    for id in ids:
        fresh = map(lambda r: r[0]<= id <= r[1], ranges)
        if any(list(fresh)):
            ans +=1
    print(ans)
    



if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
