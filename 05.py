import math

# Open the file and split on new lines
with open("input05.txt") as file:
    data = file.read().strip().split("\n\n")

seeds = [int(seed) for seed in data[0].split(" ")[1:]]

# Part 1

seed_to_soil = [
    [int(x) for x in line.split(" ")] for line in data[1].split("\n")[1:]
]
soil_to_fertilizer = [
    [int(x) for x in line.split(" ")] for line in data[2].split("\n")[1:]
]
fertilizer_to_water = [
    [int(x) for x in line.split(" ")] for line in data[3].split("\n")[1:]
]
water_to_light = [
    [int(x) for x in line.split(" ")] for line in data[4].split("\n")[1:]
]
light_to_temperature = [
    [int(x) for x in line.split(" ")] for line in data[5].split("\n")[1:]
]
temperature_to_humidity = [
    [int(x) for x in line.split(" ")] for line in data[6].split("\n")[1:]
]
humidity_to_location = [
    [int(x) for x in line.split(" ")] for line in data[7].split("\n")[1:]
]


def get_destination(num, map):
    for line in map:
        destination, source, range_length = line
        if num in range(source, source + range_length):
            return destination + (num - source)
    return num


locations = []

for seed in seeds:
    soil = get_destination(seed, seed_to_soil)
    fertilizer = get_destination(soil, soil_to_fertilizer)
    water = get_destination(fertilizer, fertilizer_to_water)
    light = get_destination(water, water_to_light)
    temperature = get_destination(light, light_to_temperature)
    humidity = get_destination(temperature, temperature_to_humidity)
    location = get_destination(humidity, humidity_to_location)
    locations.append(location)

print(
    "What is the lowest location number that corresponds to any of the initial seed numbers?",
    min(locations),
)

# Part 2

# Think of everything as intervals and offsets


def intersect_intervals(interval1, interval2):
    """
    Return the intersection of two intervals.
    """
    x_min, x_max = interval1
    y_min, y_max = interval2
    intersect_min = max(x_min, y_min)
    intersect_max = min(x_max, y_max)
    if intersect_min < intersect_max:
        intersection = (intersect_min, intersect_max)
    else:
        intersection = None, None
    return intersection


def merge_intervals(intervals):
    """
    Return a list of merged intervals.
    """
    vals = []
    for x_min, x_max in intervals:
        if vals and vals[-1] == x_min:
            vals.pop(-1)
            vals.append(x_max)
        else:
            vals.append(x_min)
            vals.append(x_max)
    return [
        (vals[2 * idx], vals[2 * idx + 1]) for idx in range(len(vals) // 2)
    ]


source_intervals = [
    (seeds[2 * idx], seeds[2 * idx] + seeds[2 * idx + 1])
    for idx in range(len(seeds) // 2)
]

for row in data[1:]:
    row = [[int(x) for x in line.split(" ")] for line in row.split("\n")[1:]]

    # Intervals of the form (source_min, source_max, offset)
    intervals = [
        (source, source + range_length, destination - source)
        for destination, source, range_length in row
    ]
    intervals.sort()

    # Store gaps where there is no offset
    gaps = [(-math.inf, intervals[0][0])]
    for idx in range(len(intervals) - 1):
        prev_max, next_min = intervals[idx][1], intervals[idx + 1][0]
        if prev_max != next_min:
            gaps.append((prev_max, next_min))
    gaps.append((intervals[-1][1], math.inf))

    # Transform the data
    transformed = []
    for x_min, x_max in source_intervals:
        for y_min, y_max, offset in intervals:
            z_min, z_max = intersect_intervals((x_min, x_max), (y_min, y_max))
            if z_min:
                transformed.append((z_min + offset, z_max + offset))

    # print("Transformed with offsets", transformed)

    for x_min, x_max in source_intervals:
        for y_min, y_max in gaps:
            z_min, z_max = intersect_intervals((x_min, x_max), (y_min, y_max))
            if z_min:
                transformed.append((z_min, z_max))

    transformed.sort()
    source_intervals = merge_intervals(transformed)
    # print(source_intervals)

print(
    "What is the lowest location number that corresponds to any of the initial seed numbers?",
    min([x_min for x_min, x_max in source_intervals]),
)
