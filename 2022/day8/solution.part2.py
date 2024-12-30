import os


def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


def flip(matrix):
    return [list(x[::-1]) for x in matrix]


def cnt(data):
    cols = len(data[0])
    rows = len(data)
    ret = []

    for i in range(rows):
        mono = []
        prev_larger = [0] * cols
        for j in range(cols):
            d = data[i][j]
            while mono and mono[-1][0] > -d:
                mono.pop()
            if mono:
                prev_larger[j] = mono[-1][1]
            mono.append((-d, j))
        ret.append([j - prev_larger[j] for j in range(cols)])

    return ret


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
        [c1[i][j] * c2[i][j] * c3[i][j] * c4[i][j] for j in range(cols)]
        for i in range(rows)
    ]

    print(max([max(l) for l in ans]))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
