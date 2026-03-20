#  2017 Day 13
#  ===========
#
#  Part 1: 1624
#  Part 2: 3923436
#
#  Timings
#  --------------------------------------
#      Parse:     0.000013s  (13.04 µs)
#     Part 1:     0.000005s  (5.250 µs)
#     Part 2:     1.073112s  (1.073 s)
#    Elapsed:     1.073192s  (1.073 s)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    def parse_line(line):
        parts = line.split(": ")
        return int(parts[0]), int(parts[1])

    return [parse_line(line) for line in text.splitlines()]

def is_caught(depth, range, time):
    return time % (2 * (range - 1)) == 0 


def any_caught(wall, time):
    return any(is_caught(depth, range, time + depth) for depth, range in wall)
    

def part1(wall, args, p1_state):
    serverity = 0
    for depth, range in wall:
        if is_caught(depth, range, depth):
            serverity += depth * range
    return serverity


def part2(wall, args, p1_state):
    time = -1
    while True:
        time += 1
        if not any_caught(wall, time):
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
