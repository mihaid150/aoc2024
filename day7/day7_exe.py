import sys
import os

# added the parent directory to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bridge_repair import BridgeRepair

if __name__ == "__main__":
    # sample
    # bridge_repair_sample = BridgeRepair("sample_input.txt")
    # print("Calibration sum for sample is " + str(bridge_repair_sample.evaluate_equations()))

    # sample corner cases
    # bridge_repair_sample_corner = BridgeRepair("sample_input_corner.txt")
    # print("Calibration sum for sample is " + str(bridge_repair_sample_corner.evaluate_equations()))

    # real
    bridge_repair_real = BridgeRepair("input.txt")
    print("Calibration sum for real is " + str(bridge_repair_real.evaluate_equations()))
