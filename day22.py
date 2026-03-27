DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse(text):
    lines = text.splitlines()
    dim = len(lines)
    mid = dim // 2
    nodes = {}
    for y in range(dim):
        for x in range(dim):
            if lines[y][x] == "#":
                nodes[x, y] = True

    return (mid, mid), nodes


def spread(pstn, nodes, bursts):
    dir = 0
    infections = 0

    for _ in range(bursts):
        infected = nodes.get(pstn, False)
        dir = (dir + (1 if infected else -1)) % 4
        delta = DIRS[dir]
        if infected:
            nodes[pstn] = False
        else:
            nodes[pstn] = True
            infections += 1
        pstn = pstn[0] + delta[0], pstn[1] + delta[1]

    return infections


def part1(data, args, p1_state):
    pstn, nodes = data
    return spread(pstn, nodes, 10_000)


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
