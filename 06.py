# Open the file and split on new lines
with open("input06.txt") as file:
    data = file.read().strip().split("\n")


def quadratic(a, b, c):
    """Solve the quadratic ax^2 + bx + c = 0."""
    return (
        int((1 / (2 * a)) * (-b + (b**2 - 4 * a * c) ** (1 / 2))),
        int((1 / (2 * a)) * (-b - (b**2 - 4 * a * c) ** (1 / 2))),
    )


# Part 1
times = [int(x.strip()) for x in data[0].split(" ")[1:] if x]
distances = [int(x.strip()) for x in data[1].split(" ")[1:] if x]

number_of_ways = []
for time, distance in zip(times, distances):
    x_0, x_1 = quadratic(-1, time, -distance)
    number_of_ways.append(min(time, x_1) - x_0)

res = 1
for ways in number_of_ways:
    res *= ways

print(
    "Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?",
    res,
)

# Part 2
time = int("".join([x.strip() for x in data[0].split(" ")[1:] if x]))
distance = int("".join([x.strip() for x in data[1].split(" ")[1:] if x]))

x_0, x_1 = quadratic(-1, time, -distance)

print(
    "How many ways can you beat the record in this one much longer race?",
    min(time, x_1) - x_0,
)
