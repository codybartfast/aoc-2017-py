
def parse(text):
    def parse_line(line):
        parts = line.split(": ")
        return int(parts[0]), int(parts[1])

    return dict(parse_line(line) for line in text.splitlines())

def is_caught(wall, depth, time):
    return depth in wall and time % (2 * (wall[depth] - 1)) == 0 


def part1(wall, args, p1_state):
    size = max(wall.keys()) + 1
    serverity = 0
    for depth in range(size):
        if is_caught(wall, depth, depth):
            serverity += depth * wall[depth]
    return serverity


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
