def find_weakness(file_path, preamble_size=25):
    data = _get_encrypted_data(file_path)
    seed = _find_seed(data, preamble_size)
    seed_parts = _find_seed_parts(seed, data)
    return min(seed_parts) + max(seed_parts)


def _get_encrypted_data(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]


def _find_seed(data, preamble_size):
    for start_id in range(len(data) - preamble_size):
        numbers = data[start_id:start_id + preamble_size + 1]
        number = numbers.pop()

        if not _can_be_summed_up(number, numbers):
            return number


def _can_be_summed_up(number, numbers):
    for i in numbers:
        for j in numbers:
            if i + j == number and i != j:
                return True
    return False


def _find_seed_parts(seed, numbers):
    for number_id, number in enumerate(numbers):
        parts_sum = number
        next_number_id = number_id + 1

        while parts_sum < seed:
            parts_sum += numbers[next_number_id]
            next_number_id += 1

        if parts_sum == seed:
            return numbers[number_id:next_number_id]
