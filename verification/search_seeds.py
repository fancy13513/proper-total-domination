"""Emit the finite seed-search problem as SMT-LIB on stdout.

Example: python search_seeds.py 9 9 --axes RC > search.smt2
         z3 search.smt2
R allows row growth, C allows column growth. Omit --axes for a fixed board.
The search uses Z3. The certificate checker, verify.py, only needs Python 3.
"""
import argparse
from itertools import product


def index_words(length, expandable):
    for k in range(3 if expandable else 1):
        yield [0, 1] * k + list(range(length))


def variable(i, j):
    return f"x{i}_{j}"


def neighbor_sum(names):
    # Three bits represent every possible sum of four bits exactly.
    return "(bvadd " + " ".join(f"(ite {name} #b001 #b000)" for name in names) + ")"


def constraints(height, width, axes):
    result = set()
    for rows, cols in product(index_words(height, "R" in axes), index_words(width, "C" in axes)):
        h, w = len(rows), len(cols)

        def at(i, j):
            return variable(rows[i % h], cols[j % w])

        sums = {}
        for i, j in product(range(h), range(w)):
            names = sorted([at(i-1, j), at(i+1, j), at(i, j-1), at(i, j+1)])
            result.add("(or " + " ".join(names) + ")")
            sums[i, j] = neighbor_sum(names)
        for i, j in sums:
            for ni, nj in [((i+1) % h, j), (i, (j+1) % w)]:
                a, b = sorted([sums[i, j], sums[ni, nj]])
                result.add(f"(distinct {a} {b})")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("height", type=int)
    parser.add_argument("width", type=int)
    parser.add_argument("--axes", choices=["", "R", "C", "RC"], default="")
    args = parser.parse_args()
    if min(args.height, args.width) < 5:
        parser.error("The window lemma in this note assumes dimensions of at least five.")
    names = [variable(i, j) for i, j in product(range(args.height), range(args.width))]
    for name in names:
        print(f"(declare-const {name} Bool)")
    for rule in sorted(constraints(args.height, args.width, args.axes)):
        print(f"(assert {rule})")
    print("(check-sat-using (then simplify bit-blast sat))")
    print("(get-value (" + " ".join(names) + "))")


if __name__ == "__main__":
    main()
