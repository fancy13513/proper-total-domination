"""Reproduce the proof for odd toroidal grids. Run with Python 3, standard library only."""
from collections import defaultdict
from itertools import product


# Each tuple contains the expandable axes and the binary rows of a seed.
SEEDS = [
    ('', [
        '1011011',
        '0001001',
        '1110110',
        '0111011',
        '0000111',
    ]),
    ('', [
        '011011100',
        '100101101',
        '010111011',
        '111010101',
        '110111110',
    ]),
    ('', [
        '11101011111',
        '00011101101',
        '10101111010',
        '10111110011',
        '01011001001',
    ]),
    ('C', [
        '0001000111000',
        '1110110110111',
        '1000011011110',
        '1111010101101',
        '1011101110110',
    ]),
    ('', [
        '1011111',
        '0110101',
        '0111110',
        '1111101',
        '1101010',
        '0110011',
        '0001111',
    ]),
    ('', [
        '001011111',
        '011100110',
        '101110101',
        '010111011',
        '111110001',
        '110110110',
        '011101101',
    ]),
    ('C', [
        '11010100001',
        '10111011010',
        '11110110111',
        '00000111000',
        '10101111110',
        '11100101000',
        '10101111110',
    ]),
    ('RC', [
        '110111101',
        '100101110',
        '000111100',
        '111101101',
        '101011011',
        '011000100',
        '111011110',
        '110100111',
        '100101000',
    ]),
]


def expanded(seed, extra_row_pairs=0, extra_col_pairs=0):
    rows = [0, 1] * extra_row_pairs + list(range(len(seed)))
    cols = [0, 1] * extra_col_pairs + list(range(len(seed[0])))
    return [[int(seed[i][j]) for j in cols] for i in rows]


def check_grid(board):
    h, w = len(board), len(board[0])
    score = [[board[(i-1) % h][j] + board[(i+1) % h][j] +
              board[i][(j-1) % w] + board[i][(j+1) % w]
              for j in range(w)] for i in range(h)]
    for i, j in product(range(h), range(w)):
        s = score[i][j]
        if s == 0 or s == score[(i+1) % h][j] or s == score[i][(j+1) % w]:
            raise ValueError(f"Failed at {(i,j)} on a {h} by {w} board")
    return score


def negative_case():
    """Count all labelled solutions to the 5 x 5 case, pruning only failed rows."""
    rows = list(product((0, 1), repeat=5))
    # good[a,b,c] is the score vector of b if it passes every horizontal check.
    good = {}
    after = defaultdict(list)
    for a, b, c in product(range(32), repeat=3):
        v = tuple(rows[a][j] + rows[b][(j-1) % 5] +
                  rows[b][(j+1) % 5] + rows[c][j] for j in range(5))
        if min(v) > 0 and all(v[j] != v[(j+1) % 5] for j in range(5)):
            good[a, b, c] = v
            after[a, b].append(c)

    def different(v, w):
        return all(x != y for x, y in zip(v, w))

    survivors = [0] * 4
    for (a, b, c), vb in good.items():
        for d in after[b, c]:
            vc = good[b, c, d]
            if not different(vb, vc):
                continue
            survivors[0] += 1
            for e in after[c, d]:
                vd = good[c, d, e]
                if not different(vc, vd):
                    continue
                survivors[1] += 1
                ve = good.get((d, e, a))
                if ve is None or not different(vd, ve):
                    continue
                survivors[2] += 1
                va = good.get((e, a, b))
                if va is not None and different(ve, va) and different(va, vb):
                    survivors[3] += 1
    return len(good), survivors


def verify():
    total = 0
    for axes, seed in SEEDS:
        if any(len(s) != len(seed[0]) or set(s) - {"0", "1"} for s in seed):
            raise ValueError("Malformed binary row")
        for i in range(3 if "R" in axes else 1):
            for j in range(3 if "C" in axes else 1):
                check_grid(expanded(seed, i, j))
                total += 1
    triples, survivors = negative_case()
    print("Positive certificates checked:", total)
    print("Valid 5-column row triples:", triples)
    print("Counts after successive vertical checks:", *survivors)
    if survivors[-1] != 0:
        raise ValueError("A 5 by 5 solution was found")


if __name__ == "__main__":
    verify()
