import sys
import os

# added the parent directory to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from print_queue import SafetyManualUpdate

if __name__ == "__main__":
    
    # sample
    safety_manual_update_sample = SafetyManualUpdate("sample_input.txt")
    safety_manual_update_sample_2 = SafetyManualUpdate("sample_input.txt")

    print("Middle pages ordered number sum sample: " + str(safety_manual_update_sample.sum_middle_page_number()))
    print("Middle pages new ordered number sum sample: " + str(safety_manual_update_sample_2.sum_middle_page_number_new()))

    # real
    safety_manual_update_real = SafetyManualUpdate("input.txt")
    safety_manual_update_real_2 = SafetyManualUpdate("input.txt")
    print("Middle pages ordered number sum real: " + str(safety_manual_update_real.sum_middle_page_number()))
    print("Middle pages new ordered number real sample: " + str(safety_manual_update_real_2.sum_middle_page_number_new()))

 
