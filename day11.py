#  2017 Day 11
#  ===========
#
#  Part 1: 682
#  Part 2: 1406
#
#  Timings
#  --------------------------------------
#      Parse:     0.000148s  (147.6 µs)
#     Part 1:     0.000614s  (613.5 µs)
#     Part 2:     0.000000s  (0.292 µs)
#    Elapsed:     0.000799s  (798.7 µs)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3



def parse(text):
    return text.split(",")


# If you rotate the hex-grid 45° clockwise then I think it can be treated like
# a conventional Manhattan grid but with diagnal movement allowed up and to the
# left / but not up and and to the right \. But unlike most AoC grids North is
# is +y because it makes the allowed diagnal more intuitive (at least to me). 

DELTAS = {
    "nw": (0, 1),
    "n": (1, 1),
    "ne": (1, 0),
    "se": (0, -1),
    "s": (-1, -1),
    "sw": (-1, 0),
}


def walk(pstn, dirs):
    x, y = pstn
    max_dist = -1
    for dir in dirs:
        dx, dy = DELTAS[dir]
        x += dx
        y += dy
        dist = max(abs(x), abs(y)) if x * y > 0 else abs(x) + abs(y)
        if dist > max_dist:
            max_dist = dist
    return dist, max_dist


def part1(dirs, args, p1_state):
    dist, max_dist =walk((0, 0), dirs)
    p1_state.value = max_dist
    return dist


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
