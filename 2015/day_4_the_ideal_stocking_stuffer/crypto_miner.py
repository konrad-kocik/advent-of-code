from hashlib import md5


def find_hash_producing_number(input_file_path: str, leading_zeros: int) -> int:
    secret_key = _get_secret_key(input_file_path)
    return _find_lowest_number_producing_md5_hash(secret_key, leading_zeros)


def _get_secret_key(input_file_path: str) -> str:
    with open(input_file_path, 'r') as input_file:
        return input_file.read().strip()


def _find_lowest_number_producing_md5_hash(secret_key: str, leading_zeros: int) -> int:
    number = 0

    while True:
        hash_input = f'{secret_key}{number}'.encode()
        hash_output = md5(hash_input).hexdigest()

        if hash_output.startswith(''.zfill(leading_zeros)):
            return number

        number += 1
