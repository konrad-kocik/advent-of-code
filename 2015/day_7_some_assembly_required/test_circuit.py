from circuit import Circuit


def test_circuit():
    circuit = Circuit()
    circuit.assemble('test_input.raw')
    circuit.run()
    assert circuit.read_signal('d') == 72
    assert circuit.read_signal('e') == 507
    assert circuit.read_signal('f') == 492
    assert circuit.read_signal('g') == 114
    assert circuit.read_signal('h') == 65412
    assert circuit.read_signal('i') == 65079
    assert circuit.read_signal('x') == 123
    assert circuit.read_signal('y') == 456
