import sys
import os

# added the parent directory to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ceres_search import CeresSearch

if __name__ == "__main__":
    
    # sample
    ceres_search_sample = CeresSearch("sample_input.txt")
    print("Count of linear XMAS in sample: " + str(ceres_search_sample.search_linear_xmas()))
    print("Count of cross XMAS in sample: " + str(ceres_search_sample.search_cross_xmas())) 

    # real
    ceres_search_real = CeresSearch("input.txt")
    print("Count of linear XMAS in real: " + str(ceres_search_real.search_linear_xmas()))
    print("Count of cross XMAS in real: " + str(ceres_search_real.search_cross_xmas()))

