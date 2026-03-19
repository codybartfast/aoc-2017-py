def parse(text):
    return text


def score_groups(stream):
    group_score = 0
    in_garbage = False
    ignore = False
    open_groups = 0
    for i in range(len(stream)):
        if ignore:
            ignore = False
            continue
        match stream[i]:
            case "!":
                ignore = True
            case "<":
                in_garbage = True
            case ">":
                in_garbage = False
            case "{":
                if not in_garbage:
                    open_groups += 1
            case "}":
                if not in_garbage:
                    group_score += open_groups
                    open_groups -= 1
    return group_score


def part1(stream, args, p1_state):
    print(f"\n{stream}\n")
    return score_groups(stream)


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
