from nuclear_plant import count_safe_reports


def test_count_safe_reports():
    assert count_safe_reports('test_input.raw') == 2
