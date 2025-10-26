from typing import Tuple
from math import trunc

Instruction = Tuple[int, int]


class Debugger:
    def __init__(self):
        self._register_a = 0
        self._register_b = 0
        self._register_c = 0
        self._program = ''
        self._instruction_pointer = 0
        self._output = []

    def initialize(self, input_file_path: str):
        with open(input_file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if line.startswith('Register A'):
                    self._register_a = int(line.split(': ')[1])
                elif line.startswith('Register B'):
                    self._register_b = int(line.split(': ')[1])
                elif line.startswith('Register C'):
                    self._register_c = int(line.split(': ')[1])
                elif line.startswith('Program'):
                    self._program = line.split(': ')[1].replace(',', '')

    def run_program(self):
        while self._instruction_pointer < len(self._program):
            instruction = self._get_instruction()
            self._execute_instruction(instruction)

    def get_output(self) -> str:
        return ','.join(self._output)

    def _get_instruction(self) -> Instruction:
        return int(self._program[self._instruction_pointer]), int(self._program[self._instruction_pointer + 1])

    def _execute_instruction(self, instruction: Instruction):
        opcode, operand = instruction

        if opcode == 0:
            self._execute_adv(operand)
        elif opcode == 1:
            self._execute_bxl(operand)
        elif opcode == 2:
            self._execute_bst(operand)
        elif opcode == 3:
            self._execute_jnz(operand)
        elif opcode == 4:
            self._execute_bxc()
        elif opcode == 5:
            self._execute_out(operand)
        elif opcode == 6:
            self._execute_bdv(operand)
        elif opcode == 7:
            self._execute_cdv(operand)
        else:
            raise Exception(f'Invalid opcode {opcode}')

    def _execute_adv(self, operand: int):
        self._register_a = trunc(self._register_a / (2 ** self._translate_combo_operand(operand)))
        self._step_to_next_instruction()

    def _execute_bxl(self, operand: int):
        self._register_b = self._register_b ^ operand
        self._step_to_next_instruction()

    def _execute_bst(self, operand: int):
        self._register_b = self._translate_combo_operand(operand) % 8
        self._step_to_next_instruction()

    def _execute_jnz(self, operand: int):
        if self._register_a != 0:
            self._instruction_pointer = operand
        else:
            self._step_to_next_instruction()

    def _execute_bxc(self):
        self._register_b = self._register_b ^ self._register_c
        self._step_to_next_instruction()

    def _execute_out(self, operand: int):
        self._output.append(str(self._translate_combo_operand(operand) % 8))
        self._step_to_next_instruction()

    def _execute_bdv(self, operand: int):
        self._register_b = trunc(self._register_a / (2 ** self._translate_combo_operand(operand)))
        self._step_to_next_instruction()

    def _execute_cdv(self, operand: int):
        self._register_c = trunc(self._register_a / (2 ** self._translate_combo_operand(operand)))
        self._step_to_next_instruction()

    def _translate_combo_operand(self, operand: int) -> int:
        if operand in (0, 1, 2, 3):
            return operand
        elif operand == 4:
            return self._register_a
        elif operand == 5:
            return self._register_b
        elif operand == 6:
            return self._register_c
        else:
            raise Exception(f'Invalid combo operand {operand}')

    def _step_to_next_instruction(self):
        self._instruction_pointer += 2
