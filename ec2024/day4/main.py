from util.main import parse_file_to_lines

test_file = "ec2024/day4/test.txt"
input_file = "ec2024/day4/input.txt"
lines = parse_file_to_lines(input_file)

def part_1():
    nails = [int(line) for line in lines]
    shortest = min(nails)
    result = sum([nail - shortest for nail in nails])
    print(result)

def part_2():
    nails = [int(line) for line in lines]
    shortest = min(nails)
    result = sum([nail - shortest for nail in nails])
    print(result)

def part_3():
    nails = list(sorted([int(line) for line in lines]))
    median = nails[len(nails) // 2]
    hits = [abs(nail - median) for nail in nails]
    result = sum(hits)
    print(result)

if __name__ == "__main__":
    part_3()