class InventoryManagementSystem:
    def __init__(self):
        self._fresh_ingredient_ranges: list[range] = []
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
                    self._fresh_ingredient_ranges.append(range(int(range_start), 
                                                               int(range_end) + 1))
                    
                if section == 'ingredients':
                    self._ingredients.append(int(line))

    def count_fresh_ingredients(self) -> int:
        fresh_ingredients_count = 0
    
        for ingredient in self._ingredients:
            if any([ingredient in fresh_range for fresh_range in self._fresh_ingredient_ranges]):
                fresh_ingredients_count += 1

        return fresh_ingredients_count
