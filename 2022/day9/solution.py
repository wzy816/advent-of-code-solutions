import os


def move_tail(h, t):
    if abs(h.real - t.real) > 1 or abs(h.imag - t.imag) > 1:
        if h.real > t.real:
            t += 1
        elif h.real < t.real:
            t -= 1
        if h.imag > t.imag:
            t += 1j
        elif h.imag < t.imag:
            t -= 1j
    return t


dirs = {"R": 1, "L": -1, "U": 1j, "D": -1j}


def main(file_name, snake_size):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    snake = [0 + 0j for _ in range(snake_size)]

    visited = {snake[-1]: 1}

    for line in data:
        direction, steps = line.split(" ")
        steps = int(steps)

        for _ in range(steps):
            snake[0] += dirs[direction]

            for i in range(1, snake_size):
                snake[i] = move_tail(snake[i - 1], snake[i])

            visited[snake[-1]] = 1

    print(len(visited.keys()))


if __name__ == "__main__":
    # main("input_demo.txt", 2)
    main("input.txt", 2)

    # main("input_demo2.txt", 10)
    main("input.txt", 10)
