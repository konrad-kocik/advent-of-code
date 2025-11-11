from typing import Tuple
from math import trunc

Instruction = Tuple[int, int]


class Debugger:
    def __init__(self, input_file_path: str):
        self._input_file_path = input_file_path
        self._initial_register_a = 0
        self._register_a = 0
        self._register_b = 0
        self._register_c = 0
        self._program = ''
        self._instruction_pointer = 0
        self._output = []

    def run_program(self):
        self._initialize()
        self._execute_instructions()

    def copy_program(self):
        checked_initial_register_a = 0

        while checked_initial_register_a < 50000000:
            checked_initial_register_a += 1
            self._initialize()
            self._initial_register_a = checked_initial_register_a
            self._register_a = checked_initial_register_a
            self._execute_instructions()

            if self.read_output().replace(',', '') == self._program:
                break

    def read_output(self) -> str:
        return ','.join(self._output)

    def read_initial_register_a(self):
        return self._initial_register_a

    def _initialize(self):
        with open(self._input_file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if line.startswith('Register A'):
                    self._register_a = int(line.split(': ')[1])
                    self._initial_register_a = self._register_a
                elif line.startswith('Register B'):
                    self._register_b = int(line.split(': ')[1])
                elif line.startswith('Register C'):
                    self._register_c = int(line.split(': ')[1])
                elif line.startswith('Program'):
                    self._program = line.split(': ')[1].replace(',', '')

        self._instruction_pointer = 0
        self._output = []

    def _execute_instructions(self):
        while self._instruction_pointer < len(self._program):
            instruction = self._get_instruction()
            self._execute_instruction(instruction)

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
