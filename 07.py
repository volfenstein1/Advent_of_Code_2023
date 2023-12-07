from typing import Counter


with open("input07.txt") as file:
    data = file.read().strip().split("\n")

data = [line.split(" ") for line in data]


# Part 1


def rank(cards):
    """Return the score of a set of cards."""
    freq = Counter(cards)
    freq = sorted(list(freq.values()))
    order = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    # Get the type of the cards
    if freq == [5]:
        type = 7
    elif freq == [1, 4]:
        type = 6
    elif freq == [2, 3]:
        type = 5
    elif freq == [1, 1, 3]:
        type = 4
    elif freq == [1, 2, 2]:
        type = 3
    elif freq == [1, 1, 1, 2]:
        type = 2
    else:
        type = 1
    tiebreaker = [order[card] for card in cards]
    return [type] + tiebreaker


data.sort(key=lambda x: rank(x[0]))

res = 0
for idx, line in enumerate(data):
    res += (idx + 1) * int(line[1])

print("What are the total winnings?", res)

# Part 2


def joker(cards):
    """Return the score of a set of cards, where jokers are wild."""
    freq = Counter(cards)
    jokers = freq["J"]
    del freq["J"]
    freq = sorted(list(freq.values()))
    if freq:
        freq[-1] += jokers
    else:
        freq = [jokers]
    order = {
        "J": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    # Get the type of the cards with jokers wild
    if freq == [5]:
        type = 7
    elif freq == [1, 4]:
        type = 6
    elif freq == [2, 3]:
        type = 5
    elif freq == [1, 1, 3]:
        type = 4
    elif freq == [1, 2, 2]:
        type = 3
    elif freq == [1, 1, 1, 2]:
        type = 2
    else:
        type = 1
    tiebreaker = [order[card] for card in cards]
    return [type] + tiebreaker


data.sort(key=lambda x: joker(x[0]))

res = 0
for idx, line in enumerate(data):
    res += (idx + 1) * int(line[1])

print(
    "Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?",
    res,
)
