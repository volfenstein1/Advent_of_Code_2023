# Open the file and split on new lines
from typing import DefaultDict


with open("input03.txt") as file:
    data = file.read().strip().split("\n")

# Augment the data
data = ["." + line + "." for line in data]
data = ["." * len(data[0])] + data + ["." * len(data[0])]

for line in data:
    print(line)

# Part 1
res = 0
for idx_row, row in enumerate(data):
    for idx_col, char in enumerate(row):
        if (
            0 < idx_row < len(data) - 1
            and idx_col < len(row) - 1
            and not char.isdigit()
        ):
            num = 0
            num_length = 0
            # We have found a string of digits
            while row[idx_col + 1 + num_length].isdigit():
                num = 10 * num + int(row[idx_col + 1 + num_length])
                num_length += 1
            # Check if there is a nearby symbol
            if num:
                nearby = False
                for char in data[idx_row - 1][
                    idx_col : idx_col + 2 + num_length
                ]:
                    if not char.isdigit() and char != ".":
                        nearby = True
                for char in data[idx_row][idx_col : idx_col + 2 + num_length]:
                    if not char.isdigit() and char != ".":
                        nearby = True
                for char in data[idx_row + 1][
                    idx_col : idx_col + 2 + num_length
                ]:
                    if not char.isdigit() and char != ".":
                        nearby = True
                if nearby:
                    res += num

print(
    "What is the sum of all of the part numbers in the engine schematic?", res
)

# Part 2

# Find the gears, store them in a dictionary
# gears = {}
# for idx_row, row in enumerate(data):
#     for idx_col, char in enumerate(row):
#         if char == '*':
#             gears[(idx_row, idx_col)] = set()

gears = DefaultDict(list)

for idx_row, row in enumerate(data):
    for idx_col, char in enumerate(row):
        if (
            0 < idx_row < len(data) - 1
            and idx_col < len(row) - 1
            and not char.isdigit()
        ):
            num = 0
            num_length = 0
            # We have found a string of digits
            while row[idx_col + 1 + num_length].isdigit():
                num = 10 * num + int(row[idx_col + 1 + num_length])
                num_length += 1
            # Check if there is a nearby gear
            if num:
                for loc_row in range(idx_row - 1, idx_row + 2):
                    for loc_col in range(idx_col, idx_col + 2 + num_length):
                        if data[loc_row][loc_col] == "*":
                            print(loc_row, loc_col)
                            gears[(loc_row, loc_col)].append(num)

res = 0
for key in gears:
    if len(gears[key]) == 2:
        res += gears[key][0] * gears[key][1]

print(
    "What is the sum of all of the gear ratios in your engine schematic?", res
)
