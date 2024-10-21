from game import play_game, play_game_with_new_rules


def test_play_game():
    assert play_game('test_input.raw') == 15


def test_play_game_with_new_rules():
    assert play_game_with_new_rules('test_input.raw') == 12
