from itertools import batched
import re


def parse(text):
    re_digits = re.compile(r"-?\d+")

    def parse_line(line):
        return tuple(map(tuple, batched(map(int, re_digits.findall(line)), 3)))

    lines = text.splitlines()
    return [(i, parse_line(line)) for i, line in enumerate(lines)]


def id(particle):
    return particle[0]


def accln(particle):
    return particle[1][2]


def magn(v):
    x, y, z = v
    return abs(x) + abs(y) + abs(z)


def part1(particles, args, p1_state):
    particles.sort(key=lambda p: magn(accln(p)))
    return id(particles[0])


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
