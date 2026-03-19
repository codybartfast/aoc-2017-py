#  2017 Day 9
#  ==========
#
#  Part 1: 17390
#  Part 2: 7825
#
#  Timings
#  --------------------------------------
#      Parse:     0.000000s  (0.333 µs)
#     Part 1:     0.000587s  (586.7 µs)
#     Part 2:     0.000000s  (0.292 µs)
#    Elapsed:     0.000634s  (633.9 µs)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    return text


def examine(stream):
    group_score = 0
    garbage_count = 0
    ignore = False
    in_garbage = False
    open_groups = 0
    for char in stream:
        if ignore:
            ignore = False
            continue

        if char == "!":
            ignore = True
            continue

        if in_garbage:
            if char == ">":
                in_garbage = False
            else:
                garbage_count += 1
            continue

        match char:
            case "<":
                in_garbage = True
            case "{":
                open_groups += 1
            case "}":
                group_score += open_groups
                open_groups -= 1

    return group_score, garbage_count


def part1(stream, args, p1_state):
    n_groups, n_garbage = examine(stream)
    p1_state.value = n_garbage
    return n_groups


def part2(_, __, p1_state):
    return p1_state.value


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
