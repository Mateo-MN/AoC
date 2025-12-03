from pathlib import Path

def part1(n: str) -> int:
    biggest = smallest = 0
    for i in range(len(n)):
        s = int(n[i])
        if s > biggest and i + 1 < len(n):
            biggest = s
            smallest = 0
        elif s > smallest:
            smallest = s
    return biggest * 10 + smallest

def part2(n: str, d: int) -> int:
    biggest = [0 for i in range(d)]
    for i in range(len(n)):
        s = int(n[i])
        for j in range(len(biggest)):
            if s > biggest[j] and i + (d - (j+1)) < len(n):
                biggest[j] = s
                biggest[j+1:d] = [0] * (d - (j+1))
                break
    print(n, sum(biggest[i] * 10**((d - 1) - i) for i in range(d)))
    return sum(biggest[i] * 10**((d - 1) - i) for i in range(d))
    
score1 = score2 = 0
with open(Path(__file__).parent / "3.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        score1 += part1(line)
        score2 += part2(line, 12)
print(score2)
