import re


def d02():
    lines = open(f"inputs\\d02.txt").read().strip().split("\n")

    # cube_set = {'red': 12, 'green': 13, 'blue': 14}

    game_regex = r"Game (\d+)"
    sum_part1 = 0
    sum_part2 = 0

    for line in lines:
        red_max = 0
        green_max = 0
        blue_max = 0
        game_data = line.split(':')
        game_id = int(re.search(game_regex, game_data[0]).group(1))
        cube_sets = game_data[1].split(';')
        valid = True
        for cubes in cube_sets:
            red_cntr = 12
            green_cntr = 13
            blue_cntr = 14
            for cube in cubes.split(','):
                cube_data = cube.strip().split(' ')
                if cube_data[1] == 'red':
                    if red_max < int(cube_data[0]):
                        red_max = int(cube_data[0])
                    red_cntr -= int(cube_data[0])
                elif cube_data[1] == 'green':
                    if green_max < int(cube_data[0]):
                        green_max = int(cube_data[0])
                    green_cntr -= int(cube_data[0])
                elif cube_data[1] == 'blue':
                    if blue_max < int(cube_data[0]):
                        blue_max = int(cube_data[0])
                    blue_cntr -= int(cube_data[0])
                else:
                    pass
            if red_cntr < 0 or green_cntr < 0 or blue_cntr < 0:
                valid = False
        if valid:
            sum_part1 += game_id
        print(f"{game_id}: {red_cntr} red, {green_cntr} green, {blue_cntr} blue")
        sum_part2 += red_max * green_max * blue_max
    print(sum_part1)
    print(sum_part2)


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
