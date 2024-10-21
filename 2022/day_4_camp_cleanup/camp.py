def get_count_of_fully_overlapping_section_assignments(file_path):
    section_assignments = _get_section_assignments(file_path)
    fully_overlapping_section_assignments = _get_fully_overlapping_section_assignments(section_assignments)
    return len(fully_overlapping_section_assignments)


def get_count_of_overlapping_section_assignments(file_path):
    section_assignments = _get_section_assignments(file_path)
    overlapping_section_assignments = _get_overlapping_section_assignments(section_assignments)
    return len(overlapping_section_assignments)


def _get_section_assignments(file_path):
    section_assignments = []

    with open(file_path, 'r') as file:
        for line in file:
            first_section, second_section = line.strip().split(',')
            section_assignments.append([[*first_section.split('-')],
                                        [*second_section.split('-')]])

    return section_assignments


def _get_fully_overlapping_section_assignments(section_assignments):
    fully_overlapping_section_assignments = []

    for section_assignment_pair in section_assignments:
        first_section, second_section = _convert_section_assignments_to_sets(section_assignment_pair)

        if first_section.issubset(second_section) or second_section.issubset(first_section):
            fully_overlapping_section_assignments.append(section_assignment_pair)

    return fully_overlapping_section_assignments


def _get_overlapping_section_assignments(section_assignments):
    overlapping_section_assignments = []

    for section_assignment_pair in section_assignments:
        first_section, second_section = _convert_section_assignments_to_sets(section_assignment_pair)

        if first_section.intersection(second_section):
            overlapping_section_assignments.append(section_assignment_pair)

    return overlapping_section_assignments


def _convert_section_assignments_to_sets(section_assignment_pair):
    return set(range(int(section_assignment_pair[0][0]),
                     int(section_assignment_pair[0][1]) + 1)), \
           set(range(int(section_assignment_pair[1][0]),
                     int(section_assignment_pair[1][1]) + 1))
