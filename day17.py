def parse(text):
    return int(text)


def part1(data, args, p1_state):
    buffer = [0]
    pstn = 0
    for n in range(1, 2017 + 1):
        pstn = (pstn + data + 1) % len(buffer)
        buffer.insert(pstn, n)

    return buffer[pstn + 1]


def part2(data, args, p1_state):
    buffer = [0]
    pstn = 0
    for n in range(1, 50_000_000 + 1):
        print(f"{n:,}")
        pstn = (pstn + data + 1) % len(buffer)
        buffer.insert(pstn, n)
    print()
    print(buffer[0])
    print(buffer[-1])
    print(buffer[(buffer.index(0) + 1) % len(buffer)])


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
