import os

map_cache = {}  # stone_num: [next]


# 0 => 1 => 2024 => 20,24 => 2,0,2,4
# f(0) = [1]
# f(1) = [2024]
# f(2024) = [20,24]
def map_stone_num_to_next(stone_num: int):
    if stone_num in map_cache:
        return map_cache[stone_num]
    r = None
    if stone_num == 0:
        r = [1]
    elif len(str(stone_num)) % 2 == 0:
        si = str(stone_num)
        left = si[: len(si) // 2]
        right = si[len(si) // 2 :]
        r = [int(left), int(right)]
    else:
        r = [int(stone_num * 2024)]
    map_cache[stone_num] = r
    return r


total_dict = {}  # (step, stone_num) : total_stones


# 0 => 1 => 2024 => 20,24 => 2,0,2,4
# f(0,*) = 1
# f(1,0) = f(0,1) = 0
# f(2,0) = f(1,1) = f(0,2024) = 1
# f(3,0) = f(2,1) = f(1,2024) = f(0,20) + f(0,24) = 1 + 1 = 2
# ...
def count_stone_num_at_blink(
    step: int,
    stone_num: int,
):
    k = (step, stone_num)
    if k in total_dict:
        return total_dict[k]

    if step == 0:
        r = 1
    else:
        r = 0
        for o in map_stone_num_to_next(stone_num):
            r += count_stone_num_at_blink(step - 1, o)
    total_dict[k] = r
    return r


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    stones = [int(d) for d in data[0].split(" ")]

    print(stones)

    ans = 0
    blinks = 75
    for stone_num in stones:
        ans += count_stone_num_at_blink(blinks, stone_num)
    print(ans)


if __name__ == "__main__":
    main()
