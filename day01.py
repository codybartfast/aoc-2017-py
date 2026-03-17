#  2017 Day 01
#  ===========
#
#  Part 1: 1097
#  Part 2: 1188
#
#
#  Timings
#  ---------------------------------
#    Parse:     0.000000    0.250 µs
#   Part 1:     0.000049   49.42  µs
#   Part 2:     0.000047   47.42  µs
#  Elapsed:     0.000138  137.5   µs
#  ---------------------------------
#
#     Date: March 2026
#  Machine: MacBook M4
#   Python: 3.14.3


def parse(text):
    return text


def solve_captcha(captcha, offset):
    return sum(
        int(c1)
        for c1, c2 in zip(captcha, captcha[offset:] + captcha[:offset])
        if c1 == c2
    )


def part1(captcha, args, p1_state):
    return solve_captcha(captcha, 1)


def part2(captcha, args, p1_state):
    return solve_captcha(captcha, len(captcha) // 2)


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
