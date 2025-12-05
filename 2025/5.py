from pathlib import Path

with open(Path(__file__).parent / "5.txt", "r") as file:
    data = file.read()
    
[ranges, IDs] = data.split("\n\n")
ranges = [tuple(map(int, pair.split("-"))) for pair in ranges.split("\n")]

def part1(ranges, IDs):
    fresh = 0
    for ID in map(int, IDs.split("\n")):
        for range in ranges:
            if range[0] <= ID and ID <= range[1]:
                fresh += 1
                break
    return fresh

def part2(ranges):
    sorted_rages = sorted(ranges, key=lambda x: x[0])
    
    discontinuous_ranges = []
    current_range = list(sorted_rages[0])
    for range in sorted_rages[1:]:
        if range[0] <= current_range[1]:
            if current_range[1] < range[1]:
                current_range[1] = range[1]
        else:
            discontinuous_ranges.append(tuple(current_range))
            current_range = list(range)
    discontinuous_ranges.append(tuple(current_range))
    
    sol = 0
    for range in discontinuous_ranges:
        sol += range[1] - range[0] + 1
    return sol

print("Part1:", part1(ranges, IDs))
print("Part2:", part2(ranges))