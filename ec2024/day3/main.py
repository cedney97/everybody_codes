from util.main import parse_file_to_lines, print_grid

test_file = "ec2024/day3/test.txt"
input_file = "ec2024/day3/input.txt"
lines = parse_file_to_lines(input_file)

orth_deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
diag_deltas = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1))

def part_1(deltas=orth_deltas):
    
    def blank_marked():
        return [[False for _ in row] for row in lines]

    def check_elevation(curr: int, r: int, c: int, elevations: list[list[int]]):
        if r < 0 or r >= len(elevations): return False
        if c < 0 or c >= len(elevations[r]): return False

        return elevations[r][c] == curr

    def dig(elevations: list[list[int]], step: int):
        marked = blank_marked()
        for r in range(len(elevations)):
            for c in range(len(elevations[r])):
                if elevations[r][c] == step:
                    valid = True
                    for dr, dc in deltas:
                        if not check_elevation(elevations[r][c], r + dr, c + dc, elevations):
                            valid = False

                    if valid:
                        marked[r][c] = True
                    del valid

        num_marked = 0

        for r in range(len(marked)):
            for c in range(len(marked[r])):
                if marked[r][c]:
                    elevations[r][c] += 1        
                    num_marked += 1

        return elevations, num_marked

    elevations = [[-1 if c == "." else 1 for c in row ] for row in lines]

    result = sum([sum([1 if c == 1 else 0 for c in r]) for r in elevations])
    prev_result = 0
    step = 1

    while prev_result != result:
        elevations, num_marked = dig(elevations, step)
        prev_result = result
        result += num_marked
        step += 1
    
    print_grid(elevations)
    print(result)


def part_2():
    part_1()

def part_3():
    part_1(diag_deltas)

if __name__ == "__main__":
    part_3()