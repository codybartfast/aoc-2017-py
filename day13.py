#  2017 Day 13
#  ===========
#
#  Part 1: 1624
#  Part 2: 3923436
#
#  Timings
#  --------------------------------------
#      Parse:     0.000018s  (17.58 µs)
#     Part 1:     0.000003s  (3.500 µs)
#     Part 2:     0.719350s  (719.4 ms)
#    Elapsed:     0.719418s  (719.4 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


# Suppose could us a sieve of Eratosthenes like approach 🤔

def parse(text): # and convert range to period
    def parse_line(line):
        parts = line.split(": ")
        return int(parts[0]), (int(parts[1]) - 1) * 2

    return [parse_line(line) for line in text.splitlines()]


def part1(wall, args, p1_state):
    serverity = 0
    for depth, period in wall:
        if depth % period == 0:
            serverity += depth * (period // 2 + 1)
    return serverity


def part2(wall, args, p1_state):
    time = -1
    while True:
        time += 1
        if not any((time + depth) % period == 0 for depth, period in wall):
            return time


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
