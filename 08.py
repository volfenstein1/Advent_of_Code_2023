from math import lcm

with open("input08.txt") as file:
    data = file.read().strip().split("\n\n")

instructions = data[0]
network = {}
for line in data[1].split("\n"):
    network[line[:3]] = (line[7:10], line[12:15])


def search_network(cur):
    count = 0
    while True:
        for left_right in instructions:
            count += 1
            if left_right == "L":
                cur = network[cur][0]
            else:
                cur = network[cur][1]
            if cur == "ZZZ":
                return count


# Part 1
print("How many steps are required to reach ZZZ?", search_network("AAA"))

# Part 2

# Find the starting points
starts = []
for node in network:
    if node[-1] == "A":
        starts.append(node)


def search_network_last(cur):
    count = 0
    while True:
        for left_right in instructions:
            count += 1
            if left_right == "L":
                cur = network[cur][0]
            else:
                cur = network[cur][1]
            if cur[-1] == "Z":
                return count


print(
    "How many steps does it take before you're only on nodes that end with Z?",
    lcm(*[search_network_last(node) for node in starts]),
)
