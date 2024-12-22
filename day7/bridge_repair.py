import os
import re
from itertools import product  # Import to generate operator combinations
from read_input import get_input


class BridgeRepair:
    def __init__(self, input_data_path) -> None:
        self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
        self.puzzle = get_input(input_data_path).splitlines()

        self.equations = {}
        self.equation_pattern = re.compile(r'^(\d+):\s*(\d+(?:\s+\d+)*)$')

    def parse_data(self):
        for line in self.puzzle:
            match = self.equation_pattern.match(line)
            if match:
                test_value = int(match.group(1))
                operands_str = match.group(2)
                operands = list(map(int, operands_str.split()))
                self.equations[test_value] = operands

    def can_from_lhs_with_add_mul(self, lhs, rhs):
        print(f"lhs: {lhs}")
        print(f"rhs: {rhs}")

        # Edge cases
        if not rhs:
            return lhs == 0
        if len(rhs) == 1:
            return rhs[0] == lhs

        # Generate all combinations of operators for (len(rhs) - 1) slots
        operator_combinations = product(['+', '*'], repeat=len(rhs) - 1)

        for operators in operator_combinations:
            result = rhs[0]  # Start evaluation from the first number
            for i, op in enumerate(operators):
                if op == '+':
                    result += rhs[i + 1]
                elif op == '*':
                    result *= rhs[i + 1]

            # Check if this combination yields the desired LHS
            if result == lhs:
                return True

        # If no combination works, return False
        return False

    def evaluate_equations(self):
        self.parse_data()
        calibration_result = []

        for equation in self.equations:
            lhs = equation
            rhs = self.equations[equation]
            print(f"Processing equation: {lhs} = {rhs}")

            if self.can_from_lhs_with_add_mul(lhs, rhs):
                print(f"Equation {lhs} = {rhs} is valid.")
                calibration_result.append(lhs)
            else:
                print(f"Equation {lhs} = {rhs} is invalid.")

        print(f"Calibration result: {calibration_result}")
        return sum(calibration_result)
