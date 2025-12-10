import os
import time


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main("input_demo.txt")
    # main("input.txt")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f} seconds")
