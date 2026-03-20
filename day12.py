import re

def parse(text):
    re_digits = re.compile(r"-?\d+")

    def parse_line(line):
        ds = list(map(int, re_digits.findall(line))) # need int?
        return ds[0], ds[1:]
        
    lines = text.splitlines()
    return dict(parse_line(line) for line in lines)


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
    return list(known)


def part1(links, args, p1_state):
    return len(find_group(0, links))


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
