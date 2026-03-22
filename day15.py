#  2017 Day 15
#  ===========
#
#  Part 1: 631
#  Part 2: 279
#
#  Timings
#  --------------------------------------
#      Parse:     0.000035s  (35.25 µs)
#     Part 1:     9.069774s  (9.070 s)
#     Part 2:     4.643134s  (4.643 s)
#    Elapsed:    13.713082s  (13.71 s)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


import re

def parse(text):
    re_digits = re.compile(r"-?\d+")

    def parse_line(line):
        parts = line.split()
        return int(parts[-1])
    
    lines = text.splitlines()
    return [parse_line(line) for line in lines]


def generator(factor, prev, filter):
    while True:
        prev *= factor
        prev %= 2147483647
        if prev & filter == 0:
            yield prev


def part1(data, args, p1_state):
    [prev_a, prev_b] = data

    gen_a = iter(generator(16807, prev_a, 0b0))
    gen_b = iter(generator(48271, prev_b, 0b0))

    mask = (2 ** 16) - 1
    return sum(next(gen_a) & mask == next(gen_b) & mask for _ in range(40_000_000))


def part2(data, args, p1_state):
    [prev_a, prev_b] = data

    gen_a = iter(generator(16807, prev_a, 0b11))
    gen_b = iter(generator(48271, prev_b, 0b111))

    mask = (2 ** 16) - 1
    return sum(next(gen_a) & mask == next(gen_b) & mask for _ in range(5_000_000))


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
