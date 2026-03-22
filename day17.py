#  2017 Day 17 - linked
#  ===========
#
#  Part 1: 1025
#  Part 2: 37803463
#
#  Timings
#  --------------------------------------
#      Parse:     0.000001s  (0.875 µs)
#     Part 1:     0.007267s  (7.267 ms)
#     Part 2:   219.773509s  (3m 39.8s)
#    Elapsed:   219.780856s  (3m 39.8s)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


#  2017 Day 17
#  ===========
#
#  Part 1: 1025
#  Part 2: 37803463
#
#  Timings
#  --------------------------------------
#      Parse:     0.000001s  (0.959 µs)
#     Part 1:     0.000439s  (439.2 µs)
#     Part 2:     8.403502s  (8.404 s)
#    Elapsed:     8.404022s  (8.404 s)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


from array import array


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def parse(text):
    return int(text)


def spin(size, steps):
    max_buff = 2**11

    buffers = [array('I', [0])]
    b, i = 0, 0
    for n in range(1, size + 1):
        remaining = steps + 1
        while remaining:
            space = len(buffers[b]) - i
            if remaining <= space:
                i += remaining
                remaining = 0
            else:
                remaining -= space
                b = (b + 1) % len(buffers)
                i = 0
        buffers[b].insert(i, n)
        
        if len(buffers[b]) > max_buff:
            buff0 = buffers.pop(b)
            size = len(buff0) // 2
            buff1, buff2 = buff0[:size], buff0[size:]
            buffers.insert(b, buff2)
            buffers.insert(b, buff1)

    return (b, i), buffers


def next(pstn, buffers):
    b, i = pstn
    i += 1
    return buffers[b][i] if i < len(buffers[b]) else buffers[(b + 1) % len(buffers)][0]


def part1(data, args, p1_state):
    pstn, buffers = spin(2017, data)
    return next(pstn, buffers)


def part2(data, args, p1_state):
    (b, i), buffers = spin(50_000_000, data)
    for b, buff in enumerate(buffers):
        if 0 in buff:
            return next((b, buff.index(0)), buffers)


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
