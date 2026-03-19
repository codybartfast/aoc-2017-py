#  2017 Day 10
#  ===========
#
#  Part 1: 62238
#  Part 2: 2b0c9cc0449507a0db3babd57ad9e8d8
#
#  Timings
#  --------------------------------------
#      Parse:     0.000003s  (3.167 µs)
#     Part 1:     0.000027s  (26.58 µs)
#     Part 2:     0.001231s  (1.231 ms)
#    Elapsed:     0.001296s  (1.296 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


from array import array


def parse(text):
    return text, tuple(map(int, text.split(",")))


def knot(lengths, rounds):
    # data always begins at the current position.  pstn tracks the nominal
    # current position. At end pstn is used to shift data so it starts at '0'
    # rather than current position.
    data = array("B", range(256))
    skip = 0
    for _ in range(rounds):
        for length in lengths:
            data[:length] = data[:length][::-1]
            shift = (length + skip) % 256
            data = data[shift:] + data[:shift]
            skip = (skip + 1) % 256
    pstn = (sum(lengths) * rounds + skip * (skip - 1) // 2) % 256
    return data[-pstn:] + data[:-pstn]


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
    knotted = knot(lengths, 1)
    return knotted[0] * knotted[1]


def part2(data, args, p1_state):
    text, _ = data
    lengths = list(text.encode()) + [17, 31, 73, 47, 23]
    knotted = knot(lengths, 64)
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
