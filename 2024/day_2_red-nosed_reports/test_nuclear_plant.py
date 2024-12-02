from nuclear_plant import count_safe_reports


def test_count_safe_reports():
    assert count_safe_reports('test_input.raw') == 2


def test_count_safe_reports_with_problem_dampener():
    assert count_safe_reports('test_input.raw', problem_dampener=True) == 4
