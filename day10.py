def parse(text):
    return tuple(map(int, text.split(",")))


def knot(data, lengths):
    pstn = 0
    skip = 0
    for length in lengths:
        data = data[pstn:] + data[:pstn]
        data = list(reversed(data[:length])) + data[length:]
        data = data[-pstn:] + data[:-pstn]
        
        pstn = (pstn + length + skip) % len(data)
        skip += 1
        # print(length, data, pstn)
        
    return data


def part1(lengths, args, p1_state):
    print(f"\n{lengths}\n")
    size = 5 if len(lengths) == 4 else 256
    knotted = knot(list(range(size)), lengths)
    return knotted[0] * knotted[1]


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
