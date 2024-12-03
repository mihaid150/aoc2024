import os
import re
from read_input import get_input
from typing import List

class CorruptedMemory:
    def __init__(self, input_data_path: str):
        self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
        self.input_data = get_input(input_data_path).splitlines()
        self.full_input_data = ''.join(self.input_data)
        self.uncorrupted_inst = []
        self.mul_pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
        self.number_pattern = re.compile(r'\d+')
        self.complex_pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)')
        self.do_pattern = re.compile(r'do\(\)')
        self.dont_pattern = re.compile(r'don\'t\(\)')

    def parse_instructions(self) -> None:
        self.uncorrupted_inst = self.mul_pattern.findall(self.full_input_data)

    def compute_uncorrupted_sum(self) -> int:
        self.parse_instructions()
        return sum(
            int(operands[0]) * int(operands[1])
            for uncorr_inst in self.uncorrupted_inst
            for operands in [self.number_pattern.findall(uncorr_inst)]
        )

    def parse_instructions_new(self) -> None:
        self.uncorrupted_inst = self.complex_pattern.findall(self.full_input_data)

    def compute_uncorrupted_sum_new(self) -> int:
        self.parse_instructions_new()

        filtered_inst = []
        skip = False
        for inst in self.uncorrupted_inst:
            if self.dont_pattern.match(inst):
                skip = True
            elif self.do_pattern.match(inst):
                skip = False
            elif not skip:
                filtered_inst.append(inst)

        return sum(
            int(operands[0]) * int(operands[1])
            for uncorr_inst in filtered_inst
            for operands in [self.number_pattern.findall(uncorr_inst)]
        )
