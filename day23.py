#  2017 Day 23
#  ===========
#
#  Part 1: 5929
#  Part 2: 907
#
#  Timings
#  --------------------------------------
#      Parse:     0.000029s  (29.25 µs)
#     Part 1:     0.003702s  (3.702 ms)
#     Part 2:     3.970636s  (3.971 s)
#    Elapsed:     3.974460s  (3.974 s)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


REG_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]

REG_A = REG_NAMES.index("a")
REG_B = REG_NAMES.index("b")
REG_C = REG_NAMES.index("c")
REG_D = REG_NAMES.index("d")
REG_E = REG_NAMES.index("e")
REG_F = REG_NAMES.index("f")
REG_G = REG_NAMES.index("g")
REG_H = REG_NAMES.index("h")


OPS = ["jnz", "mul", "set", "sub", "mod"]
#       0      1      2      3      4
# match case values are hard coded

JNZ = OPS.index("jnz")
MUL = OPS.index("mul")
SET = OPS.index("set")
SUB = OPS.index("sub")
MOD = OPS.index("mod")


def parse(text):
    def parse_arg(arg):
        return (1, REG_NAMES.index(arg)) if arg in REG_NAMES else (0, int(arg))

    def parse_line(line):
        parts = line.split()
        return tuple([OPS.index(parts[0])] + [parse_arg(part) for part in parts[1:]])

    return [parse_line(line) for line in text.splitlines()]


def boot(a=0):
    regs = [0] * len(REG_NAMES)
    regs[REG_NAMES.index("a")] = a
    return regs


def run(prog, regs):
    pc = 0
    n_mul = 0
    while 0 <= pc < len(prog):
        op, (t1, a1), (t2, a2) = prog[pc]
        match op:
            # jnz
            case 0:
                pc += (regs[a2] if t2 else a2) if (regs[a1] if t1 else a1) else 1
            # set
            case 2:
                regs[a1] = regs[a2] if t2 else a2
                pc += 1
            # sub
            case 3:
                regs[a1] = regs[a1] - (regs[a2] if t2 else a2)
                pc += 1
            # mod
            case 4:
                regs[a1] = regs[a1] % (regs[a2] if t2 else a2)
                pc += 1
            # mul
            case 1:
                regs[a1] = regs[a1] * (regs[a2] if t2 else a2)
                pc += 1
                n_mul += 1
            case _:
                assert False, prog[pc]

    return n_mul, regs[REG_H]


def part1(prog, args, p1_state):
    return run(prog, boot())[0]


def part2(prog, args, p1_state):
    prog[10] = SET, (1, REG_G), (1, REG_B)
    prog[11] = MOD, (1, REG_G), (1, REG_D)
    prog[12] = JNZ, (1, REG_G), (0, 8)
    prog[13] = SET, (1, REG_F), (0, 0)
    prog[14] = JNZ, (0, 1), (0, 11)

    for i in range(15, 20):
        prog[i] = None

    return run(prog, boot(1))[1]


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
