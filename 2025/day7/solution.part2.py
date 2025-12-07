import os

from collections import Counter
def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")
    
    splitter = {}
    rows = len(data)
    cols = len(data[0])
    pos = Counter()
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == 'S':
                pos[(r,c)] = 1
            elif data[r][c] == '^':
                splitter[(r,c)] = 1

    for _ in range(rows-1):
        next_pos = Counter()
        for s in pos:
            if (s[0]+1,s[1]) in splitter:
                if s[1]+1 < cols:
                    next_pos[(s[0]+1,s[1]+1)]+= pos[s]
                if s[1]-1 >= 0:
                    next_pos[(s[0]+1,s[1]-1)]+= pos[s]
            else:
                next_pos[(s[0]+1,s[1])]+= pos[s]
        pos = next_pos

    print(pos.total())



if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
