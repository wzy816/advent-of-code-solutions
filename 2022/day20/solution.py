import os

from tqdm import tqdm


# linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def build_loop(nums):
    tail = None
    for i, num in enumerate(nums):
        node = Node((i, num))
        if tail:
            tail.next = node
            node.prev = tail
        tail = node

    # find head
    head = tail
    while head.prev:
        head = head.prev

    head.prev = tail
    tail.next = head

    return head


def move_forward(node):
    def wire(node, next_node):
        node.next = next_node
        next_node.prev = node

    # move node forwad will make
    # node1, node, node2, node3
    # =>
    # node1, node2, node, node3
    node1 = node.prev
    node2 = node.next
    node3 = node2.next
    wire(node1, node2)
    wire(node2, node)
    wire(node, node3)


def move_backward(node):
    move_forward(node.prev)


def mix(head, n):
    for i in range(n):
        node = head
        while node.value[0] != i:
            node = node.next
        v = node.value[1]
        if v > 0:
            for _ in range(v % (n - 1)):
                move_forward(node)
        else:
            for _ in range((-v) % (n - 1)):
                move_backward(node)


def out(head, n):
    node0 = head
    while node0.value[1] != 0:
        node0 = node0.next

    ans = node0.value[1]
    for _ in range(3):
        for __ in range(1000 % n):
            node0 = node0.next
        ans += node0.value[1]
    return ans


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    nums = list(map(int, data))
    n = len(nums)

    # part1
    head = build_loop(nums)
    mix(head, n)
    print(out(head, n))

    # par2
    head = build_loop([i * 811589153 for i in nums])
    for _ in tqdm(range(10)):
        mix(head, n)
    print(out(head, n))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
