# Author:   Not me hehehe....


GRID_SIZE = 139


def d03():
    lines = open(f"inputs\\d03.txt").read().strip().split("\n")

    sum_part1 = 0
    sum_part2 = 0
    parts = []
    temp_number = ""
    star_set = set()
    star_set_voigas = set()

    for y, line in enumerate(lines):
        line += '.'
        is_part = False
        # print(f"Line: {y}")
        for x, c in enumerate(line):
            # print(f"Line: {line}\n Char: {c}")
            if c.isdigit():
                # print(f"{c} is digit")
                temp_number += c
                result, star_y, star_x = check_for_char(lines, y, x)
                is_part |= result
                if result and star_y >= 0 and star_x >= 0:
                    star_set.add((star_y, star_x))
                    star_set_voigas.add((star_y, star_x))
                    # print(star_set)
            else:
                # print(f"{c} is not digit")
                if is_part:
                    # print(temp_number)
                    part_number = int(temp_number)
                    parts.append((part_number, star_set))
                    sum_part1 += part_number
                    # print(f"{sum_part1}\n")
                temp_number = ""
                star_set = set()
                is_part = False

    # print(parts)
    # print(star_set_voigas)

    for star in star_set_voigas:
        numbers_of_star = []
        for part in parts:
            for s in part[1]:
                if s == star:
                    numbers_of_star.append(part[0])
        if len(numbers_of_star) == 2:
            sum_part2 += numbers_of_star[0]*numbers_of_star[1]

    print(f"Part1: {sum_part1}")
    print(f"Part2: {sum_part2}")


def check_for_char(lines, i, j):
    result = False
    # oben links
    if is_valid_point(i-1, j-1, GRID_SIZE):
        if not lines[i-1][j-1].isdigit() and lines[i-1][j-1] != '.':
            if lines[i-1][j-1] == '*':
                return True, i-1, j-1
            result = True
    # oben mitte
    if is_valid_point(i-1, j, GRID_SIZE):
        if not lines[i-1][j].isdigit() and lines[i-1][j] != '.':
            if lines[i-1][j] == '*':
                return True, i-1, j
            result = True
    # oben rechts
    if is_valid_point(i-1, j+1, GRID_SIZE):
        if not lines[i-1][j+1].isdigit() and lines[i-1][j+1] != '.':
            if lines[i-1][j+1] == '*':
                return True, i-1, j+1
            result = True
    # mitte links
    if is_valid_point(i, j-1, GRID_SIZE):
        if not lines[i][j-1].isdigit() and lines[i][j-1] != '.':
            if lines[i][j-1] == '*':
                return True, i, j-1
            result = True
    # mitte rechts
    if is_valid_point(i, j+1, GRID_SIZE):
        if not lines[i][j+1].isdigit() and lines[i][j+1] != '.':
            if lines[i][j+1] == '*':
                return True, i, j+1
            result = True
    # unten links
    if is_valid_point(i+1, j-1, GRID_SIZE):
        if not lines[i+1][j-1].isdigit() and lines[i+1][j-1] != '.':
            if lines[i+1][j-1] == '*':
                return True, i+1, j-1
            result = True
    # unten mitte
    if is_valid_point(i+1, j, GRID_SIZE):
        if not lines[i+1][j].isdigit() and lines[i+1][j] != '.':
            if lines[i+1][j] == '*':
                return True, i+1, j
            result = True
    # unten rechts
    if is_valid_point(i+1, j+1, GRID_SIZE):
        if not lines[i+1][j+1].isdigit() and lines[i+1][j+1] != '.':
            if lines[i+1][j+1] == '*':
                return True, i+1, j+1
            result = True
    return result, -1, -1


def is_valid_point(y, x, grid_size):
    if 0 <= x <= grid_size and 0 <= y <= grid_size:
        # print(f"{y}|{x} is valid")
        return True
    else:
        return False


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()


# Notes
# Letzte Zeile an punkten hinzufügen
