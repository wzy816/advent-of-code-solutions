import itertools
import math
import os


def surface_area(cubes):
    ret = len(cubes) * 6

    for c1, c2 in itertools.combinations(cubes, 2):
        x1, y1, z1 = c1
        x2, y2, z2 = c2
        if abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1:
            ret -= 2
    return ret


def bounding_box(cubes):
    xmin, ymin, zmin = math.inf, math.inf, math.inf
    xmax, ymax, zmax = -math.inf, -math.inf, -math.inf
    for c in cubes:
        xmin = min(xmin, c[0])
        ymin = min(ymin, c[1])
        zmin = min(zmin, c[2])
        xmax = max(xmax, c[0])
        ymax = max(ymax, c[1])
        zmax = max(zmax, c[2])
    return map(int, (xmin, xmax, ymin, ymax, zmin, zmax))


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    cubes = set()
    for line in data:
        x, y, z = map(int, line.split(","))
        cubes.add((x, y, z))

    # part1
    print(surface_area(cubes))

    # part2
    # extend bbox of cubes and fill air cubes
    xmin, xmax, ymin, ymax, zmin, zmax = bounding_box(cubes)
    air_cubes = set()
    for x in range(xmin - 1, xmax + 2):
        for y in range(ymin - 1, ymax + 2):
            for z in range(zmin - 1, zmax + 2):
                c = (x, y, z)
                if c in cubes:
                    continue
                else:
                    air_cubes.add(c)

    # bfs find exterior air cubes
    air_xmin, air_xmax, air_ymin, air_ymax, air_zmin, air_zmax = bounding_box(air_cubes)

    q = [(air_xmin, air_ymin, air_zmin)]
    exterior_cubes = set()

    while q:
        x, y, z = q.pop(0)
        c = (x, y, z)
        if c in air_cubes:
            air_cubes.remove(c)
            exterior_cubes.add(c)
            for dx, dy, dz in [
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1),
            ]:
                nx, ny, nz = x + dx, y + dy, z + dz
                if (nx, ny, nz) in air_cubes:
                    q.append((nx, ny, nz))

    # count only exterior cubes, minus bbox 6 surfaces
    a, b, c = air_xmax - air_xmin + 1, air_ymax - air_ymin + 1, air_zmax - air_zmin + 1
    print(surface_area(exterior_cubes) - 2 * (a * b + b * c + c * a))


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
