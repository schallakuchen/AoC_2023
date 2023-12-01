import re


def d01():
    lines = open(f"inputs\\d01.txt").read().strip().split("\n")

    # PART 1
    calibration_sum = 0
    for line in lines:
        digits = re.findall(r"\d", line)
        number = int(digits[0]) * 10 + int(digits[-1])
        calibration_sum += number

    print("Part 1: " + str(calibration_sum))
    calibration_sum = 0
    search_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in lines:
        i = 0
        digits = []
        while i < len(line):
            if line[i].isdigit():
                digits.append(int(line[i]))
            else:
                partLine = line[i:]
                j = 1
                for word in search_strings:
                    if partLine.startswith(word):
                        digits.append(j)
                    j += 1
            i += 1
        #print(digits)
        calibration_sum += int(digits[0]) * 10 + int(digits[-1])

    print("Part 2: " + str(calibration_sum))


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()