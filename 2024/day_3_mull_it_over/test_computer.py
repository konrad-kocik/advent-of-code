from computer import add_up_results_of_all_instructions_from_memory


def test_add_up_results_of_all_instructions_from_memory():
    assert add_up_results_of_all_instructions_from_memory('test_input.raw') == 161


def test_add_up_results_of_all_instructions_from_memory_with_conditional_statements():
    assert add_up_results_of_all_instructions_from_memory('test_input.raw', conditional_statements=True) == 48
