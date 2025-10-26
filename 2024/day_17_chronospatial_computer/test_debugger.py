from pytest import fixture

from debugger import Debugger


@fixture
def debugger():
    debugger = Debugger()
    debugger.initialize('test_input.raw')
    return debugger


def test_run_program(debugger):
    debugger.run_program()
    output = debugger.get_output()
    assert output == '4,6,3,5,6,3,5,2,1,0'
