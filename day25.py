from array import array
from itertools import batched


def parse(text):
    lines = text.splitlines()

    begin = ord(lines[0][:-1].split()[-1]) - ord("A")
    steps = int(lines[1].split()[-2])
    blocks = list(batched(lines[2:], 10))
    sentences = [[line[:-1].split()[-1] for line in block[1:]] for block in blocks]

    return begin, steps, tuple(
        (
            (int(ws[2]), (-1 if ws[3] == "left" else 1), ord(ws[4]) - ord("A")),
            (int(ws[6]), (-1 if ws[7] == "left" else 1), ord(ws[8]) - ord("A")),
        )
        for ws in sentences
    )

def part1(blueprint, args, p1_state):
    state, steps, prog = blueprint
    tape = array('B', [0] * (2 ** 14))
    pstn = len(tape) // 2

    for _ in range(steps):
        write, go, state = prog[state][tape[pstn]]
        tape[pstn] = write
        pstn += go

    return sum(tape)


def part2(data, args, p1_state):
    return "Merry Christmas"


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
