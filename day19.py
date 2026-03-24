#  2017 Day 19
#  ===========
#
#  Part 1: RYLONKEWB
#  Part 2: 16016
#
#  Timings
#  --------------------------------------
#      Parse:     0.000033s  (32.79 µs)
#     Part 1:     0.000554s  (554.3 µs)
#     Part 2:     0.000000s  (0.250 µs)
#    Elapsed:     0.000620s  (619.6 µs)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    return text.splitlines()


def follow(diag, pstn):
    x, y, line, dx, dy = pstn
    count = 1
    trace = []

    while True:
        x, y = x + dx, y + dy
        c = diag[y][x]
        if c == " ":
            return trace, count
        count += 1
        if c == line:
            continue
        elif c == "+":
            if line == "|":
                line = "-"
                left = diag[y][x - 1]
                dx, dy = (-1, -0) if left == "-" or left.isalpha() else (1, 0)
            else:
                line = "|"
                up = diag[y - 1][x]
                dx, dy = (0, -1) if up == "|" or up.isalpha() else (0, 1)
        elif c.isalpha():
            trace.append(c)


def part1(diag, args, p1_state):
    pstn = (diag[0].index("|"), 0, "|", 0, 1)
    trace, count = follow(diag, pstn)
    p1_state.value = count
    return "".join(trace)


def part2(data, args, p1_state):
    return p1_state.value


# Runner
################################################################################


def jingle(text=None, filepath=None, extra_args=None):
    if not text and filepath:
        with open(filepath, "r") as f:
            text = f.read()
    sack.present(text, extra_args, parse, part1, part2)


if __name__ == "__main__":
    import sys
    import sack

    file = sys.argv[1] if len(sys.argv) > 1 else None
    filepath = sack.get_filepath(file)
    if filepath:
        extra_args = sys.argv[2:]
        jingle(filepath=filepath, extra_args=extra_args)
