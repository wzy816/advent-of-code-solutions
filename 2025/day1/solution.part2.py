import os


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    ans = 0
    pos = 50
    for d in data:
        prev_pos = pos
        if d.startswith("L"):
            mul = -1
        elif d.startswith("R"):
            mul = 1

        for i in range(int(d[1:])):
            pos += mul*1
            if pos % 100 == 0:
                ans +=1

    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")

