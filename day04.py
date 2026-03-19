def parse(text):
    def parse_line(line):
        parts = line.split()
        return [part for part in parts]

    lines = text.splitlines()
    return [parse_line(line) for line in lines]


def part1(pass_phrases, args, p1_state):
    print(f"\n{pass_phrases}\n")
    return sum(
        1 for phrase in pass_phrases if len(phrase) == len(set(phrase))
    )


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
