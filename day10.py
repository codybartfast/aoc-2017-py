#  2017 Day 10
#  ===========
#
#  Part 1: 62238
#  Part 2: 2b0c9cc0449507a0db3babd57ad9e8d8
#
#  Timings
#  --------------------------------------
#      Parse:     0.000003s  (3.333 µs)
#     Part 1:     0.000069s  (69.08 µs)
#     Part 2:     0.009871s  (9.871 ms)
#    Elapsed:     0.009987s  (9.987 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3

def parse(text):
    return text, tuple(map(int, text.split(",")))


def knot(data, lengths, rounds):
    pstn = 0
    skip = 0
    for _ in range(rounds):
        for length in lengths:
            data = data[pstn:] + data[:pstn]
            data = list(reversed(data[:length])) + data[length:]
            data = data[-pstn:] + data[:-pstn]
            pstn = (pstn + length + skip) % len(data)
            skip += 1
    return data


def dense_hash(hash):
    dense = []
    for start in range(0, 256, 16):
        n = 0
        for i in range(start, start + 16):
            n ^= hash[i]
        dense.append(format(n, "02x"))
    return "".join(dense)


def part1(data, args, p1_state):
    _, lengths = data
    size = 5 if len(lengths) == 4 else 256
    knotted = knot(list(range(size)), lengths, 1)
    return knotted[0] * knotted[1]


def part2(data, args, p1_state):
    text, _ = data
    lengths = list(text.encode()) + [17, 31, 73, 47, 23]
    knotted = knot(list(range(256)), lengths, 64)
    return dense_hash(knotted)




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
