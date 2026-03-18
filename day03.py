from itertools import islice


def parse(text):
    return int(text)


def walk():
    x, y = (0, 0)
    length = 0
    yield (x, y)
    while True:
        length += 1
        # go right
        for _ in range(length):
            x += 1
            yield (x, y)
        # go up
        for _ in range(length):
            y -= 1
            yield (x, y)

        length += 1
        # go left
        for _ in range(length):
            x -= 1
            yield (x, y)
        # go down
        for _ in range(length):
            y += 1
            yield (x, y)


def stress_test(target, walk_it):
    values = {(0, 0): 1}
    next(walk_it)
    while True:
        x, y = next(walk_it)
        value = sum(
            values.get((x + dx, y + dy), 0)
            for dx, dy in [
                (-1, -1),
                (0, -1),
                (1, -1),
                (-1, 0),
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
            ]
        )
        if value > target:
            return value
        else:
            values[(x, y)] = value


def part1(data, args, p1_state):
    x, y = next(islice(walk(), data - 1, None))
    return abs(x) + abs(y)


def part2(data, args, p1_state):
    return stress_test(data, iter(walk()))


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
