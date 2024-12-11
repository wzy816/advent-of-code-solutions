import os


def change_once(stones):

    ret = []
    for stone in stones:
        if stone == 0:
            ret.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            left = s[: len(s) // 2]
            right = s[len(s) // 2 :]
            ret = ret + [int(left), int(right)]
        else:
            ret.append(stone * 2024)
    return ret


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    stones = [int(d) for d in data[0].split(" ")]
    blinks = 25
    for _ in range(blinks):
        stones = change_once(stones)
    print(len(stones))


if __name__ == "__main__":
    main()
