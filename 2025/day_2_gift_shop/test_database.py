from pytest import fixture

from database import Database


@fixture
def database():
    db = Database()
    db.load('test_input.raw')
    return db


def test_find_invalid_product_ids(database: Database):
    invalid_product_ids = database.find_invalid_product_ids()
    assert sum(invalid_product_ids) == 1227775554


def test_find_invalid_product_ids_with_extended_search(database: Database):
    invalid_product_ids = database.find_invalid_product_ids(advanced_search=True)
    assert sum(invalid_product_ids) == 4174379265
