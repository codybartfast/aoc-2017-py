#  2017 Day 12
#  ===========
#
#  Part 1: 134
#  Part 2: 193
#
#  Timings
#  --------------------------------------
#      Parse:     0.000767s  (766.8 µs)
#     Part 1:     0.000028s  (28.42 µs)
#     Part 2:     0.000484s  (484.0 µs)
#    Elapsed:     0.001328s  (1.328 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    def parse_line(line):
        prog, neighbours_text = line.split(" <-> ")
        return prog, neighbours_text.split(", ")

    return dict(
        (
            (prog, others.split(", "))
            for prog, others in (line.split(" <-> ") for line in text.splitlines())
        )
    )


def find_group(prog, links):
    known = set([prog])
    found = [prog]
    while found:
        new_found = []
        for prog in found:
            for other in links[prog]:
                if other not in known:
                    new_found.append(other)
                known.add(other)
        found = new_found
    return known


def find_groups(links):
    unseen = set(links.keys())
    groups = []
    while unseen:
        n = unseen.pop()
        group = find_group(n, links)
        groups.append(group)
        unseen.difference_update(group)
    return groups


def part1(links, args, p1_state):
    return len(find_group("0", links))


def part2(links, args, p1_state):
    return len(find_groups(links))


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
