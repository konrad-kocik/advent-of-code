class Database:
    def __init__(self):
        self._product_ids: list[int] = []

    def load(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for product_id_range in input_file.read().split(','):
                product_id_range_start, product_id_range_end = product_id_range.split('-')
                for product_id in range(int(product_id_range_start), int(product_id_range_end) + 1):
                    self._product_ids.append(product_id)

    def find_invalid_product_ids(self, advanced_search: bool = False) -> list[int]:
        invalid_product_ids = []

        for product_id in self._product_ids:
            if advanced_search:
                if self._check_if_invalid_using_advanced_mode(str(product_id)):
                    invalid_product_ids.append(product_id)
            else:
                if self._check_if_invalid_using_basic_mode(str(product_id)):
                    invalid_product_ids.append(product_id)                                    

        return invalid_product_ids        

    def _check_if_invalid_using_advanced_mode(self, product_id: str) -> bool:
        for split_length in range(1, len(product_id)):
            if len(product_id) % split_length == 0:
                product_id_to_split = product_id[:]
                product_id_parts = set()

                for _ in range(len(product_id) // split_length):
                    product_id_parts.add(product_id_to_split[:split_length])
                    product_id_to_split = product_id_to_split[split_length:]

                if len(product_id_parts) == 1:
                    return True
        return False

    def _check_if_invalid_using_basic_mode(self, product_id: str) -> bool:
        if len(product_id) % 2 == 0:
                    product_id_head = product_id[:len(product_id) // 2]
                    product_id_tail = product_id[len(product_id) // 2:]

                    if product_id_head == product_id_tail:
                        return True
        return False
