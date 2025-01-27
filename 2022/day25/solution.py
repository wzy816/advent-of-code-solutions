import os


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    def snafu_to_decimal(snafu):
        d = {"1": 1, "2": 2, "-": -1, "=": -2, "0": 0}
        decimal = 0
        for i, char in enumerate(snafu[::-1]):
            decimal += d[char] * (5**i)
        return decimal

    def decimal_to_snafu(decimal):
        d = {1: "1", 2: "2", 4: "-", 3: "=", 0: "0"}
        snafu = ""
        while decimal > 0:
            remainder = decimal % 5
            snafu = d[remainder] + snafu
            if remainder > 2:
                decimal += 5
            decimal //= 5
        return snafu

    # part1
    total = sum([snafu_to_decimal(line) for line in data])
    print(total)
    print(decimal_to_snafu(total))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
