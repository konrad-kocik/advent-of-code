class InventoryManagementSystem:
    def __init__(self):
        self._fresh_ingredient_ranges: list[tuple[int, int]] = []
        self._ingredients: list[int] = []

    def load_database(self, input_file_path: str):
        with open(input_file_path) as input_file:
            section = 'ranges'

            for line in input_file:
                line = line.strip()

                if not line:
                    section = 'ingredients'
                    continue

                if section == 'ranges':
                    range_start, range_end = line.split('-')
                    self._fresh_ingredient_ranges.append((int(range_start), int(range_end)))
                    
                if section == 'ingredients':
                    self._ingredients.append(int(line))

    def count_fresh_ingredients(self) -> int:
        fresh_ingredients_count = 0
    
        for ingredient in self._ingredients:
            if any([ingredient in range(fresh_range[0], fresh_range[1] + 1) for fresh_range in self._fresh_ingredient_ranges]):
                fresh_ingredients_count += 1

        return fresh_ingredients_count

    def count_all_possible_fresh_ingredients(self) -> int:
        self._merge_overlaping_fresh_ingredient_ranges()
        return self._count_ingredients_in_all_fresh_ranges()

    def _merge_overlaping_fresh_ingredient_ranges(self):
        should_merge = True

        while should_merge:
            merged_fresh_ingredient_ranges = []
            should_merge = False

            for fresh_range in self._fresh_ingredient_ranges:
                for merged_fresh_range in merged_fresh_ingredient_ranges:
                    if (fresh_range[0] in range(merged_fresh_range[0], merged_fresh_range[1] + 1) 
                        or fresh_range[1] in range(merged_fresh_range[0], merged_fresh_range[1] + 1)
                        or merged_fresh_range[0] in range(fresh_range[0], fresh_range[1] + 1)
                        or merged_fresh_range[1] in range(fresh_range[0], fresh_range[1] + 1)):
                        new_fresh_range_start = min(fresh_range[0], merged_fresh_range[0])
                        new_fresh_range_end = max(fresh_range[1], merged_fresh_range[1])
                        new_fresh_range = (new_fresh_range_start, new_fresh_range_end)
                        merged_fresh_ingredient_ranges.append(new_fresh_range)
                        merged_fresh_ingredient_ranges.remove(merged_fresh_range)
                        should_merge = True
                        break
                else:
                    merged_fresh_ingredient_ranges.append(fresh_range)

            self._fresh_ingredient_ranges = merged_fresh_ingredient_ranges

    def _count_ingredients_in_all_fresh_ranges(self) -> int:
        return sum([len(range(fresh_range[0], fresh_range[1] + 1)) for fresh_range in self._fresh_ingredient_ranges])
