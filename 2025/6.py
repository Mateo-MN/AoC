import numpy as np
from pathlib import Path

def part1():
    data = []
    with open(Path(__file__).parent / "6.txt", "r") as file:
        for line in file:
            data.append(line.split())
           
    sol = 0
    for j in range(len(data[0])):
        op = data[-1][j]
        num = int(data[0][j])
        for i in range(len(data) - 2, 0, -1):
            if op == "+":
                num += int(data[i][j])
            else:
                num *= int(data[i][j])
        sol += num  
    return sol  

def part2():
    data = []
    with open(Path(__file__).parent / "6.txt", "r") as file:
        for line in file:
            data.append(line[:-1])
    number_groups = []
    current_group = []
    for i in range(len(data[0])):
        number = ""
        for line in data[:-1]:
            number += line[i]
        number = number.strip(" ")
        if number != "":
            current_group.append(int(number))
            continue
        number_groups.append(current_group)
        current_group = []
    number_groups.append(current_group)
    
    sol = 0
    for i, op in enumerate(data[-1].split()):
        num = number_groups[i][0]
        for n in number_groups[i][1:]:
            if op == "*":
                num *= n
            else:
                num += n
        sol += num
    return sol
        
            
print(part2())
