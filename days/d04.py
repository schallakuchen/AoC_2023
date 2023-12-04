import re


def d04():
    lines = open(f"inputs\\d04.txt").read().strip().split("\n")
    sum_part1 = 0
    sum_part2 = 0

    # Part 1
    for card_id, line in enumerate(lines):
        winning_numbers_string = line.split(':')[1].strip().split('|')[0]
        your_numbers_string = line.split(':')[1].strip().split('|')[1]

        winning_numbers = re.findall(r"\d+", your_numbers_string)
        your_numbers = re.findall(r"\d+", winning_numbers_string)

        common_numbers = list(set(winning_numbers).intersection(set(your_numbers)))

        card_points = 1
        if len(common_numbers) > 0:
            for cn in common_numbers:
                card_points *= 2
            card_points /= 2
        else:
            card_points = 0

        sum_part1 += card_points

    # sum_part1 is a float after the division
    print(int(sum_part1))

    # Part 2
    cards = []
    for line in lines:
        winning_numbers_string = line.split(':')[1].strip().split('|')[0]
        your_numbers_string = line.split(':')[1].strip().split('|')[1]

        winning_numbers = set(map(int, re.findall(r"\d+", winning_numbers_string)))
        your_numbers = set(map(int, re.findall(r"\d+", your_numbers_string)))

        cards.append((winning_numbers, your_numbers))

    card_instances = [1] * len(cards)

    for i, (winning_numbers, player_numbers) in enumerate(cards):
        num_of_common_numbers = len(winning_numbers & player_numbers)
        for j in range(i + 1, i + 1 + num_of_common_numbers):
            card_instances[j] += card_instances[i]

    sum_part2 = (sum(card_instances))
    print(sum_part2)


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
