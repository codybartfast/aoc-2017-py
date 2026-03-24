import re


def parse(text):
    return text.splitlines()


def follow(diag, pstn):
    x, y, line, dx, dy = pstn
    trace = []

    while True:
        nx, ny = x + dx, y + dy
        c = diag[ny][nx]
        if c == " ":
            return trace
        if c.isalpha():
            trace.append(c)
        if c == line:
            x, y = nx, ny
        elif c == "+":
            if line == "|":
                line = "-"
                left = diag[ny][nx - 1]
                dx, dy = (-1, -0) if left == "-" or left.isalpha() else (1, 0)
            else:
                assert line == "-"
                line = "|"
                up = diag[ny - 1][nx]
                dx, dy = (0, -1) if up == "|" or up.isalpha() else (0, 1)
        x, y = nx, ny


def part1(diag, args, p1_state):
    print(f"\n{'\n'.join(diag)}\n")
    pstn = (diag[0].index("|"), 0, "|", 0, 1)
    return "".join(follow(diag, pstn))


def part2(data, args, p1_state):
    return "ans2"


# Runner
################################################################################


def jingle(text=None, filepath=None, extra_args=None):
    if not text and filepath:
        with open(filepath, "r") as f:
            text = f.read()
    sack.present(text, extra_args, parse, part1, part2)


if __name__ == "__main__":
    import sys
    import sack

    file = sys.argv[1] if len(sys.argv) > 1 else None
    filepath = sack.get_filepath(file)
    if filepath:
        extra_args = sys.argv[2:]
        jingle(filepath=filepath, extra_args=extra_args)
