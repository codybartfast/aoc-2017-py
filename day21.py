from itertools import batched


def parse(text):
    def parse_line(line):
        return line.split(" => ")

    lines = text.splitlines()
    start_len = len(lines[0])
    two_to_three = []
    three_to_four = []

    for line in lines:
        if len(line) == start_len:
            two_to_three.append(parse_line(line))
        else:
            three_to_four.append(parse_line(line))

    return dict(two_to_three), dict(three_to_four)


def normaliser(dict):
    def make_key(grid):
        return "/".join("".join(row) for row in grid)

    normalise = {}
    for pattern in list(dict.keys()):
        grid = list(map(list, pattern.split("/")))
        for _ in range(4):
            for row in grid:
                row.reverse()
            normalise[make_key(grid)] = pattern
            grid = list(map(list, zip(*grid)))
            normalise[make_key(grid)] = pattern

    return normalise


def split_four(four, normal2):
    parts = [pair for row in four.split("/") for pair in [row[:2], row[2:]]]
    return [
        normal2[f"{parts[0]}/{parts[2]}"],
        normal2[f"{parts[1]}/{parts[3]}"],
        normal2[f"{parts[4]}/{parts[6]}"],
        normal2[f"{parts[5]}/{parts[7]}"],
    ]


def count_pixels(
    three,
    iterations,
    normal2,
    two_to_three,
    three_to_four,
    three_to_threes,
    known,
):
    assert iterations >= 0

    key = (iterations, three)
    if key in known:
        return known[key]

    if iterations == 0:
        value = three.count("#")
    elif iterations == 1:
        value = three_to_four[three].count("#")
    elif iterations == 2:
        four = three_to_four[three]
        twos = split_four(four, normal2)
        threes = [two_to_three[two] for two in twos]
        value = sum(three.count("#") for three in threes)
    else:
        next_threes = three_to_threes[three]
        value = sum(
            count_pixels(
                next_three,
                iterations - 3,
                normal2,
                two_to_three,
                three_to_four,
                three_to_threes,
                known,
            )
            for next_three in next_threes
        )
    known[key] = value
    return value


def threes_to_twos(threes, normal2):
    [top_left, top_right, bottom_left, bottom_right] = threes
    left = top_left.split("/") + bottom_left.split("/")
    right = top_right.split("/") + bottom_right.split("/")
    six = [left[i] + right[i] for i in range(6)]
    return [
        normal2["/".join([six[y][x : x + 2], six[y + 1][x : x + 2]])]
        for y in range(0, 6, 2)
        for x in range(0, 6, 2)
    ]


def split_nine(nine):
    threes = []
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            threes.append(
                "".join(nine[y][x : x + 3])
                + "/"
                + "".join(nine[y + 1][x : x + 3])
                + "/"
                + "".join(nine[y + 2][x : x + 3])
            )
    return threes


def solve(two_to_three, three_to_four, iterations):
    normal2 = normaliser(two_to_three)
    normal3 = normaliser(three_to_four)

    three_to_threes = {}
    for three in three_to_four.keys():
        nine = solve2(
            three.split("/"), 3, two_to_three, three_to_four, normal2, normal3
        )
        threes = split_nine(nine)
        three_to_threes[three] = [normal3[three] for three in threes]

    three = ".#./..#/###"

    return count_pixels(
        normal3[three],
        iterations,
        normal2,
        two_to_three,
        three_to_four,
        three_to_threes,
        {},
    )


################################################################################


def count(grid):
    return sum(1 for line in grid for char in line if char == "#")


def extend_row(row, dim, extend, normal):
    squares = [
        [row[y][x : x + dim] for y in range(dim)] for x in range(0, len(row[0]), dim)
    ]
    str_squares = ["/".join("".join(row) for row in square) for square in squares]
    str_new_squares = [extend[normal[str_square]] for str_square in str_squares]
    new_squares = [str_square.split("/") for str_square in str_new_squares]
    dim += 1
    return [[char for square in new_squares for char in square[y]] for y in range(dim)]


def solve2(grid, iterations, two_to_three, three_to_four, normal2, normal3):

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
    return solve2(grid, iterations - 1, two_to_three, three_to_four, normal2, normal3)


def disp(str_sqr):
    print("\n".join(str_sqr.split("/")))
    print()


def part1(design, args, p1_state):
    two_to_three, three_to_four = design
    return solve(two_to_three, three_to_four, 5)


def part2(design, args, p1_state):
    two_to_three, three_to_four = design
    return solve(two_to_three, three_to_four, 18)


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
