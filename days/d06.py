import re


def d06():
    lines = open(f"inputs\\d06.txt").read().strip().split("\n")

    result_part1 = 1
    result_part2 = 1

    times = [int(value) for value in re.findall(r"\d+", lines[0].split(':')[1].strip())]
    distances = [int(value) for value in re.findall(r'\d+', lines[1].split(':')[1].strip())]

    part2_time = int(''.join(map(str, times)))
    part2_distance = int(''.join(map(str, distances)))

    print(times)
    print(distances)

    print(part2_time)
    print(part2_distance)

    for race_no, (time, distance) in enumerate(zip(times, distances)):
        print(f"Race No. {race_no}")
        ways_to_win = calculate_num_of_strategies(time, distance)
        print(f"Number of ways to win: {ways_to_win}")
        result_part1 *= ways_to_win

    # Yes I know this is inefficient. It's better to use bigger increments to approximate faster
    # Or even better, use binary search. But who cares, it got solved faster than I could decide to do so :)
    result_part2 = calculate_num_of_strategies(part2_time, part2_distance)

    print(f"Part 1: {result_part1}")
    print(f"Part 2: {result_part2}")


def calculate_num_of_strategies(time, distance_to_beat):
    num_of_winning_strategies = 0
    for ms in range(0, time):
        distance = ms * (time - ms)
        # print(distance)
        if distance > distance_to_beat:
            num_of_winning_strategies += 1
    return num_of_winning_strategies


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
