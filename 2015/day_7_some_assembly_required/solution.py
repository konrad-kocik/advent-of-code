from circuit import Circuit

print('\nSolving first part of puzzle')
circuit = Circuit()
circuit.assemble('input.raw')
circuit.run()
wire_a_signal = circuit.read_signal(wire_name='a')
print(f'Answer to first part of puzzle is: {wire_a_signal}')

print('\nSolving second part of puzzle')
circuit = Circuit()
circuit.assemble('input.raw')
circuit.override(wire_name='b', signal=wire_a_signal)
circuit.run()
wire_a_signal = circuit.read_signal(wire_name='a')
print(f'Answer to second part of puzzle is: {wire_a_signal}')
