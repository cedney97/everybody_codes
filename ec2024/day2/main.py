import re
from util.main import parse_file_to_lines, print_grid

test_file = "ec2024/day2/test.txt"
input_file = "ec2024/day2/input.txt"
lines: list[str] = parse_file_to_lines(input_file)

deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))

def part_1():
    keys = lines[0]
    keys = keys[6:].split(",")

    inscription = lines[2]
    words = inscription.split(" ")

    num_words = 0
    for word in words:
        for key in keys:
            if key in word:
                num_words += 1
    
    print(num_words)

def counted_symbols(word: str, keys: list[str]):
    counted_indices = set()

    for key in keys:
        start = 0
        while True:
            index = word.find(key, start)
            if index == -1:
                break

            for i in range(index, index + len(key)):
                counted_indices.add(i)
            
            start = index + 1

    return len(counted_indices)

def part_2():
    keys = lines[0]
    keys = keys[6:].split(",")
    keys = keys + list(set(["".join(key[::-1]) for key in keys]))

    inscriptions = lines[2:]
    num_symbols = 0
    for inscription in inscriptions:
        # print(inscription)
        counted = 0
        for word in inscription.split(" "):
            counted += counted_symbols(word, keys)
        # print(counted)
        num_symbols += counted
    print(num_symbols)

def check_direction(grid: list[str], r: int, c: int, dr: int, dc: int, key: str, acc: str):
    if r < 0 or r >= len(grid):
        return False
    while c < 0:
        c += len(grid[r])
    while c >= len(grid[r]):
        c -= len(grid[r])

    acc += grid[r][c]
    if len(acc) < len(key):
        return check_direction(grid, r + dr, c + dc, dr, dc, key, acc)
    
    return acc == key

def mark_direction(scales, r: int, c: int, dr: int, dc: int, steps: int):
    if r < 0 or r >= len(scales):
        return False
    while c < 0:
        c += len(scales[r])
    while c >= len(scales[r]):
        c -= len(scales[r])
    
    if steps == 0:
        return
    
    scales[r][c] = True
    mark_direction(scales, r + dr, c + dc, dr, dc, steps - 1)

def part_3():
    keys = lines[0]
    keys = keys[6:].split(",")

    grid = lines[2:]
    scales = [[False for _ in row] for row in grid]
    
    for key in keys:
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == key[0]:
                    for dr, dc in deltas:
                        if check_direction(grid, r, c, dr, dc, key, ""):
                            mark_direction(scales, r, c, dr, dc, len(key))

    result = 0
    for row in scales:
        for col in row:
            if col: result += 1
    # print_grid(scales)
    print(result)

if __name__ == "__main__":
    part_3()