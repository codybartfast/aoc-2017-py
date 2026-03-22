#  2017 Day 16
#  ===========
#
#  Part 1: namdgkbhifpceloj
#  Part 2: ibmchklnofjpdeag
#
#  Timings
#  --------------------------------------
#      Parse:     0.001439s  (1.439 ms)
#     Part 1:     0.001089s  (1.089 ms)
#     Part 2:     0.060846s  (60.85 ms)
#    Elapsed:     0.063410s  (63.41 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):

    def parse_part(part):
        match part[0]:
            case "s":
                return ("s", int(part[1:]))
            case "x":
                [a, b] = part[1:].split("/")
                return ("x", int(a), int(b))
            case "p":
                [a, b] = part[1:].split("/")
                return ("p", a, b)
            case _:
                assert False, part

    return [parse_part(part) for part in text.split(",")]


def dance(progs, moves):
    for move in moves:
        match move:
            case ("s", n):
                assert n, n
                progs = progs[-n:] + progs[:-n]
            case ("x", a, b):
                t = progs[a]
                progs[a] = progs[b]
                progs[b] = t
            case ("p", a, b):
                i = progs.index(a)
                progs[progs.index(b)] = a
                progs[i] = b
            case _:
                assert False, move

    return progs, "".join(progs)


def part1(moves, args, p1_state):
    progs = list("abcdefghijklmnop" if len(moves) != 3 else "abcde")
    return dance(progs, moves)[1]


def part2(moves, args, p1_state):
    key = "abcdefghijklmnop"
    progs = list(key)
    seen = []

    while key not in seen:
        seen.append(key)
        progs, key = dance(progs, moves)

    return seen[(1_000_000_000 - len(seen)) % len(seen)]


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
