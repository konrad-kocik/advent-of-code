def get_sum_of_answers(strategy):
    return sum([len(strategy(group_answers)) for group_answers in _get_groups_answers()])


def _get_groups_answers():
    answers = []

    with open('input.raw', 'r') as file:
        group = []

        for person in file:
            person = person.rstrip()
            if person == '':
                answers.append(group)
                group = []
                continue
            group.append(person)

        answers.append(group)
    return answers


def _get_unique_answers(group):
    return set(''.join(group))


def _get_identical_answers(group):
    if len(group) == 1:
        return set(group[0])

    answers = ''.join(group)
    return set([answer for answer in answers if answers.count(answer) == len(group)])


print(get_sum_of_answers(_get_unique_answers))
print(get_sum_of_answers(_get_identical_answers))
