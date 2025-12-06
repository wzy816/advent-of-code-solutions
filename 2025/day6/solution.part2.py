import os
import math

def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    # reverse
    data = [line[::-1] for line in data]

    # transpose and insert empty row before +/*
    data = [''.join(line[:-1]+(' ',line[-1])) for line in zip(*data)]
    data = ''.join(data).split()

    ans = 0
    arr = []
    for d in data:
        if d == '+':
            ans += sum(arr)
            arr = []
        elif d[-1] == '*':
            ans += math.prod(arr)
            arr = []
        else:
            arr.append(int(d))

    print(ans)

if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
