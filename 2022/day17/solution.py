import os

from tqdm import tqdm


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    jets = data[0]

    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
    ]

    rock_index = 0
    move_index = 0

    chamber = set()
    chamber_height = 0
    rock_locs = []

    for _ in tqdm(range(10000)):

        rock = [(x + 2, y + chamber_height + 3) for x, y in rocks[rock_index % 5]]

        while True:
            if move_index % 2 == 0:
                jet = jets[(move_index // 2) % len(jets)]

                if jet == ">":
                    new_rock = [(x + 1, y) for x, y in rock]
                    if any(x >= 7 or (x, y) in chamber for x, y in new_rock):
                        new_rock = rock
                    else:
                        rock = new_rock
                elif jet == "<":
                    new_rock = [(x - 1, y) or (x, y) in chamber for x, y in rock]
                    if any(x < 0 or (x, y) in chamber for x, y in new_rock):
                        new_rock = rock
                    else:
                        rock = new_rock
            else:
                new_rock = [(x, y - 1) for x, y in rock]

                if any(y < 0 or (x, y) in chamber for x, y in new_rock):
                    new_rock = rock
                    chamber.update(new_rock)

                    old_chamber_height = chamber_height
                    chamber_height = max(
                        chamber_height, max(y for x, y in new_rock) + 1
                    )
                    rock_locs.append(
                        (
                            rock_index % 5,
                            new_rock[0][0],  # x
                            chamber_height - old_chamber_height,  # height diff
                        )
                    )

                    rock_index += 1
                    move_index += 1
                    break
                else:
                    rock = new_rock

            move_index += 1

        # part1
        if rock_index == 2022:
            print(chamber_height)

    # part2
    # search repetitions in rock locs
    target = 1000000000000

    for start in tqdm(range(10000)):
        found = False
        for size in range(2, (10000 - start) // 2):

            if (
                rock_locs[start : start + size]
                == rock_locs[start + size : start + size * 2]
            ):

                found = True
                break
        if found:
            break

    head_sum = sum([l[2] for l in rock_locs[0:start]])
    rep_sum = sum([l[2] for l in rock_locs[start : start + size]])
    rep_cnt = (target - start) // size
    tail_size = (target - start) % size
    tail_sum = sum([l[2] for l in rock_locs[start : start + tail_size]])
    print(head_sum + rep_sum * rep_cnt + tail_sum)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
