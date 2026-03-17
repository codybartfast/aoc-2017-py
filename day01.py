def parse(text):
    return text


def part1(data, args, p1_state):
    return sum(int(c1) for c1, c2 in zip(data, data[1:] + data[0]) if c1 == c2)


def part2(data, args, p1_state):
    half = len(data) // 2
    return sum(int(c1) for c1, c2 in zip(data, data[half:] + data[:half]) if c1 == c2)


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
