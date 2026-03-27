REG_NAMES = ["program_counter", "a", "b", "c", "d", "e", "f", "g", "h"]
R_PC = 0

OPS = ["jnz", "mul", "set", "sub"]
#       0      1      2      3      4      5      6

def parse(text):
    def parse_arg(arg):
        return (1, REG_NAMES.index(arg)) if arg in REG_NAMES else (0, int(arg))

    def parse_line(line):
        parts = line.split()
        return tuple([OPS.index(parts[0])] + [parse_arg(part) for part in parts[1:]])

    return [parse_line(line) for line in text.splitlines()]


def boot():
    regs = [0] * len(REG_NAMES)
    return regs


def run(prog, regs):
    pc = regs[R_PC]
    n_mul = 0
    while 0 <= pc < len(prog):
        op, (t1, a1), (t2, a2) = prog[pc]
        match op:
            # jnz
            case 0:
                pc += (regs[a2] if t2 else a2) if (regs[a1] if t1 else a1) else 1
            # mul
            case 1:
                regs[a1] = regs[a1] * (regs[a2] if t2 else a2)
                pc += 1
                n_mul += 1
            # set
            case 2:
                regs[a1] = regs[a2] if t2 else a2
                pc += 1
            # sub
            case 3:
                regs[a1] = regs[a1] - (regs[a2] if t2 else a2)                
                pc += 1
            case _:
                assert False, prog[pc]

    return n_mul


def part1(prog, args, p1_state):
    return run(prog, boot())


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
