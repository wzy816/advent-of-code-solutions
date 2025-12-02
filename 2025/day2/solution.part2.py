import os

def check_if_repeated(s,times):
    if len(s) % times != 0:
        return False
    sub_len = len(s) // times
    for i in range(times):
        if s[i*sub_len:(i+1)*sub_len] != s[0:sub_len]:
            return False
    return True

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

            for repeted_times in range(2,len(s)+1):
                if check_if_repeated(s,repeted_times):
                    ans += i
                    break
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
