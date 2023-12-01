with open("input01") as file:
    data = file.read().strip().split("\n")

# Part 1
calibration_vals = [[char for char in word if char.isdigit()] for word in data]
calibration_ints = [word[0] + word[-1] for word in calibration_vals if word]

res = 0
for numbers in calibration_ints:
    res += int(numbers)

print("Sum of calibration values", res)

# Part 2
calibration_vals = []
for row in data:
    new_row = []
    for idx in range(len(row)):
        if row[idx].isdigit():
            new_row.append(row[idx])
        elif row[idx:].startswith("one"):
            new_row.append("1")
        elif row[idx:].startswith("two"):
            new_row.append("2")
        elif row[idx:].startswith("three"):
            new_row.append("3")
        elif row[idx:].startswith("four"):
            new_row.append("4")
        elif row[idx:].startswith("five"):
            new_row.append("5")
        elif row[idx:].startswith("six"):
            new_row.append("6")
        elif row[idx:].startswith("seven"):
            new_row.append("7")
        elif row[idx:].startswith("eight"):
            new_row.append("8")
        elif row[idx:].startswith("nine"):
            new_row.append("9")
    calibration_vals.append(new_row)

calibration_ints = [word[0] + word[-1] for word in calibration_vals]

res = 0
for numbers in calibration_ints:
    res += int(numbers)

print("Sum of calibration vals including alphanumeric", res)
