# Open the file and split on new lines
with open("input02.txt") as file:
    data = file.read().strip().split("\n")

data = [line.split(":")[1].replace(",", "").split(";") for line in data]


def red_green_blue(game):
    red, green, blue = 0, 0, 0
    game_split = game.split(" ")
    for idx, term in enumerate(game_split):
        if term == "red":
            red = int(game_split[idx - 1])
        if term == "green":
            green = int(game_split[idx - 1])
        if term == "blue":
            blue = int(game_split[idx - 1])
    return (red, green, blue)


# Each row is a list of tuples (red, green, blue)
data = [[red_green_blue(game) for game in line] for line in data]

# Part 1

res = 0

max_red = 12
max_green = 13
max_blue = 14

for idx, line in enumerate(data):
    if all(
        [
            game[0] <= max_red and game[1] <= max_green and game[2] <= max_blue
            for game in line
        ]
    ):
        res += idx + 1

print("Sum of game IDs:", res)

# Part 2

res = 0

for line in data:
    res += (
        max([game[0] for game in line])
        * max([game[1] for game in line])
        * max([game[2] for game in line])
    )

print("Sum of the power of these sets:", res)
