#  2017 Day 21
#  ===========
#
#  Part 1: 171
#  Part 2: 2498142
#
#  Timings
#  --------------------------------------
#      Parse:     0.000027s  (27.42 µs)
#     Part 1:     0.002073s  (2.073 ms)
#     Part 2:     0.000055s  (54.58 µs)
#    Elapsed:     0.002194s  (2.194 ms)
#  --------------------------------------
#
#     Date:  March 2026
#  Machine:  MacBook M4
#   Python:  3.14.3


# This is a slight mess.  I started with a memoized approach that completed in
# about 1ms but was incorrect for a reason I never fathomed.  So I wrote the
# naive solution (which takes around 800ms) and then used that to build the
# three_to_threes table, where the original bug was likely hiding itself.
#
# The memoized approach relies on a 3x3 grid giving us a 9x9 grid after 3
# iterations which can then be split into 9 3x3 grids.
#
# Once we have the three_to_threes table 18 iterations only takes 0.06ms.


from itertools import batched


def parse(text):

    lines = text.splitlines()
    short = len(lines[0])
    _2_to_3 = []
    _3_to_4 = []

    for line in lines:
        (_2_to_3 if len(line) == short else _3_to_4).append(line.split(" => "))

    return dict(_2_to_3), dict(_3_to_4)


def to_str(grid):
    return "/".join("".join(row) for row in grid)


# Naive
################################################################################


def count(grid):
    return sum(1 for line in grid for char in line if char == "#")


def squares_from_row(row, dim):
    return [
        [row[y][x : x + dim] for y in range(dim)] for x in range(0, len(row[0]), dim)
    ]


def to_squares(grid, dim):
    rows = batched(grid, dim)
    return [squares_from_row(row, dim) for row in rows]


def row_from_squares(squares, dim):
    return [[char for square in squares for char in square[y]] for y in range(dim)]


def extend_row(row, dim, extend, normal):
    str_squares = [to_str(square) for square in squares_from_row(row, dim)]
    str_new_squares = [extend[normal[str_square]] for str_square in str_squares]
    new_squares = [str_square.split("/") for str_square in str_new_squares]
    return row_from_squares(new_squares, dim + 1)


def make_grid(grid, iterations, two_to_three, three_to_four, normal2, normal3):

    if not iterations:
        return grid

    if len(grid) % 2 == 0:
        dim = 2
        extend = two_to_three
        normal = normal2
    else:
        dim = 3
        extend = three_to_four
        normal = normal3

    rows = batched(grid, dim)
    grid = [
        line
        for row in [extend_row(row, dim, extend, normal) for row in rows]
        for line in row
    ]
    return make_grid(
        grid, iterations - 1, two_to_three, three_to_four, normal2, normal3
    )


# Memoized
################################################################################


def count_pixels(
    three,
    iterations,
    known,
    two_to_three,
    three_to_four,
    normal2,
    normal3,
    three_to_threes,
):

    key = (iterations, three)
    if key in known:
        return known[key]

    if iterations == 0:
        value = three.count("#")
    elif iterations == 1:
        value = three_to_four[three].count("#")
    elif iterations == 2:
        grid = make_grid(
            three.split("/"), 2, two_to_three, three_to_four, normal2, normal3
        )
        value = count(grid)
    else:
        value = sum(
            count_pixels(
                next_three,
                iterations - 3,
                known,
                two_to_three,
                three_to_four,
                normal2,
                normal3,
                three_to_threes,
            )
            for next_three in three_to_threes[three]
        )
    known[key] = value
    return value


def normaliser(dict):
    normalise = {}
    for pattern in list(dict.keys()):
        grid = list(map(list, pattern.split("/")))
        for _ in range(4):
            for row in grid:
                row.reverse()
            normalise[to_str(grid)] = pattern
            grid = list(map(list, zip(*grid)))
            normalise[to_str(grid)] = pattern

    return normalise


def make_three_to_threes(two_to_three, three_to_four, normal2, normal3):
    three_to_threes = {}
    for three in three_to_four.keys():
        nine = make_grid(
            three.split("/"), 3, two_to_three, three_to_four, normal2, normal3
        )
        three_to_threes[three] = [
            normal3[to_str(three)] for row in to_squares(nine, 3) for three in row
        ]
    return three_to_threes


def part1(design, args, p1_state):
    two_to_three, three_to_four = design
    normal2 = normaliser(two_to_three)
    normal3 = normaliser(three_to_four)
    three_to_threes = make_three_to_threes(
        two_to_three, three_to_four, normal2, normal3
    )
    p1_state.value = normal2, normal3, three_to_threes
    return count_pixels(
        normal3[".#./..#/###"],
        5,
        {},
        two_to_three,
        three_to_four,
        normal2,
        normal3,
        three_to_threes,
    )


def part2(design, args, p1_state):
    two_to_three, three_to_four = design
    normal2, normal3, three_to_threes = p1_state.value
    return count_pixels(
        normal3[".#./..#/###"],
        18,
        {},
        two_to_three,
        three_to_four,
        normal2,
        normal3,
        three_to_threes,
    )


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
