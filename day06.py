def parse(text):
    return [int(part) for part in text.split()]


def reallocate(data, part2 = False):
    count = 0
    seen = {}
    seen[tuple(data)] = count
    while True:
        count += 1
        (pstn, size) = max(enumerate(data), key=lambda pair: pair[1])
        data[pstn] = 0
        for _ in range(size):
            pstn = (pstn + 1) % len(data)
            data[pstn] += 1
        key = tuple(data)
        if key in seen:
            return count - seen[key] if part2 else count
        seen[key] = count
        
        

def part1(data, args, p1_state):
    print(f"\n{data}\n")
    return reallocate(data.copy())


def part2(data, args, p1_state):
    return reallocate(data, True)


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
