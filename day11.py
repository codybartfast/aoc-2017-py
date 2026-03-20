def parse(text):
    return text.split(",")


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
