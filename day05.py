#  2017 Day 5
#  ==========
#
#  Part 1: 318883
#  Part 2: 23948711
#
#  Timings
#  --------------------------------------
#      Parse:     0.000083s  (83.00 µs)
#     Part 1:     0.022635s  (22.64 ms)
#     Part 2:     1.345750s  (1.346 s)
#    Elapsed:     1.368566s  (1.369 s)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    return [int(line) for line in text.splitlines()]


def jump(offsets, stranger):
    idx = 0
    count = 0
    while 0 <= idx < len(offsets):
        count += 1
        offset = offsets[idx]
        offsets[idx] += -1 if stranger and offset >= 3 else 1
        idx += offset
    return count


def part1(offsets, args, p1_state):
    return jump(offsets.copy(), False)


def part2(offsets, args, p1_state):
    return jump(offsets, True)


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
