def parse(text):
    def parse_line(line):
        ps = line.split()
        return (ps[0], ps[1], int(ps[2]), ps[4], ps[5], int(ps[6]))

    lines = text.splitlines()
    return [parse_line(line) for line in lines]


def run(prog):
    regs = {}
    maximum = -(10 ** 18)
    for mod_reg, op, diff, comp_reg, comp, comp_val in prog:
        comp_reg_val = regs.get(comp_reg, 0)
        match comp:
            case "==":
                do_act = comp_reg_val == comp_val
            case "!=":
                do_act = comp_reg_val != comp_val
            case "<":
                do_act = comp_reg_val < comp_val
            case "<=":
                do_act = comp_reg_val <= comp_val
            case ">":
                do_act = comp_reg_val > comp_val
            case ">=":
                do_act = comp_reg_val >= comp_val
            case _:
                assert False, comp
        if do_act:
            diff = diff if op == "inc" else -diff
            val = regs.get(mod_reg, 0) + diff
            if val > maximum:
                maximum = val
            regs[mod_reg] = val 
    return regs, maximum


def part1(prog, args, p1_state):
    # print(f"\n{data}\n")
    registers, maximum = run(prog)
    p1_state.value = maximum
    return max(registers.values())


def part2(_, __, p1_state):
    return p1_state.value


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
