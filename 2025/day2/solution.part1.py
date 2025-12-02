import os


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")
    
    ranges = data[0].split(",")
    ans = 0
    for r in ranges:
        start,end = r.split("-")

        for i in range(int(start), int(end)+1):
            s = str(i)
            if len(s) % 2 == 0 and s[0:len(s)//2] == s[len(s)//2:]:
                # print(s)
                ans += i
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
