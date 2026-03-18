from itertools import islice
from math import isqrt


def parse(text):
    return int(text)


def walk():
    n = 1
    x, y = (0, 0)
    length = 0
    yield (x, y), n
    while True:
        length += 1
        # go right
        for _ in range(length):
            n += 1
            x += 1
            yield (x, y), n
        # go up
        for _ in range(length):
            n += 1
            y -= 1
            yield (x, y), n

        length += 1
        # go left
        for _ in range(length):
            n += 1
            x -= 1
            yield (x, y), n
        # go down
        for _ in range(length):
            n += 1
            y += 1
            yield (x, y), n


def part1(data, args, p1_state):
    (x, y), _ = next(islice(walk(), data - 1, None))
    return abs(x) + abs(y)


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
