import sys
import os

# added the parent directory to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from location_distance import Locations

if __name__ == "__main__":

    # sample
    locations_sample = Locations("sample_input.txt")
    print("Distance: " + str(locations_sample.compute_distance()))
    print("Similarity score: " + str(locations_sample.compute_similarity_score()))

    # real
    locations = Locations("input.txt")
    print("Distance: " + str(locations.compute_distance()))
    print("Similarity score: " + str(locations.compute_similarity_score()))
