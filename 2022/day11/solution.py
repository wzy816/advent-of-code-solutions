import os
from copy import deepcopy

from tqdm import tqdm


class Monkey:
    def __init__(self):
        self._items = []
        self._operation = None
        self._test = None
        self._inspected = 0

    @property
    def test(self):
        return self._test

    @property
    def items(self):
        return self._items

    @property
    def operation(self):
        return self._operation

    @property
    def inspected(self):
        return self._inspected

    def inspect(self):
        self._inspected += 1

    def add_items(self, item):
        self._items.append(int(item))

    def add_operation(self, op):
        self._operation = lambda old: eval(op)

    def add_test(self, test, true, false):
        self._test = lambda x: int(true) if x % int(test) == 0 else int(false)


def round(monkeys, manage):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop()
            ni = monkey.operation(item)
            ni = manage(ni)
            t = monkey.test(ni)
            monkeys[t].add_items(ni)
            monkey.inspect()


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n\n")

    monkeys = []
    for m in data:
        lines = m.split("\n")
        monkey = Monkey()

        for line in lines[1:]:
            if line.startswith("  Starting items:"):
                items = line.split(": ")[1].split(", ")
            elif line.startswith("  Operation:"):
                op = line.split("new =")[1]
            elif line.startswith("  Test:"):
                test = line.split(" ")[-1]
            elif line.startswith("    If true:"):
                true = line.split(" ")[-1]
            elif line.startswith("    If false:"):
                false = line.split(" ")[-1]

        for item in items:
            monkey.add_items(item)
        monkey.add_operation(op)
        monkey.add_test(test, true, false)

        monkeys.append(monkey)

    # part1
    m1 = [deepcopy(m) for m in monkeys]
    for _ in range(20):
        round(m1, lambda x: x // 3)
    inspected = sorted([m.inspected for m in m1], reverse=True)
    print(inspected[0] * inspected[1])

    # part2
    # multiple all divisibles you get 9699690
    m2 = [deepcopy(m) for m in monkeys]
    for _ in tqdm(range(10000)):
        round(m2, lambda x: x % 9699690)
    inspected = sorted([m.inspected for m in m2], reverse=True)
    print(inspected[0] * inspected[1])


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
