def get_sum_of_duplicated_item_type_priorities(file_path):
    rucksacks = _get_rucksacks(file_path)
    duplicated_item_types = _get_duplicated_item_types(rucksacks)
    duplicated_item_type_priorities = _get_item_type_priorities(duplicated_item_types)
    return sum(duplicated_item_type_priorities)


def get_sum_of_badge_priorities(file_path):
    rucksacks = _get_rucksacks(file_path)
    badges = _get_badges(rucksacks)
    badge_priorities = _get_item_type_priorities(badges)
    return sum(badge_priorities)


def _get_rucksacks(file_path):
    rucksacks = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            rucksacks.append([line[:len(line)//2],
                              line[len(line)//2:]])

    return rucksacks


def _get_duplicated_item_types(rucksacks):
    rucksacks_duplicates = []

    for rucksack in rucksacks:
        rucksack_duplicate = None
        first_compartment, second_compartment = rucksack

        for item in first_compartment:
            if item in second_compartment:
                rucksack_duplicate = item
                break

        rucksacks_duplicates.append(rucksack_duplicate)

    return rucksacks_duplicates


def _get_badges(rucksacks):
    rucksacks_badges = []

    while rucksacks:
        rucksack_badge = None

        first_rucksack = rucksacks.pop(0)
        second_rucksack = rucksacks.pop(0)
        third_rucksack = rucksacks.pop(0)

        for item in first_rucksack[0] + first_rucksack[1]:
            if _is_item_in_rucksack(item, second_rucksack) and _is_item_in_rucksack(item, third_rucksack):
                rucksack_badge = item
                break

        rucksacks_badges.append(rucksack_badge)

    return rucksacks_badges


def _is_item_in_rucksack(item, rucksack):
    return item in rucksack[0] or item in rucksack[1]


def _get_item_type_priorities(item_types):
    priorities = []

    for item_type in item_types:
        priorities.append(ord(item_type) - (96 if item_type.islower() else 38))

    return priorities
