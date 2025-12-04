from pytest import fixture

from printing_department import PrintingDepartment


@fixture
def printing_department():
    pd = PrintingDepartment()
    pd.load_map('test_input.raw')
    return pd


def test_count_accessable_rolls_of_paper(printing_department: PrintingDepartment):
    accessable_rolls_of_paper_count = printing_department.count_accessable_rolls_of_paper()
    assert accessable_rolls_of_paper_count == 13


def test_remove_rolls_of_paper_until_inaccessable(printing_department: PrintingDepartment):
    removed_rolls_of_paper_count = printing_department.remove_rolls_of_paper_until_inaccessable()
    assert removed_rolls_of_paper_count == 43
