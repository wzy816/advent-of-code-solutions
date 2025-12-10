import os
import time


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    ans = 0
    for row in data:
        target = None
        buttons = []

        for item in row.split(" "):
            if item.startswith("["):
                ts = ["0" if i == "." else "1" for i in item[1:-1]][::-1]
                target = int("".join(ts), 2)
            elif item.startswith("("):
                mask = 0
                btns = list(map(int, item[1:-1].split(",")))
                for btn in btns:
                    mask += 1 << btn
                buttons.append(mask)

        states = {0: 0}
        while target not in states:
            next_states = states.copy()
            for s in states:
                for button in buttons:
                    new_s = s ^ button
                    if new_s not in next_states:
                        next_states[new_s] = states[s] + 1
                    else:
                        if states[s] + 1 < next_states[new_s]:
                            next_states[new_s] = states[s] + 1
            states = next_states

        ans += states[target]
    print(ans)


if __name__ == "__main__":
    start_time = time.perf_counter()
    # main("input_demo.txt")
    main("input.txt")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f} seconds")
