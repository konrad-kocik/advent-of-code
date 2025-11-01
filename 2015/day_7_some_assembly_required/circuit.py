from functools import reduce
from operator import and_, or_


class CircuitPart:
    def __init__(self):
        self._inputs: list['CircuitPart'] = []
        self._outputs: list['CircuitPart'] = []
        self._signal = None

    @property
    def outputs(self) -> list['CircuitPart']:
        return self._outputs

    @property
    def signal(self) -> int:
        return self._signal

    @signal.setter
    def signal(self, value: int):
        self._signal = value

    def connect_input(self, circuit_part: 'CircuitPart'):
        self._inputs.append(circuit_part)

    def connect_output(self, circuit_part: 'CircuitPart'):
        self._outputs.append(circuit_part)

    def evaluate(self):
        raise NotImplementedError()


class Wire(CircuitPart):
    def __init__(self, name: str):
        super().__init__()
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def evaluate(self):
        if self._inputs:
            if self._inputs[0].signal is None:
                self._inputs[0].evaluate()
            self._signal = self._inputs[0].signal


class AndGate(CircuitPart):
    def evaluate(self):
        for input_part in self._inputs:
            if input_part.signal is None:
                input_part.evaluate()
        self._signal = reduce(and_, [input_part.signal for input_part in self._inputs])


class OrGate(CircuitPart):
    def evaluate(self):
        for input_part in self._inputs:
            if input_part.signal is None:
                input_part.evaluate()
        self._signal = reduce(or_, [input_part.signal for input_part in self._inputs])


class NotGate(CircuitPart):
    def evaluate(self):
        if self._inputs[0].signal is None:
            self._inputs[0].evaluate()
        self._signal = ~self._inputs[0].signal & 0xFFFF


class LshiftGate(CircuitPart):
    def __init__(self, shift_amount: int):
        super().__init__()
        self._shift_amount = shift_amount

    def evaluate(self):
        if self._inputs[0].signal is None:
            self._inputs[0].evaluate()
        self._signal = self._inputs[0].signal << self._shift_amount


class RshiftGate(CircuitPart):
    def __init__(self, shift_amount: int):
        super().__init__()
        self._shift_amount = shift_amount

    def evaluate(self):
        if self._inputs[0].signal is None:
            self._inputs[0].evaluate()
        self._signal = self._inputs[0].signal >> self._shift_amount


class Circuit:
    def __init__(self):
        self._wires: list[Wire] = []

    def assemble(self, input_file_path: str):
        with open(input_file_path, 'r') as input_file:
            for instruction in input_file:
                if 'AND' in instruction:
                    self._install_and_gate(instruction)
                elif 'OR' in instruction:
                    self._install_or_gate(instruction)
                elif 'NOT' in instruction:
                    self._install_not_gate(instruction)
                elif 'LSHIFT' in instruction:
                    self._install_lshift_gate(instruction)
                elif 'RSHIFT' in instruction:
                    self._install_rshift_gate(instruction)
                elif instruction[0].isdigit():
                    self._install_input_wire(instruction)
                else:
                    self._install_wires(instruction)

    def run(self):
        for output_wire in [wire for wire in self._wires if not wire.outputs]:
            output_wire.evaluate()

    def read_signal(self, wire_name: str) -> int:
        wire = self._find_wire(wire_name)
        return wire.signal

    def override(self, wire_name: str, signal: int):
        wire = self._find_wire(wire_name)
        wire.signal = signal

    def _install_and_gate(self, instruction: str):
        input_wire_name_1, _, input_wire_name_2, _, output_wire_name = instruction.split()
        input_wire_1 = self._install_wire(input_wire_name_1)
        input_wire_2 = self._install_wire(input_wire_name_2)
        output_wire = self._install_wire(output_wire_name)
        gate = AndGate()
        self._connect_circuit_parts(input_wire_1, gate)
        self._connect_circuit_parts(input_wire_2, gate)
        self._connect_circuit_parts(gate, output_wire)

    def _install_or_gate(self, instruction: str):
        input_wire_name_1, _, input_wire_name_2, _, output_wire_name = instruction.split()
        input_wire_1 = self._install_wire(input_wire_name_1)
        input_wire_2 = self._install_wire(input_wire_name_2)
        output_wire = self._install_wire(output_wire_name)
        gate = OrGate()
        self._connect_circuit_parts(input_wire_1, gate)
        self._connect_circuit_parts(input_wire_2, gate)
        self._connect_circuit_parts(gate, output_wire)

    def _install_not_gate(self, instruction: str):
        _, input_wire_name, _, output_wire_name = instruction.split()
        input_wire = self._install_wire(input_wire_name)
        output_wire = self._install_wire(output_wire_name)
        gate = NotGate()
        self._connect_circuit_parts(input_wire, gate)
        self._connect_circuit_parts(gate, output_wire)

    def _install_lshift_gate(self, instruction: str):
        input_wire_name, _, shift_amount, _, output_wire_name = instruction.split()
        input_wire = self._install_wire(input_wire_name)
        output_wire = self._install_wire(output_wire_name)
        gate = LshiftGate(int(shift_amount))
        self._connect_circuit_parts(input_wire, gate)
        self._connect_circuit_parts(gate, output_wire)

    def _install_rshift_gate(self, instruction: str):
        input_wire_name, _, shift_amount, _, output_wire_name = instruction.split()
        input_wire = self._install_wire(input_wire_name)
        output_wire = self._install_wire(output_wire_name)
        gate = RshiftGate(int(shift_amount))
        self._connect_circuit_parts(input_wire, gate)
        self._connect_circuit_parts(gate, output_wire)

    def _install_input_wire(self, instruction: str):
        input_signal, _, input_wire_name = instruction.split()
        input_wire = self._install_wire(input_wire_name)
        input_wire.signal = int(input_signal)

    def _install_wires(self, instruction: str):
        input_wire_name, _, output_wire_name = instruction.split()
        input_wire = self._install_wire(input_wire_name)
        output_wire = self._install_wire(output_wire_name)
        self._connect_circuit_parts(input_wire, output_wire)

    def _install_wire(self, wire_name: str) -> Wire:
        if not wire_name.isdigit():
            wire = self._find_wire(wire_name)

            if not wire:
                wire = Wire(wire_name)
                self._wires.append(wire)
        else:
            wire = Wire('input_signal')
            wire.signal = int(wire_name)

        return wire

    def _find_wire(self, wire_name: str) -> Wire | None:
        for wire in self._wires:
            if wire.name == wire_name:
                return wire
        return None

    @staticmethod
    def _connect_circuit_parts(input_part: CircuitPart, output_part: CircuitPart):
        input_part.connect_output(output_part)
        output_part.connect_input(input_part)
