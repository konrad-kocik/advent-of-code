from printing_department import PrintingDepartment

print('Solving first part of puzzle')
printing_department = PrintingDepartment()
printing_department.load_map('input.raw')
accessable_rolls_of_paper_count = printing_department.count_accessable_rolls_of_paper()
print(f'Answer to first part of puzzle is: {accessable_rolls_of_paper_count}')

print('Solving second part of puzzle')
printing_department = PrintingDepartment()
printing_department.load_map('input.raw')
removed_rolls_of_paper_count = printing_department.remove_rolls_of_paper_until_inaccessable()
print(f'Answer to second part of puzzle is: {removed_rolls_of_paper_count}')
