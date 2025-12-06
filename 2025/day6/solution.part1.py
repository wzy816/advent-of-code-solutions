import os
import math

def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")


    rows = [line.strip().split() for line in data]

    ans = 0
    for columns in zip(*rows):
        if columns[-1] == '+':
            ans += sum(map(int,columns[:-1]))
        elif columns[-1] == '*':
            ans += math.prod(map(int,columns[:-1]))
    print(ans)

if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
