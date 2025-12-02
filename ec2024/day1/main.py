from typing import Counter
from util.main import parse_file_to_lines

test_file = "ec2024/day1/test.txt"
input_file = "ec2024/day1/input.txt"
current_file = input_file

potion_map = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5
}

def part_1():
    lines = parse_file_to_lines(current_file)
    enemies = lines[0]
    counter = Counter(enemies)
    result = 0
    for key in counter:
        result += counter[key] * potion_map.get(key, 0)
    print(result)

def part_2():
    lines = parse_file_to_lines(current_file)
    enemies = lines[0]
    pairs = [enemies[i:i + 2] for i in range(0, len(enemies), 2)]
    result = 0
    for pair in pairs:
        x, y = pair[0], pair[1]
        additional = 0
        if "x" not in [x, y]:
            additional = 1
        result += potion_map.get(x, 0) + additional
        result += potion_map.get(y, 0) + additional
    print(result)

def part_3():
    lines = parse_file_to_lines(current_file)
    enemies = lines[0]
    groups = [enemies[i:i + 3] for i in range(0, len(enemies), 3)]
    result = 0
    for group in groups:
        group = [enemy for enemy in group if enemy != "x"]
        additional = len(group) - 1
        new_potions = 0
        for g in group:
            new_potions += potion_map.get(g, 0) + additional
        # print(group)
        # print(additional)
        # print(new_potions)
        result += new_potions
    print(result)

if __name__ == "__main__":
    part_3()