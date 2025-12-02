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
            lines.append(line)
        return lines