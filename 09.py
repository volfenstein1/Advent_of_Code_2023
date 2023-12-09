with open("input09.txt") as file:
    data = file.read().strip().split("\n")

data = [[int(x) for x in line.split(" ")] for line in data]


# Part 1


def get_next_val(sequence):
    """Return the next value of the sequence."""
    rows = [sequence]
    while any(rows[-1]):
        next_row = [
            rows[-1][idx] - rows[-1][idx - 1]
            for idx in range(1, len(rows[-1]))
        ]
        rows.append(next_row)
    return sum(row[-1] for row in rows)


res = 0
for sequence in data:
    res += get_next_val(sequence)
print("What is the sum of these extrapolated values?", res)

# Part 2


def get_prev_val(sequence):
    """Return the previous value of the sequence."""
    rows = [sequence]
    while any(rows[-1]):
        next_row = [
            rows[-1][idx] - rows[-1][idx - 1]
            for idx in range(1, len(rows[-1]))
        ]
        rows.append(next_row)
    res = 0
    for num in [row[0] for row in rows[::-1]]:
        res = num - res
    return res


res = 0
for sequence in data:
    res += get_prev_val(sequence)
print(
    "Analyze your OASIS report again, this time extrapolating the previous "
    " value for each history. What is the sum of these extrapolated values?",
    res,
)
