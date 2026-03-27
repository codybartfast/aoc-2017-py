#  2017 Day 22
#  ===========
#
#  Part 1: 5538
#  Part 2: 2511090
#
#  Timings
#  --------------------------------------
#      Parse:     0.000037s  (37.12 µs)
#     Part 1:     0.001144s  (1.144 ms)
#     Part 2:     0.796101s  (796.1 ms)
#    Elapsed:     0.797334s  (797.3 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


#  Using an array for Part 2 reduced overall time from around 1,200ms to 800ms


from array import array


DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
MAX = 225


def parse(text):
    lines = text.splitlines()
    dim = len(lines)
    mid = dim // 2
    offset = MAX - mid
    nodes = {}
    for y in range(dim):
        for x in range(dim):
            if lines[y][x] == "#":
                nodes[offset + x, offset + y] = 2

    return (MAX, MAX), nodes


def spread(curr, nodes, bursts):
    dir = 0
    infections = 0

    for _ in range(bursts):
        infected = nodes.get(curr, False)
        dir = (dir + (1 if infected else -1)) % 4
        delta = DIRS[dir]
        if infected:
            nodes[curr] = False
        else:
            nodes[curr] = True
            infections += 1
        curr = curr[0] + delta[0], curr[1] + delta[1]

    return infections


def evolved(curr, nodes, bursts):
    width = 2 * MAX + 1
    cluster = array("B", [0] * width * width)
    for x, y in nodes.keys():
        cluster[y * width + x] = 2
    idx = curr[1] * width + curr[0]
    dirs = [-width, 1, width, -1]

    dir = 0
    infections = 0
    for _ in range(bursts):
        cluster[idx] = ((state := cluster[idx]) + 1) % 4
        if state == 1:
            infections += 1
        idx += dirs[dir := (dir + 3 + state) % 4]

    return infections


def part1(status, args, p1_state):
    curr, nodes = status
    return spread(curr, dict(nodes), 10_000)


def part2(status, args, p1_state):
    curr, nodes = status
    return evolved(curr, nodes, 10_000_000)


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
