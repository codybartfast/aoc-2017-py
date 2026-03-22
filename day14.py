from array import array


def parse(text):
    return text


def knot2(lengths):
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


def hex_to_bin(hex):
    assert not len(hex) % 2
    bstr = ""
    for c in hex:
        bstr += format(int(c, 16), "04b")
    return bstr


def read_disk(key):
    disk = []
    for n in range(128):
        lengths = f"{key}-{n}".encode()
        disk.append(hex_to_bin(knot2(lengths)))
    return disk

def clear_region(disk, len, i):
    j = -1
    disk[i] = "0"
    for j in [i - len, i - 1, i + 1, i + len]:
        if disk[j] == "1":
            clear_region(disk, len, j)

def part1(key, args, p1_state):
    disk = read_disk(key)
    p1_state.value = disk
    return sum(1 for track in disk for b in track if b == "1")


def part2(_, __, p1_state):
    len = 128 + 2
    disk_strs = p1_state.value
    disk = ["0"] * len
    for track_str in disk_strs:
        disk.append("0")
        disk.extend(list(track_str))
        disk.append("0")
    disk.extend(["0"] * len)

    regions = 0
    for i, b in enumerate(disk):
        if b == "1":
            regions += 1
            clear_region(disk, len, i)
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
