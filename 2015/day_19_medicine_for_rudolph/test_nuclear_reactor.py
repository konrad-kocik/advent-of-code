from pytest import mark

from nuclear_reactor import NuclearReactor


@mark.parametrize('input_file_path, expected_output_lenght', 
                  [('test_input_1.raw', 4),
                   ('test_input_2.raw', 7)])
def test_nuclear_reactor(input_file_path, expected_output_lenght):
    nuclear_reactor = NuclearReactor()
    nuclear_reactor.load_molecule(input_file_path)
    nuclear_reactor.fuse()
    assert len(nuclear_reactor.output) == expected_output_lenght
