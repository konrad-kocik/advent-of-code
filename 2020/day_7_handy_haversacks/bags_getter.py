from bag import Bag


def get_bags(file_path):
    bags = []

    with open(file_path, 'r') as file:
        for line in file:
            bag_name, inside_bags_data = map(str.strip, line.strip()[:-1].split('bags contain'))
            inside_bags_data = _parse_inside_bags_data(inside_bags_data)
            inside_bags = _create_inside_bags(inside_bags_data, bags)
            _update_bags(bags, bag_name, inside_bags)

    return bags


def _parse_inside_bags_data(inside_bags_data):
    inside_bags_data = [] if inside_bags_data == 'no other bags' else inside_bags_data.split(', ')
    inside_bags_data = [inside_bag_data.split(' ', maxsplit=1) for inside_bag_data in inside_bags_data]

    for inside_bag_data in inside_bags_data:
        inside_bag_data[0] = int(inside_bag_data[0])
        to_replace = ' bags' if inside_bag_data[1].endswith('bags') else ' bag'
        inside_bag_data[1] = inside_bag_data[1].replace(to_replace, '')

    return inside_bags_data


def _create_inside_bags(inside_bags_data, bags):
    inside_bags = []

    for inside_bag_count, inside_bag_name in inside_bags_data:

        found = False
        for bag in bags:
            if bag.name == inside_bag_name:
                inside_bags.append((inside_bag_count, bag))
                found = True
                break
        if not found:
            bag = Bag(inside_bag_name, [])
            bags.append(bag)
            inside_bags.append((inside_bag_count, bag))

    return inside_bags


def _update_bags(bags, bag_name, inside_bags):
    found = False

    for bag in bags:
        if bag.name == bag_name:
            found = True
            bag.add_content(inside_bags)
            break

    if not found:
        bags.append(Bag(bag_name, inside_bags))
