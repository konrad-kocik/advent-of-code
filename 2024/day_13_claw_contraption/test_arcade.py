from arcade import calculate_minimal_number_of_tokens_to_win_prizes


def test_calculate_minimal_number_of_tokens_to_win_prizes():
    assert calculate_minimal_number_of_tokens_to_win_prizes('test_input.raw') == 480
