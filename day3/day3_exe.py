import sys
import os

# added the parent directory to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from corrupted_memory import CorruptedMemory

if __name__ == "__main__":
    
    # sample
    corrupted_memory_sample = CorruptedMemory("sample_input.txt")
    print("Uncorrupted instructions sample sum: " + str(corrupted_memory_sample.compute_uncorrupted_sum()))
    
    corrupted_memory_sample_2 = CorruptedMemory("sample_input_2.txt")
    print("Uncorrupted instructions sample 2 sum:" + str(corrupted_memory_sample_2.compute_uncorrupted_sum_new()))

    # real
    corrupted_memory_real = CorruptedMemory("input.txt")
    print("Uncorrupted instructions real sum: " + str(corrupted_memory_real.compute_uncorrupted_sum()))

    corrupted_memory_real_2 = CorruptedMemory("input_2.txt")
    print("Uncorrupted instructions real 2 sum:" + str(corrupted_memory_real_2.compute_uncorrupted_sum_new()))
     
