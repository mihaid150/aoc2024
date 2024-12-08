import sys
import os

# added the parent directory to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from guard_gallivant import GuardGallivant
from guard_gallivant_optimized import GuardGallivantOptimized


if __name__ == "__main__":
    # sample
    guard_gallivant_sample = GuardGallivant("sample_input.txt")
    print("Number of guard distinct positions in sample case: " + str(guard_gallivant_sample.start_guard_movement()))

    guard_gallivant_sample_2 = GuardGallivant("sample_input.txt")
    print("Number of possible sample loops is " + str(guard_gallivant_sample_2.count_possible_loops()))

    # real
    guard_gallivant_real = GuardGallivant("input.txt")
    print("Number of guard distinct positions in real case: " + str(guard_gallivant_real.start_guard_movement()))

    guard_gallivant_real_2 = GuardGallivant("input.txt")
    print("Number of possible real loops is " + str(guard_gallivant_real_2.count_possible_loops()))
