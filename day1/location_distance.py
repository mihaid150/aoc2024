# AOC2024 day 1
import os
from read_input import get_input
from collections import Counter

class Locations:
    def __init__(self, input_data_path):
        self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
        self.input_data = get_input(input_data_path).splitlines()
        self.first_ids = []
        self.second_ids = []
    
    def parse_data(self):
        self.first_ids, self.second_ids = zip(*(map(int, line.split()) for line in self.input_data))
    
    def compute_distance(self):
        self.parse_data()

        fst_ids = sorted(self.first_ids)
        snd_ids = sorted(self.second_ids)
        
        return sum(abs(fst - snd) for fst, snd in zip(fst_ids, snd_ids))

    def compute_similarity_score(self):
        self.parse_data()

        second_id_counts = Counter(self.second_ids)
        return sum(location * second_id_counts.get(location, 0) for location in self.first_ids)
        

