from printing_department import PrintingDepartment


def test_count_accessable_rolls_of_paper():
    printing_department = PrintingDepartment()
    printing_department.load_map('test_input.raw')
    accessable_rolls_of_paper_count = printing_department.count_accessable_rolls_of_paper()
    assert accessable_rolls_of_paper_count == 13
