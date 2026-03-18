#  2017 Day 2
#  ==========
#
#  Part 1: 54426
#  Part 2: 333
#
#  Timings
#  --------------------------------------
#      Parse:     0.000032s  (32.38 µs)
#     Part 1:     0.000003s  (2.542 µs)
#     Part 2:     0.000020s  (19.83 µs)
#    Elapsed:     0.000094s  (93.63 µs)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text): # also sorts row
    def parse_line(line):
        return sorted([int(part) for part in line.split()])

    return [parse_line(line) for line in text.splitlines()]


def part1(sheet, args, p1_state):
    return sum(row[-1] - row[0] for row in sheet)


def checksum2(row):
    for i, d in enumerate(row):
        for j in range(i + 1, len(row)):
            if row[j] % d == 0:
                return row[j] // d


def part2(sheet, args, p1_state):
    return sum(checksum2(row) for row in sheet)


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
