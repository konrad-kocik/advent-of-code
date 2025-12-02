from database import Database


def test_find_invalid_product_ids():
    database = Database()
    database.load('test_input.raw')
    invalid_product_ids = database.find_invalid_product_ids()
    assert sum(invalid_product_ids) == 1227775554
