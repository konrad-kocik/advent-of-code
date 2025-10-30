from pytest import mark

from crypto_miner import find_hash_producing_number


@mark.parametrize('input_file_path, expected_number', [('test_input_1.raw', 609043),
                                                       ('test_input_2.raw', 1048970)])
def test_get_md5_hash(input_file_path, expected_number):
    assert find_hash_producing_number(input_file_path, leading_zeros=5) == expected_number
