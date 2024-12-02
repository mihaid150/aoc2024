# AOC2024 day2
import os
from read_input import get_input

class UnusualData:
    def __init__(self, input_data_path):
        self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
        self.input_data = get_input(input_data_path).splitlines()
        self.reports = []

    def parse_data(self):
        self.reports = [list(map(int, line.split())) for line in self.input_data]
   
   # part 1

    def test_increasing_report(self, report):
        return all(a < b and 1 <= abs(a - b) <= 3 for a, b in zip(report, report[1:]))

    def test_decreasing_report(self, report):
        return all(a > b and 1 <= abs(a - b) <= 3 for a, b in zip(report, report[1:]))

    def is_safe_report(self, report):
        if self.test_increasing_report(report) or self.test_decreasing_report(report):
            return True
        return False

    def count_safety_reports(self):
        self.parse_data()
        
        return sum(1 for report in self.reports if self.is_safe_report(report))
        
    # part 2
    
    def is_safe_report_with_tolerance(self, report):
        
        # no need to remove a level first
        if self.test_increasing_report(report) or self.test_decreasing_report(report):
            return True

        # test by removing an element
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            if self.test_increasing_report(new_report) or self.test_decreasing_report(new_report):
                return True

        # more than one tolerance
        return False

    def count_safety_reports_with_tolerance(self):
        self.parse_data()

        return sum(1 for report in self.reports if self.is_safe_report_with_tolerance(report))
        


