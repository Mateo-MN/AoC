from pathlib import Path

rotations = []
with open(Path(__file__).parent / "1.txt", "r") as input_file:
    for line in input_file:
        rotations.append([line[0], int(line[1:])])

def part1(rotations, dial=50):
    score = 0
    for rotation in rotations:
        dial += rotation[1] * (1 if rotation[0] == "R" else -1)
        dial %= 100

        if dial == 0:
            score += 1
    return score

def part2(rotations, dial=50):
    score = 0
    just_0 = False
    for rotation in rotations:
        if rotation[1] / 100 >= 1:
            score += int(rotation[1] / 100)
            rotation[1] %= 100
        
        dial += rotation[1] * (1 if rotation[0] == "R" else -1)
        if dial != dial % 100 and not just_0 and dial % 100 != 0:
            score += 1
        dial %= 100
        
        if dial == 0:
            just_0 = True
            score += 1
        else:
            just_0 = False
    return score

print("Part1:", part1(rotations))
print("Part2:", part2(rotations))