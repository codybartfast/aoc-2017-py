SND = 0
REG_NAMES = ["_SND", "a", "b", "f", "i", "p"]
OPS = ["add", "jgz", "mod", "mul", "rcv", "set", "snd"]
#       0      1      2      3      4      5      6


def parse(text):
    def parse_arg(arg):
        return (1, REG_NAMES.index(arg)) if arg in REG_NAMES else (0, int(arg))

    def parse_line(line):
        parts = line.split()
        match len(parts):
            case 2:
                return OPS.index(parts[0]), parse_arg(parts[1])
            case 3:
                return OPS.index(parts[0]), parse_arg(parts[1]), parse_arg(parts[2])
            case _:
                assert False, line

    lines = text.splitlines()
    return [parse_line(line) for line in lines]


def boot():
    return [0] * len(REG_NAMES)


def run(regs, prog):
    pc = 0
    while 0 <= pc < len(prog):
        match prog[pc]:
            # add
            case (0, (1, r), (arg2_type, val2)):
                regs[r] += regs[val2] if arg2_type else val2
                pc += 1
            # jgz
            case (1, (arg1_type, val1), (arg2_type, val2)):
                if (regs[val1] if arg1_type else val1):
                    pc += regs[val2] if arg2_type else val2
                else:
                    pc += 1
            # mod
            case (2, (1, r), (arg2_type, val2)):
                regs[r] %= regs[val2] if arg2_type else val2
                pc += 1
            # mul
            case (3, (1, r), (arg2_type, val2)):
                regs[r] *= regs[val2] if arg2_type else val2
                pc += 1
            # rcv
            case (4, (arg1_type, val1)):
                if (regs[val1] if arg1_type else val1):
                    return regs[SND]
                pc += 1
            # set
            case (5, (1, r), (arg2_type, val2)):
                regs[r] = regs[val2] if arg2_type else val2
                pc += 1
            # snd
            case (6, (arg1_type, val1)):
                regs[SND] = regs[val1] if arg1_type else val1
                pc += 1
            case _:
                assert False, prog[pc]

    assert False, regs
    


def part1(prog, args, p1_state):
    return run(boot(), prog)


def part2(prog, args, p1_state):
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
