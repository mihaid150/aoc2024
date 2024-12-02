import sys
import os

# added the parent directory to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from safety_reports import UnusualData

if __name__ == "__main__":
    
    # sample
    unusual_data_sample = UnusualData("sample_input.txt")
    print("Safety reports: " + str(unusual_data_sample.count_safety_reports()))
    print("Safety reports with one tolerance: " + str(unusual_data_sample.count_safety_reports_with_tolerance()))

    # real
    unusual_data = UnusualData("input.txt")
    print("Safety reports: " + str(unusual_data.count_safety_reports()))
    print("Safety reports with one tolerance: " + str(unusual_data.count_safety_reports_with_tolerance()))
