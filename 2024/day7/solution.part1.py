import os


def is_evaluated_true(result, nums):
    p = []
    p.append(nums[0])

    for i in range(1, len(nums)):
        new_p = []
        for c in p:
            for a in [c + nums[i], c * nums[i]]:
                if a <= result:
                    new_p.append(a)
        p = new_p
    return result in p


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    ans = 0
    for line in data:
        result, nums = line.split(":")
        nums = [int(n) for n in nums.strip().split(" ")]
        result = int(result)
        if is_evaluated_true(result, nums):
            ans += result
    print(ans)


if __name__ == "__main__":
    main()
