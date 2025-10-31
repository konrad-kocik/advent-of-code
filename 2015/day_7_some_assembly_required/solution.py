from circuit import Circuit

print('\nSolving first part of puzzle')
circuit = Circuit()
circuit.assemble('input.raw')
circuit.run()
wire_a_signal = circuit.read_signal('a')
print(f'Answer to first part of puzzle is: {wire_a_signal}')
