from collections import Counter

'''
# 1
letter_map = {
    'A': 'E',
    'K': 'D',
    'Q': 'C',
    'J': 'B',
    'T': 'A',
}

def hand_type(hand):
    count = sorted(list(Counter(hand).values()))
    match count:
        case [5]:
            return 6
        case [_, 4]:
            return 5
        case [2, 3]:
            return 4
        case [*_, 3]:
            return 3
        case [_, 2, 2]:
            return 2
        case [*_, 2]:
            return 1
        case _:
            return 0

def strength(hand):
    return (hand_type(hand), [letter_map.get(card, card) for card in hand])

hands = []

with open('7.txt') as f:
    for line in f.readlines():
        hand, bid = line.split()
        hands.append((hand, int(bid)))

hands.sort(key=lambda x: strength(x[0]))

res = 0
for rank, (hand, bid) in enumerate(hands, 1):
    res += bid * rank
print(res)
'''

# 2
letter_map = {
    'A': 'D',
    'K': 'C',
    'Q': 'B',
    'T': 'A',
    'J': '.',
}

def hand_type(hand):
    j = hand.count('J')
    count = sorted(list(Counter(hand).values()))

    match (count, j):
        case ([5], _):
            return 6

        case ([_, 4], 0):
            return 5
        case ([_, 4], 1|4):
            return 6

        case ([2, 3], 0):
            return 4
        case ([2, 3], 2|3):
            return 6

        case ([*_, 3], 0):
            return 3
        case ([*_, 3], 1|3):
            return 5

        case ([_, 2, 2], 0):
            return 2
        case ([_, 2, 2], 1):
            return 4
        case ([_, 2, 2], 2):
            return 5

        case ([*_, 2], 0):
            return 1
        case ([*_, 2], 1|2):
            return 3

        case ([*_], 0):
            return 0
        case ([*_], 1):
            return 1

def strength(hand):
    return (hand_type(hand), [letter_map.get(card, card) for card in hand])


hands = []
with open('7.txt') as f:
    for line in f.readlines():
        hand, bid = line.split()
        hands.append((hand, int(bid)))

hands.sort(key=lambda x: strength(x[0]))
# print(hands)

res = 0
for rank, (hand, bid) in enumerate(hands, 1):
    res += bid * rank
print(res)
