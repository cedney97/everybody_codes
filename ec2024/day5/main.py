from typing import Counter
from util.main import parse_file_to_lines, print_grid, transpose_grid

test_file = "ec2024/day5/test.txt"
input_file = "ec2024/day5/input.txt"
lines = parse_file_to_lines(input_file)

def end_number(cols: list[list[int]]):
    result = "".join([str(col[0]) for col in cols])
    return int(result)

def simulate_dance(cols, start_col, num_times, counter=None):
    col_idx = start_col
    right_col_idx = (start_col + 1) % len(cols)

    while num_times > 0:
        num_times -= 1

        clapper = cols[col_idx].pop(0)

        col = cols[right_col_idx]
        n = len(col)

        path = list(range(n)) + list(range(n - 1, -1, -1))
        cycle_length = len(path)  # = 2*n

        step_index = (clapper - 1) % cycle_length
        target = path[step_index]

        left_side = (step_index < n)

        if left_side:
            insert_idx = target          # in front of dancer
        else:
            insert_idx = target + 1      # behind dancer

        col.insert(insert_idx, clapper)

        col_idx = (col_idx + 1) % len(cols)
        right_col_idx = (right_col_idx + 1) % len(cols)

        shout = end_number(cols)

        if counter is not None:
            counter[shout] += 1

    return cols, col_idx

def simulate_dance_fast(cols, col_idx, counter=None):
    """
    Performs exactly ONE round of dancing.
    Optimized to avoid path building & expensive list operations.
    """

    right_col_idx = (col_idx + 1) % len(cols)

    clapper = cols[col_idx].pop(0)

    col = cols[right_col_idx]
    n = len(col)

    cycle = 2 * n
    step = (clapper - 1) % cycle

    if step < n:
        insert_idx = step
    else:
        right_pos = (cycle - 1) - step
        insert_idx = right_pos + 1

    col.insert(insert_idx, clapper)

    shout = end_number(cols)
    if counter is not None:
        counter[shout] += 1

    return (col_idx + 1) % len(cols)

def part_1():
    rows = [[int(p) for p in line.split(" ")] for line in lines]
    cols = transpose_grid(rows)
    
    cols, _ = simulate_dance(cols, 0, 10)

    print(end_number(cols))

def part_2():
    counter = Counter()
    rounds = 0
    rows = [[int(p) for p in line.split(" ")] for line in lines]
    cols = transpose_grid(rows)
    
    col_idx = 0

    target_shout = None
    target_shout_count = 0

    while target_shout_count < 2024:
        rounds += 1
        col_idx = simulate_dance_fast(cols, col_idx, counter)

        shout = end_number(cols)
        c = counter[shout]

        if c > target_shout_count:
            target_shout = shout
            target_shout_count = c

    print("Round", rounds, "-", target_shout, "Count:", target_shout_count)
    print("Final Answer:", target_shout * rounds)
    
def part_3():
    rows = [[int(p) for p in line.split(" ")] for line in lines]
    cols = transpose_grid(rows)
    max_shout = 0
    round = 0
    col_idx = 0
    seen = {}

    while True:
        shout = end_number(cols)
        max_shout = max(max_shout, shout)

        config = tuple(tuple(col) for col in cols)
        if config in seen:
            break

        seen[config] = round

        col_idx = simulate_dance_fast(cols, col_idx)
        round += 1

    print(max_shout)

if __name__ == "__main__":
    part_3()