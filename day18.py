from collections import deque

R_PC = 0
R_SND_COUNT = 1
REG_NAMES = ["_PC", "_N_SND", "a", "b", "c", "d", "f", "i", "p"]
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


def boot(program_id):
    prog_reg = REG_NAMES.index("p")
    regs = [0] * len(REG_NAMES)
    regs[prog_reg] = program_id
    return regs


def run(prog, regs, snd_q, rcv_q, part2=False):
    pc = regs[R_PC]
    while 0 <= regs[R_PC] < len(prog):
        match prog[pc]:
            # add
            case (0, (1, r), (arg2_type, val2)):
                regs[r] += regs[val2] if arg2_type else val2
                pc += 1
            # jgz
            case (1, (arg1_type, val1), (arg2_type, val2)):
                if 0 < (regs[val1] if arg1_type else val1):
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
            case (4, (1, val1)):
                if part2:
                    if rcv_q:
                        regs[val1] = rcv_q.popleft()
                        pc += 1
                    else:
                        regs[R_PC] = pc
                        return "waiting"
                else:
                    if regs[val1]:
                        return rcv_q.pop()
            # set
            case (5, (1, r), (arg2_type, val2)):
                regs[r] = regs[val2] if arg2_type else val2
                pc += 1
            # snd
            case (6, (arg1_type, val1)):
                snd_q.append(regs[val1] if arg1_type else val1)
                regs[R_SND_COUNT] += 1
                pc += 1
            case _:
                assert False, prog[pc]

    assert False, regs


def part1(prog, args, p1_state):
    queue = deque()
    return run(prog, boot(0), queue, queue)


def part2(prog, args, p1_state):
    regs0 = boot(0)
    regs1 = boot(1)

    from0 = deque()
    from1 = deque()

    def run0():
        return run(prog, regs0, from0, from1, True)

    def run1():
        return run(prog, regs1, from1, from0, True)

    while run0() == "waiting":
        rslt1 = run1()
        assert rslt1 == "waiting"
        if not from0 and not from1:
            break
    return regs1[R_SND_COUNT]


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
