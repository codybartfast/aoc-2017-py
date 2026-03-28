from collections import deque

def parse(text):
    return deque(tuple(map(int, line.split("/"))) for line in text.splitlines())


def bridges(mags, bridge, type, strength):

    for _ in range(len(mags)):
        mag = mags.popleft()
        if type in mag:
            bridge.append(mag)
            strength += mag[0] + mag[1]
            yield bridge, strength
            next_type = mag[1 - mag.index(type)]
            yield from bridges(mags, bridge, next_type, strength)
            bridge.pop()
            strength -= mag[0] + mag[1]
        mags.append(mag)
    


def part1(mags, args, p1_state):
    return max(str for bridge, str in bridges(mags, [], 0, 0))


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
