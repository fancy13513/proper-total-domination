"""Reproduce the two main results. Add --cross-check for the NumPy audit."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
CHECKS = ROOT / "verification"


def checked_output(arguments, expected):
    run = subprocess.run(arguments, check=True, capture_output=True, text=True)
    if run.stdout.splitlines() != expected.splitlines():
        raise RuntimeError("Output differed from the reference:\n" + run.stdout)
    return run.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cross-check", action="store_true")
    opts = parser.parse_args()
    compiler = shutil.which("g++") or shutil.which("clang++")
    if not compiler:
        parser.exit(2, "This run needs g++ or clang++ on PATH.\n")
    original = checked_output([sys.executable, str(CHECKS / "verify.py")],
                              (ROOT / "results" / "seeds.txt").read_text())
    print(original, end="")
    with tempfile.TemporaryDirectory() as temp:
        for program, reference in [("exhaustive_5x5", "exhaustive.txt"),
                                   ("width_five", "width-five.txt")]:
            exe = Path(temp) / (program + (".exe" if os.name == "nt" else ""))
            subprocess.run([compiler, "-std=c++17", "-O3", str(CHECKS / f"{program}.cpp"),
                            "-o", str(exe)], check=True)
            result = checked_output([str(exe)], (ROOT / "results" / reference).read_text())
            print(result, end="")
    if opts.cross_check:
        print(checked_output([sys.executable, str(CHECKS / "recheck.py")],
                             (ROOT / "results" / "cross-check.txt").read_text()), end="")
    print("PASS")


if __name__ == "__main__":
    main()
