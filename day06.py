#  2017 Day 6
#  ==========
#
#  Part 1: 4074
#  Part 2: 2793
#
#  Timings
#  --------------------------------------
#      Parse:     0.000003s  (3.291 µs)
#     Part 1:     0.005030s  (5.030 ms)
#     Part 2:     0.000000s  (0.333 µs)
#    Elapsed:     0.005078s  (5.078 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


def parse(text):
    return [int(part) for part in text.split()]


def reallocate(memory):
    cycles = 0
    seen = {}
    seen[tuple(memory)] = cycles
    while True:
        cycles += 1
        (bank, size) = max(enumerate(memory), key=lambda pair: pair[1])
        memory[bank] = 0
        for _ in range(size):
            bank = (bank + 1) % len(memory)
            memory[bank] += 1
        key = tuple(memory)
        if key in seen:
            return cycles, cycles - seen[key]
        seen[key] = cycles
        
        

def part1(memory, args, p1_state):
    ans1, ans2 = reallocate(memory)
    p1_state.value = ans2
    return ans1


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
