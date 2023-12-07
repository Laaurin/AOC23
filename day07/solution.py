class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.numbers = self.get_cards(cards)
        self.bid = bid
        self.type = self.get_type()
        self.upgrade_type()

    def get_type(self):
        print(self.cards)
        self.card_count = {}
        for card in self.cards:
            if card == 'J':
                continue
            if card in self.card_count:
                self.card_count[card] += 1
            else:
                self.card_count[card] = 1
        multiples = []
        for key in self.card_count.keys():
            if self.card_count[key] == 5:
                return 7
            elif self.card_count[key] == 4:
                return 6
            if self.card_count[key] == 3:
                multiples.append(3)
            elif self.card_count[key] == 2:
                multiples.append(2)
        print(multiples)
        print("--")
        if 3 in multiples:
            if 2 in multiples:
                return 5
            return 4
        if multiples == [2, 2]:
            return 3
        if multiples == [2]:
            return 2
        return 1


    def upgrade_type(self):
        amount = self.cards.count('J')
        if amount == 0:
            return
        if self.type == 6:
            new_val = get_key_by_value(self.card_count, 4)
            self.cards = self.cards.replace("J", new_val)
        elif self.type == 5 or self.type == 4:
            new_val = get_key_by_value(self.card_count, 3)
            self.cards = self.cards.replace("J", new_val)
        elif self.type == 3 or self.type == 2:
            new_val = get_key_by_value(self.card_count, 2)
            self.cards = self.cards.replace("J", new_val)
        elif self.type == 1:
            if amount == 5:
                new_val = "A"
            else:
                new_val = get_key_by_value(self.card_count, 1)
            self.cards = self.cards.replace("J", new_val)
        self.type = self.get_type()
        self.numbers = self.get_cards(self.cards)


    def get_cards(self, cards):
        numbered = []
        for card in cards:
            if card.isdigit():
                numbered.append(int(card))
            elif card == 'T':
                numbered.append(10)
            elif card == 'J':
                numbered.append(11)
            elif card == 'Q':
                numbered.append(12)
            elif card == 'K':
                numbered.append(13)
            elif card == 'A':
                numbered.append(14)
        return numbered


def s1():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())

    hands = []
    for line in lines:
        info = line.split()
        hands.append(Hand(info[0], int(info[1])))

    hand_types = [[] for i in range(7)]
    for hand in hands:
        hand_types[hand.type - 1].append(hand)

    for i in range(len(hand_types)):
        hand_types[i] = sorted(hand_types[i], key=get_nums)

    solution = 0
    multiplier = 1
    for i in hand_types:
        for j in i:
            print(j.cards)
            solution += multiplier * j.bid
            multiplier += 1
    print(solution)


def get_type(hand):
    return hand.type


def get_nums(hand):
    return hand.numbers

def get_key_by_value(dictionary, target_value):
    keys = []
    for key, value in dictionary.items():
        if value == target_value:
            keys.append(key)
    if len(keys) > 0:
        numbers = get_
    return None
s1()
