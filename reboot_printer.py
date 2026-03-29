#
#  Total Time: 30.27 s
#

from pathlib import Path
import sack

BASE = Path(__file__).parent


def read_solvers():
    import runpy

    solvers = []

    for day in range(1, 26):
        sol_path = BASE / f"day{day:02}.py"
        if not sol_path.is_file():
            next

        jingle = runpy.run_path(str(sol_path), init_globals={"sack": sack})["jingle"]

        input_file = BASE / f"input/2017/day{day:02}/input.txt"
        input = open(input_file).read().strip("\n")

        solvers.append((jingle, input))

    return solvers


def run_all():
    import time

    def h_print(*args):
        print("# ", *args)

    solvers = read_solvers()

    start = time.perf_counter()

    for solver, input in solvers:
        solver(text=input)

    stop = time.perf_counter()

    print()
    print()
    h_print()
    h_print(f"Total Time: {sack.friendly_time(stop - start)}")
    h_print()
    print()


if __name__ == "__main__":
    run_all()
