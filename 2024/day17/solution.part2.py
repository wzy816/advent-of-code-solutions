import os


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

    def run_program(ra, program):
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

        register = {"A": ra, "B": 0, "C": 0}

        i = 0
        out = []
        size = len(program)
        while i < size:
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
                new_out = combo(operand, register) % 8
                out.append(new_out)
            elif opcode == 6:
                numerator = register["A"]
                denominator = 2 ** combo(operand, register)
                register["B"] = numerator // denominator
            elif opcode == 7:
                numerator = register["A"]
                denominator = 2 ** combo(operand, register)
                register["C"] = numerator // denominator

            i += 2
        return out[0]

    # from input
    # program = 2, 4, 1, 3, 7, 5, 0, 3, 1, 5, 4, 1, 5, 5, 3, 0
    # explained
    # 2,4 reg['B'] = reg['A'] % 8
    # 1,3 reg['B'] = 3 ^ reg['B']
    # 7,5 reg['C'] = reg['A'] // 2**reg['B']
    # 0,3 reg['A'] = reg['A'] // 8
    # 1,5 reg['B'] = 5 ^ reg['B']
    # 4,1 reg['B'] = reg['B'] ^ reg['C']
    # 5,5 out reg['B'] % 8
    # 3,0 if reg['A'] != 0, loop again
    #
    # for each loop, next reg['A'] is reg['A'] shifted 3 times to the right, lost last 3 bits
    # only 5,5 out a number
    # loop ends when reg['A'] is 0, so out length = how many 3 bits in reg['A']
    #
    # reverse think about the program execution
    # last number out is generated when reg['A'] has at most 3 bits
    # so iterate 0-7 to find that 3 bits reg['A'], for example 110 => 0
    # second to last number out is generated when reg['A'] from last generated is shifted 3 times to the left, plus new last 3 bits
    # so iterate 0-7 to find that 3 bits reg['A'] again, for example  110<<3 + 001 = 110001 => [3,0]
    # there might be multiple 3bits or none for each out number, cause the generation process is not predictable

    ans = [0]
    out = program
    for o in out[::-1]:
        new_ans = []
        for a in ans:
            for i in range(8):
                # run program without last loop instruction
                cur_o = run_program(a * 8 + i, program[:-2])
                if cur_o == o:
                    new_ans.append(a * 8 + i)
        ans = new_ans
    print(min(ans))


if __name__ == "__main__":
    # main("input_demo2.txt")
    main("input.txt")
