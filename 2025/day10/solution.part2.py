import os
import time

from scipy.optimize import linprog


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    ans = 0
    for row in data:
        target = None
        buttons = []
        jolt = None

        for item in row.split(" "):
            if item.startswith("["):
                target = [i for i in item[1:-1]]
            elif item.startswith("("):
                button = [0] * len(target)
                bs = list(map(int, item[1:-1].split(",")))
                for b in bs:
                    button[b] = 1
                buttons.append(button)
            elif item.startswith("{"):
                jolt = list(map(int, item[1:-1].split(",")))

        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog
        c = [1] * len(buttons)
        A = [list(r) for r in zip(*buttons)]
        b = jolt
        bounds = [(0, max(jolt))] * len(buttons)
        integrality = [1] * len(buttons)

        res = linprog(c, A_eq=A, b_eq=b, bounds=bounds, integrality=integrality)
        ans += int(res.fun)

    print(ans)


if __name__ == "__main__":
    start_time = time.perf_counter()
    # main("input_demo.txt")
    main("input.txt")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f} seconds")
