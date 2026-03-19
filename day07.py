#  2017 Day 7
#  ==========
#
#  Part 1: hmvwl
#  Part 2: 1853
#
#  Timings
#  --------------------------------------
#      Parse:     0.000968s  (967.8 µs)
#     Part 1:     0.000156s  (155.7 µs)
#     Part 2:     0.000369s  (369.5 µs)
#    Elapsed:     0.001541s  (1.541 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    def parse_line(line):
        left, *rest = line.split(" -> ")
        name, num_str = left.split()
        weight = int(num_str[1:-1])
        sub_towers = rest[0].split(", ") if rest else []
        return name, (weight, sub_towers)

    return dict(parse_line(line) for line in text.splitlines())


def find_base(progs):
    names = set()
    referenced = set()
    for name, (_, subs) in progs.items():
        names.add(name)
        referenced.update(subs)
    return names.difference(referenced).pop()


def calc_load(name, progs, loads):
    weight, subs = progs[name]
    if name in loads:
        return loads[name]

    weight += sum(calc_load(sub, progs, loads) for sub in subs)
    loads[name] = weight
    return weight


def find_diff(base, progs, loads):
    _, subs = progs[base]
    lds = [loads[sub] for sub in subs]
    n = lds.pop()
    if n not in lds:
        exp, odd = lds.pop(), n
    else:
        exp = n
        odd = next(ld for ld in lds if ld != exp)
    return odd - exp


def find_wrong_weight(name, progs, loads):
    weight, subs = progs[name]
    lds = [loads[sub] for sub in subs]
    if len(set(lds)) == 1:
        return weight
    odd_weight = max(lds)
    odd_name = subs[lds.index(odd_weight)]
    return find_wrong_weight(odd_name, progs, loads)


def part1(data, args, p1_state):
    base = find_base(data)
    p1_state.value = base
    return base


def part2(progs, args, p1_state):
    base = p1_state.value
    loads = {}
    calc_load(base, progs, loads)
    diff = find_diff(base, progs, loads)
    # No reason can't be negative, but why handle case if Eric's being kind
    assert diff > 0
    return find_wrong_weight(base, progs, loads) - diff


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
