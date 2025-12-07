import os


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")
    
    splitter = {}
    rows = len(data)
    cols = len(data[0])

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == 'S':
                pos = set([(r,c)])
            elif data[r][c] == '^':
                splitter[(r,c)] = 1

    ans = 0
    for _ in range(rows-1):
        next_pos = set()
        for s in pos:
            if (s[0]+1,s[1]) in splitter:
                if s[1]+1 < cols:
                    next_pos.add((s[0]+1,s[1]+1))
                if s[1]-1 >= 0:
                    next_pos.add((s[0]+1,s[1]-1))
                ans +=1
            else:
                next_pos.add((s[0]+1,s[1]))
        pos = next_pos

    print(ans)



if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
