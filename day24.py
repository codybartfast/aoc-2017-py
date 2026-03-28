#  2017 Day 24
#  ===========
#
#  Part 1: 1868
#  Part 2: 1841
#
#  Timings
#  --------------------------------------
#      Parse:     0.000017s  (16.58 µs)
#     Part 1:     0.787808s  (787.8 ms)
#     Part 2:     0.000001s  (0.584 µs)
#    Elapsed:     0.787868s  (787.9 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


# This struck me as a fairly straightfoward depth first search.  Recently I've
# usually copied the data to pass to sub calls to ensure correctness.  The main
# thing I wanted to do here was use the one data structure and replace items
# back into to it after sub calls, deque seemed to make this quite neat, and
# deque is something I've been meaning to use more often.  Not sure it was the
# best choice.  Older commits are probably prettier before a lot of minor perf
# tweaks.


from collections import deque


def parse(text):
    def parse_line(line):
        parts = line.split("/")
        type1 = int(parts[0])
        type2 = int(parts[1])
        return (type1, type2), type1 + type2

    return deque(parse_line(line) for line in text.splitlines())


def bridges(components, type, strength, length, results):

    did_extend = False

    for _ in range(len(components)):
        comp = components.popleft()
        (type1, type2), comp_str = comp
        if type == type1:
            did_extend = True
            next_type = type2
            bridges(components, next_type, strength + comp_str, length + 1, results)
        elif type == type2:
            did_extend = True
            next_type = type1
            bridges(components, next_type, strength + comp_str, length + 1, results)
        components.append(comp)

    # 0 = MAX_STRENGTH, 1 = MAX_LENGTH, 2 = MAX_LENGTH_MAX_STRENGTH
    if not did_extend:
        if strength > results[0]:
            results[0] = strength
        if length >= results[1]:
            if length > results[1]:
                results[1] = length
                results[2] = strength
            elif strength > results[2]:
                results[2] = strength


def part1(mags, args, p1_state):

    results = [-1, -1, -1]
    bridges(mags, 0, 0, 0, results)

    p1_state.value = results[2]
    return results[0]


def part2(mags, args, p1_state):
    return p1_state.value


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
