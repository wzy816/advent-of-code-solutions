import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n\n")
    
    a = [sum([int(i) for i in x.split("\n")]) for x in data]
    a = sorted(a)
    print(sum(a[-3:]))
    # 213958



if __name__ == "__main__":
    main()
