from itertools import batched
import re


def parse(text):
    re_digits = re.compile(r"-?\d+")

    def parse_line(line):
        return list(map(tuple, batched(map(int, re_digits.findall(line)), 3)))

    lines = text.splitlines()
    return [(i, parse_line(line)) for i, line in enumerate(lines)]


def magn(v):
    x, y, z = v
    return abs(x) + abs(y) + abs(z)


def tuple_up(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])


def id(particle):
    return particle[0]


def position(particle):
    return particle[1][0]


def accln(particle):
    return particle[1][2]


def tick(particle):
    (_, vects) = particle
    vects[1] = tuple_up(vects[1], vects[2])
    vects[0] = tuple_up(vects[0], vects[1])
    return particle


def part1(particles, args, p1_state):
    particles = sorted(particles, key=lambda p: magn(accln(p)))
    return id(particles[0])


def part2(particles, args, p1_state):
    quiet_limit = 100
    quiet_count = 0
    while quiet_count < quiet_limit:
        seen, dups = set(), set()
        for particle in particles:
            pstn = position(particle)
            if pstn in seen:
                dups.add(pstn)
            else:
                seen.add(pstn)
        if dups:
            quiet_count = 0
        else:
            quiet_count += 1

        particles = [
            tick(particle) for particle in particles if position(particle) not in dups
        ]

    return len(particles)


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
