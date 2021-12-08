

def read_file_lines(filepath):
    lines = []
    with open(filepath) as f:
        return [line.strip() for line in f]


