from bags_getter import get_bags


def get_number_of_bags_contained_in(bag_name, file_path):
    for bag in get_bags(file_path):
        if bag.name == bag_name:
            return _count_inside_bags(1, bag) - 1


def _count_inside_bags(count, bag):
    return count + count * sum([_count_inside_bags(*bag_data) for bag_data in bag.content])
