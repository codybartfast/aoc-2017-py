def parse(text):
    def parse_line(line):
        parts = line.split()
        return [int(part) for part in parts]

    lines = text.splitlines()
    return [parse_line(line) for line in lines]


def part1(sheet, args, p1_state):
    return sum(max(row) - min(row) for row in sheet)


def part2(sheet, args, p1_state):
    return "ans2"


# Runner
################################################################################


def jingle(text=None, filepath=None, extra_args=None):
    if not text and filepath:
        with open(filepath, "r") as f:
            text = f.read().strip()
    sack.present(text, extra_args, parse, part1, part2)


if __name__ == "__main__":
    import sys
    import sack

    file = sys.argv[1] if len(sys.argv) > 1 else None
    filepath = sack.get_filepath(file)
    if filepath:
        extra_args = sys.argv[2:]
        jingle(filepath=filepath, extra_args=extra_args)
