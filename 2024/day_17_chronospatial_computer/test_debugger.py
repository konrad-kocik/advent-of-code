from debugger import Debugger


def test_run_program():
    debugger = Debugger('test_input_1.raw')
    debugger.run_program()
    output = debugger.read_output()
    assert output == '4,6,3,5,6,3,5,2,1,0'


def test_copy_program():
    debugger = Debugger('test_input_2.raw')
    debugger.copy_program()
    initial_register_a = debugger.read_initial_register_a()
    assert initial_register_a == 117440
