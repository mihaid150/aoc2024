import os
import re
import numpy as np
from typing import List

class CorruptedMemoryNumpy:
    def __init__(self, input_data_path: str):
        self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
        self.input_data = self._get_input(input_data_path).splitlines()
        self.full_input_data = ''.join(self.input_data)
        self.uncorrupted_inst = []
        self.mul_pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
        self.number_pattern = re.compile(r'\d+')
        self.complex_pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)')
        self.do_pattern = re.compile(r'do\(\)')
        self.dont_pattern = re.compile(r'don\'t\(\)')

    def _get_input(self, input_data_path: str) -> str:
        with open(input_data_path, 'r') as file:
            return file.read()

    def parse_instructions(self) -> None:
        self.uncorrupted_inst = self.mul_pattern.findall(self.full_input_data)

    def compute_uncorrupted_sum(self) -> int:
        self.parse_instructions()
        
        operands = np.array([
            list(map(int , self.number_pattern.findall(inst))) 
            for inst in self.uncorrupted_inst
        ])
        
        return np.sum(operands[:, 0] * operands[:, 1])

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

        filtered_operands = np.array([
            list(map(int, self.number_pattern.findall(inst)))
            for inst in filtered_inst
        ])

        return np.sum(filtered_operands[:, 0] * filtered_operands[:, 1]) if filtered_operands.size > 0 else 0
