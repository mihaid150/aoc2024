# AOC2024 day 1
import os
from read_input import get_input

class Locations:
    def __init__(self, input_data_path):
        self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
        self.input_data = get_input(input_data_path).splitlines()
        self.first_ids = []
        self.second_ids = []
    
    def parse_data(self):
        for line in self.input_data:
            first_loc_id, second_loc_id = line.split()
            self.first_ids.append(int(first_loc_id))
            self.second_ids.append(int(second_loc_id))
    
    def compute_distance(self):
        self.parse_data()

        total_distance = 0
        while self.first_ids and self.second_ids:
            first_min = min(self.first_ids)
            self.first_ids.remove(first_min)

            second_min = min(self.second_ids)
            self.second_ids.remove(second_min)

            total_distance += abs(first_min - second_min)

        return total_distance

    def count_id_frequency(self, lid, locations):
        count = 0
        for location in locations:
            if lid == location:
                count += 1
        return count

    def compute_similarity_score(self):
        self.parse_data()

        total_score = 0
        for location in self.first_ids:
            total_score += location * self.count_id_frequency(location, self.second_ids)

        return total_score
        

