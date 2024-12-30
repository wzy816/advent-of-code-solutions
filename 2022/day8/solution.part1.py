import os


def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


def flip(matrix):
    return [list(x[::-1]) for x in matrix]


def cnt(data):
    cols = len(data[0])
    rows = len(data)
    visible = [[0 for _2 in range(cols)] for _1 in range(rows)]

    for i in range(rows):
        visible[i][0] = 1
        m = data[i][0]
        for j in range(1, cols):
            if data[i][j] > m:
                visible[i][j] = 1
                m = data[i][j]

    return visible


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    data = [[int(x) for x in list(l)] for l in data]

    rows = len(data)
    cols = len(data[0])

    c1 = cnt(data)
    c2 = flip(cnt(flip(data)))
    c3 = transpose(cnt(transpose(data)))
    c4 = transpose(flip(cnt(flip(transpose(data)))))

    ans = [
        [c1[i][j] or c2[i][j] or c3[i][j] or c4[i][j] for j in range(cols)]
        for i in range(rows)
    ]

    print(sum([sum(l) for l in ans]))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
