import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input_demo.txt"), "r") as f:
        data = f.read().split("\n")




if __name__ == "__main__":
    main()
