import re


def parse(text):
    re_digits = re.compile(r"-?\d+")

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

    parts = text.split(",")
    return [parse_part(part) for part in parts]


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
    return progs


def part1(moves, args, p1_state):
    progs = list("abcdefghijklmnop" if len(moves) != 3 else "abcde")
    return "".join(dance(progs, moves))


def part2(data, args, p1_state):
    return "ans2"


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
