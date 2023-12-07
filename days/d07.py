class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.hand_type = self.determine_type()
        self.rank = 0

    def determine_type(self):
        card_dict = {}
        for card in self.hand:
            if card in card_dict:
                card_dict[card] += 1
            else:
                card_dict[card] = 1
        sorted_dict = sorted(card_dict.values(), reverse=True)

        if 5 in sorted_dict:
            return 1
        elif 4 in sorted_dict:
            return 2
        elif sorted_dict == [3, 2] or sorted_dict == [2, 3]:
            return 3
        elif 3 in sorted_dict:
            return 4
        elif sorted_dict.count(2) == 2:
            return 5
        elif 2 in sorted_dict:
            return 6
        else:
            return 7

    def card_values(self):
        values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        card_values_list = []

        for card in self.hand:
            if card in values:
                card_values_list.append(values[card])
            elif card.isdigit():
                card_values_list.append(int(card))
            else:
                print("You fu**ed up")

        return card_values_list


def d07():
    lines = open(f"inputs\\d07.txt").read().strip().split("\n")

    result_part1 = 0
    result_part2 = 0

    hands = [Hand(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]

    sort_hands(hands)

    for i, hand in enumerate(hands):
        hand.rank = i + 1

    for hand in hands:
        print(f"Rank: {hand.rank}, Hand: {hand.hand}, Type: {hand.hand_type}, Bid: {hand.bid}, Winning Amount: {hand.rank * hand.bid}")
        print(hand.card_values())
        result_part1 += hand.rank * hand.bid
        print(result_part1)

    print(f"Part 1: {result_part1}")


def sort_hands(hands):
    for i in range(len(hands)):
        for j in range(0, len(hands) - i - 1):
            if check_swap(hands[j], hands[j+1]):
                temp_hand = hands[j]
                hands[j] = hands[j+1]
                hands[j+1] = temp_hand


def check_swap(hand1, hand2):
    if hand1.hand_type < hand2.hand_type:
        return True
    elif hand1.hand_type > hand2.hand_type:
        return False
    else:
        for card_h1, card_h2 in zip(hand1.card_values(), hand2.card_values()):
            if card_h1 > card_h2:
                return True
            elif card_h1 < card_h2:
                return False
        return False


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
