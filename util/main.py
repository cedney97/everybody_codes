from typing import Any


def parse_file_to_char_array(file_name: str):
    with open(file_name) as file:
        lines = []
        for line in file:
            lines.append([c for c in line.strip()])
        return lines

def parse_file_to_lines(file_name: str):
    with open(file_name) as file:
        lines = []
        for line in file:
            lines.append(line.strip())
        return lines
    
def print_grid(grid: list[list[Any]]):
    longest = max([max([len(str(col)) for col in row]) for row in grid])
    for row in grid:
        row_str = ""
        for col in row:
            row_str += str(col).rjust(longest) + " "
        print(row_str)