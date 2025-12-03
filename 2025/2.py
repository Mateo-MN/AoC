from pathlib import Path


def part1_pair(n1, n2):
    score = 0
    for i in range(n1, n2+1):
        i_s = str(i)
        if i_s[:(len(i_s) >> 1)] == i_s[(len(i_s) >> 1):]:
            score += i
    return score


def get_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def part2_pair(n1, n2):
    score = 0
    for i in range(n1, n2+1):
        i_s = str(i)
        for divisor in get_divisors(len(i_s)):
            pattern = i_s[:divisor]
            repeating = True
            for j in range(2*divisor, len(i_s) + 1, divisor):
                if i_s[(j-divisor):j] == pattern:
                    continue
                repeating = False
                break
            if repeating == True:
                score += i
                break
    return score


score = 0
with open(Path(__file__).parent / "2.txt", "r") as file:
    for line in file:
        
        for pair in line.split(","):
            n1, n2 = pair.split("-")
            score += part2_pair(int(n1), int(n2))
        break
print(score)