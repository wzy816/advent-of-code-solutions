import os
from itertools import combinations

from tqdm import tqdm


def f1(arr,target_length):
    if target_length ==1:
        return [max(arr)]

    max_int = max(arr[0:-target_length+1])
    max_pos = arr.index(max_int)

    return [max_int] + f1(arr[max_pos+1:],target_length-1)

    
def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    ans = 0
    for bank in data:
        bank = [int(e) for e in bank]
        a = [str(i) for i in f1(bank,12)]
        ans += int(''.join(a))

    print(ans)
        


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
