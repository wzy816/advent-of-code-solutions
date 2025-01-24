import os
import re


def run_blueprint(bp, max_time):
    (
        id,
        ore_bot_ore,
        clay_bot_ore,
        obsidian_bot_ore,
        obsidian_bot_clay,
        geode_bot_ore,
        geode_bot_obsidian,
    ) = bp

    q = set()
    all_q = set()
    q.add((1, 0, 0, 0, 0, 0, 0, 0))
    time = 0

    while q:
        max_geode = max([cur[-1] for cur in q])

        if time == max_time:
            return id, max_geode

        new_q = set()
        all_q.update(q)

        remain_time = max_time - time

        for cur in q:
            (
                ore_bot,
                clay_bot,
                obsidian_bot,
                geode_bot,
                ore,
                clay,
                obsidian,
                geode,
            ) = cur

            # assume infinity resources to build geode_bot every remain minutes
            # this works mainly for the last few minutes when state space is large but minutes time is small
            if (
                geode + geode_bot * remain_time + remain_time * (remain_time - 1) // 2
                <= max_geode
            ):
                continue

            # trick:
            # since we can build only one robot every minute
            # don't build any new ore robot if we have enough to build for clay\obsidian\geode robot
            # don't build any new clay robot if we have enough to build for obsidian robot
            # don't build any new obsidian robot if we have enough to build for geode robot
            # otherwise will leave too much resources unused

            if (
                ore >= geode_bot_ore
                and obsidian >= geode_bot_obsidian
                and (
                    ore_bot >= geode_bot_ore
                    or clay_bot >= obsidian_bot_clay
                    or obsidian_bot >= geode_bot_obsidian
                )
            ):
                continue
            if ore >= geode_bot_ore and obsidian >= geode_bot_obsidian:
                new_q.add(
                    (
                        ore_bot,
                        clay_bot,
                        obsidian_bot,
                        geode_bot + 1,
                        ore - geode_bot_ore + ore_bot,
                        clay + clay_bot,
                        obsidian - geode_bot_obsidian + obsidian_bot,
                        geode + geode_bot,
                    )
                )
            if (
                ore >= obsidian_bot_ore
                and clay >= obsidian_bot_clay
                and obsidian_bot < geode_bot_obsidian
            ):
                new_q.add(
                    (
                        ore_bot,
                        clay_bot,
                        obsidian_bot + 1,
                        geode_bot,
                        ore - obsidian_bot_ore + ore_bot,
                        clay - obsidian_bot_clay + clay_bot,
                        obsidian + obsidian_bot,
                        geode + geode_bot,
                    )
                )
            if ore >= clay_bot_ore and clay_bot < obsidian_bot_clay:
                new_q.add(
                    (
                        ore_bot,
                        clay_bot + 1,
                        obsidian_bot,
                        geode_bot,
                        ore - clay_bot_ore + ore_bot,
                        clay + clay_bot,
                        obsidian + obsidian_bot,
                        geode + geode_bot,
                    )
                )

            if ore >= ore_bot_ore and (
                ore_bot < clay_bot_ore
                or ore_bot < obsidian_bot_ore
                or ore_bot < geode_bot_ore
            ):
                new_q.add(
                    (
                        ore_bot + 1,
                        clay_bot,
                        obsidian_bot,
                        geode_bot,
                        ore - ore_bot_ore + ore_bot,
                        clay + clay_bot,
                        obsidian + obsidian_bot,
                        geode + geode_bot,
                    )
                )
            new_q.add(
                (
                    ore_bot,
                    clay_bot,
                    obsidian_bot,
                    geode_bot,
                    ore + ore_bot,
                    clay + clay_bot,
                    obsidian + obsidian_bot,
                    geode + geode_bot,
                )
            )
        q = new_q.difference(all_q)
        time = time + 1


def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read().split("\n")

    blueprints = []
    for line in data:
        regex = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
        (
            id,
            ore_bot_ore,
            clay_bot_ore,
            obsidian_bot_ore,
            obsidian_bot_clay,
            geode_bot_ore,
            geode_bot_obsidian,
        ) = map(int, re.findall(regex, line)[0])

        blueprints.append(
            (
                id,
                ore_bot_ore,
                clay_bot_ore,
                obsidian_bot_ore,
                obsidian_bot_clay,
                geode_bot_ore,
                geode_bot_obsidian,
            )
        )

    # part1
    ans = 0
    for bp in blueprints:
        id, max_geode = run_blueprint(bp, 24)
        print(id, max_geode)
        ans += id * max_geode
    print(ans)

    # part2
    ans = 1
    for bp in blueprints[0:3]:
        id, max_geode = run_blueprint(bp, 32)
        ans *= max_geode
    print(ans)


if __name__ == "__main__":
    # main("input_demo.txt")
    main("input.txt")
