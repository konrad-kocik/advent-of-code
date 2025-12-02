class Database:
    def __init__(self):
        self._product_ids: list[int] = []

    def load(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for product_id_range in input_file.read().split(','):
                product_id_range_start, product_id_range_end = product_id_range.split('-')
                for product_id in range(int(product_id_range_start), int(product_id_range_end) + 1):
                    self._product_ids.append(product_id)

    def find_invalid_product_ids(self) -> list[int]:
        invalid_product_ids = []

        for product_id in self._product_ids:
            product_id = str(product_id)

            if len(product_id) % 2 == 0:
                product_id_head = product_id[:len(product_id) // 2]
                product_id_tail = product_id[len(product_id) // 2:]

                if product_id_head == product_id_tail:
                    invalid_product_ids.append(int(product_id))

        return invalid_product_ids        
