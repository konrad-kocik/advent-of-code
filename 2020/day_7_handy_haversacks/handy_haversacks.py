class Bag:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    def __repr__(self):
        return '{}: {}'.format(self._name, self._content)

    @property
    def name(self):
        return self._name

    @property
    def content(self):
        return self._content

    def add_content(self, content):
        self._content = list(set(self._content + content))


# TODO: refactor this - list comprehension with bools?
def get_number_of_bags_which_contain(bag_name, file_path):
    containing_bags_count = 0

    for bag in _get_bags(file_path):
        containing_bags_count += _search_bag(bag, bag_name)

    return containing_bags_count


def _get_bags(file_path):
    bags = []

    with open(file_path, 'r') as file:
        for line in file:
            bag_name, bags_inside = line.strip()[:-1].split('bags contain')

            bag_name = bag_name.strip()
            bags_inside = bags_inside.strip()

            bags_inside = [] if bags_inside == 'no other bags' else bags_inside.split(', ')
            bags_inside = [bag_inside[2:].replace(' bags', '') for bag_inside in bags_inside]

            content_bags = []
            for new_inside_bag_name in bags_inside:

                if new_inside_bag_name.endswith('bags'):
                    new_inside_bag_name = new_inside_bag_name.replace(' bags', '')
                elif new_inside_bag_name.endswith('bag'):
                    new_inside_bag_name = new_inside_bag_name.replace(' bag', '')

                found = False
                for main_bag in bags:
                    if new_inside_bag_name == main_bag.name:
                        content_bags.append(main_bag)
                        found = True
                        break
                if not found:
                    bag = Bag(new_inside_bag_name, [])
                    content_bags.append(bag)
                    bags.append(bag)

            found = False
            for main_bag in bags:
                if main_bag.name == bag_name:
                    found = True
                    main_bag.add_content(content_bags)
                    break

            if not found:
                bags.append(Bag(bag_name, content_bags))

    return bags


def _search_bag(bag, searched_name):
    for inside_bag in bag.content:
        if inside_bag.name == searched_name or _search_bag(inside_bag, searched_name):
            return 1
    return 0


print(get_number_of_bags_which_contain('shiny gold', 'input.raw'))
