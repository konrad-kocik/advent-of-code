from pytest import mark

from garden import calculate_total_price_of_fence


@mark.parametrize('input_file_path, price', [('test_input_1.raw', 140),
                                             ('test_input_2.raw', 772),
                                             ('test_input_3.raw', 1930)])
def test_calculate_total_price_of_fence(input_file_path, price):
    assert calculate_total_price_of_fence(input_file_path) == price


@mark.parametrize('input_file_path, price', [('test_input_1.raw', 80),
                                             ('test_input_2.raw', 436),
                                             ('test_input_3.raw', 1206),
                                             ('test_input_4.raw', 236),
                                             ('test_input_5.raw', 368)])
def test_calculate_total_price_of_fence_with_bulk_discount(input_file_path, price):
    assert calculate_total_price_of_fence(input_file_path, bulk_discount=True) == price
