import os

from itertools import combinations

def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")
    
    points = [[int(i) for i in c.split(",")] for c in data]


    ans = 0
    for p1,p2 in combinations(points,2):
        area = abs((p1[0]-p2[0]+1)*(p1[1]-p2[1]+1))
        ans = max(ans, area)
    print(ans)

if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
