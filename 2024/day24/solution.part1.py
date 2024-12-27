import os
import re


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        ivs, conns = f.read().split("\n\n")

    gate_values = {}
    for iv in ivs.split("\n"):
        g, v = re.findall(r"([a-z0-9]+): (\d)", iv)[0]
        gate_values[g] = int(v)

    connections = []
    for conn in conns.split("\n"):
        g1, op, g2, g3 = re.findall(
            r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", conn
        )[0]
        connections.append([g1, op, g2, g3, False])
        for g in [g1, g2, g3]:
            if g not in gate_values:
                gate_values[g] = None

    while not all([c[4] for c in connections]):

        for i, conn in enumerate(connections):
            if conn[4]:
                continue

            g1, op, g2, g3, visited = conn
            if gate_values[g1] is None or gate_values[g2] is None:
                continue

            if op == "AND":
                gate_values[g3] = gate_values[g1] & gate_values[g2]
            elif op == "OR":
                gate_values[g3] = gate_values[g1] | gate_values[g2]
            elif op == "XOR":
                gate_values[g3] = gate_values[g1] ^ gate_values[g2]

            connections[i][4] = True

    z_nodes = [k for k in gate_values.keys() if k.startswith("z")]
    ans = 0
    for n in sorted(z_nodes, reverse=True):
        ans = ans << 1
        ans += gate_values[n]
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
