#  2017 Day 4
#  ==========
#
#  Part 1: 325
#  Part 2: 119
#
#  Timings
#  --------------------------------------
#      Parse:     0.000130s  (129.6 µs)
#     Part 1:     0.000169s  (168.6 µs)
#     Part 2:     0.000917s  (917.0 µs)
#    Elapsed:     0.001256s  (1.256 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    return [line.split() for line in text.splitlines()]


def part1(pass_phrases, args, p1_state):
    return sum(1 for phrase in pass_phrases if len(phrase) == len(set(phrase)))


def part2(pass_phrases, args, p1_state):
    normalised = (list(map(tuple, map(sorted, phrase))) for phrase in pass_phrases)
    return sum(1 for norm in normalised if len(norm) == len(set(norm)))


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
