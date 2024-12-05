from word_searcher import search_word


def test_search_word_xmas_mode():
    assert search_word('test_input.raw', mode='XMAS') == 18


def test_search_word_x_mas_mode():
    assert search_word('test_input.raw', mode='X-MAS') == 9
