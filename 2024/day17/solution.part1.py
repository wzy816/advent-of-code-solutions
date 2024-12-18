import os
from typing import *


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    register = {}
    program = []
    for line in data:
        if line.startswith("Register"):
            _, reg, val = line.split(" ")
            reg = reg.replace(":", "")
            register[reg] = int(val)
        if line.startswith("Program"):
            _, val = line.split(": ")
            program = list(map(int, val.split(",")))
    print(register, program)

    def literal(operand: int):
        return operand

    def combo(operand: int, reg):
        if operand <= 3:
            return operand
        elif operand == 4:
            return reg["A"]
        elif operand == 5:
            return reg["B"]
        elif operand == 6:
            return reg["C"]

    i = 0
    out = []
    while i < len(program):
        opcode = program[i]
        operand = program[i + 1]
        if opcode == 0:
            numerator = register["A"]
            denominator = 2 ** combo(operand, register)
            register["A"] = numerator // denominator
        elif opcode == 1:
            register["B"] = literal(operand) ^ register["B"]
        elif opcode == 2:
            register["B"] = combo(operand, register) % 8
        elif opcode == 3:
            if register["A"] == 0:
                pass
            else:
                instruction_pointer = literal(operand)
                if instruction_pointer != i:
                    i = instruction_pointer
                    continue
        elif opcode == 4:
            register["B"] = register["B"] ^ register["C"]
        elif opcode == 5:
            out.append(combo(operand, register) % 8)
        elif opcode == 6:
            numerator = register["A"]
            denominator = 2 ** combo(operand, register)
            register["B"] = numerator // denominator
        elif opcode == 7:
            numerator = register["A"]
            denominator = 2 ** combo(operand, register)
            register["C"] = numerator // denominator

        print(
            f"{i}:{opcode},{operand}",
            register,
            bin(register["A"]),
            bin(register["B"]),
            bin(register["C"]),
            out,
        )

        i += 2
    print(",".join(map(str, out)))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
