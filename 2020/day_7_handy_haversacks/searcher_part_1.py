from bags_getter import get_bags


def get_number_of_bags_which_contain(bag_name, file_path):
    return len([bag for bag in get_bags(file_path) if _search_bag(bag, bag_name)])


def _search_bag(bag, searched_name):
    for inside_bag_data in bag.content:
        if inside_bag_data[1].name == searched_name or _search_bag(inside_bag_data[1], searched_name):
            return True
    return False
