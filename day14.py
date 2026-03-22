#  2017 Day 14
#  ===========
#
#  Part 1: 8204
#  Part 2: 1089
#
#  Timings
#  --------------------------------------
#      Parse:     0.000000s  (0.250 µs)
#     Part 1:     0.268840s  (268.8 ms)
#     Part 2:     0.001269s  (1.269 ms)
#    Elapsed:     0.270161s  (270.2 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    return text


def knot_hash(lengths):
    lengths = list(lengths) + [17, 31, 73, 47, 23]
    data = list(range(256))
    pstn = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            data = data[pstn:] + data[:pstn]
            data = list(reversed(data[:length])) + data[length:]
            data = data[-pstn:] + data[:-pstn]
            pstn = (pstn + length + skip) % len(data)
            skip += 1
    dense = []
    for start in range(0, 256, 16):
        n = 0
        for i in range(start, start + 16):
            n ^= data[i]
        dense.append(format(n, "02x"))
    return "".join(dense)


def generate_disk(key):
    disk = []
    for n in range(128):
        lengths = f"{key}-{n}".encode()
        hex = knot_hash(lengths)
        bin_str = "".join(format(int(c, 16), "04b") for c in hex)
        disk.append(bin_str)
    return disk


def disk_ng(disk_str):
    width = len(disk_str[0]) + 2
    disk_ng = ["0"] * width
    for track_str in disk_str:
        disk_ng.append("0")
        disk_ng.extend(list(track_str))
        disk_ng.append("0")
    disk_ng.extend(["0"] * width)
    return disk_ng


def clear_region(disk, len, i):
    disk[i] = "0"
    for j in [i - len, i - 1, i + 1, i + len]:
        if disk[j] == "1":
            clear_region(disk, len, j)


def part1(key, args, p1_state):
    disk = generate_disk(key)
    p1_state.value = disk
    return sum(1 for track in disk for b in track if b == "1")


def part2(_, __, p1_state):
    width = 128 + 2
    disk = disk_ng(p1_state.value)
    regions = 0
    for i, b in enumerate(disk):
        if b == "1":
            regions += 1
            clear_region(disk, width, i)
    return regions


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
