# Open the file and split on new lines
with open("input04.txt") as file:
    data = file.read().strip().split("\n")

data = [line.replace(":", "|").split("|")[1:3] for line in data]
data = [[game.split(" ") for game in line] for line in data]

# Part 1
res = 0
for line in data:
    winning_numbers = set(line[0])
    matches = 0
    for num in line[1]:
        if num and num in winning_numbers:
            matches += 1
    if matches:
        res += 2 ** (matches - 1)

print("How many points are they worth in total?", res)

# Part 2

cards = [1] * len(data)
res = 0
for idx, line in enumerate(data):
    winning_numbers = set(line[0])
    matches = 0
    for num in line[1]:
        if num and num in winning_numbers:
            matches += 1
    for x in range(idx + 1, min(len(data), idx + matches + 1)):
        cards[x] += cards[idx]

res = sum(cards)
print("How many total scratchcards do you end up with?", res)
