from word_searcher import search_word


def test_search_word():
    assert search_word('XMAS', 'test_input.raw') == 18
