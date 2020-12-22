from pytest import mark

from passport_processing import _is_byr_valid, _is_iyr_valid, _is_eyr_valid, _is_hgt_valid


@mark.parametrize('passport', [{},
                               {'byr': 1919},
                               {'byr': 2003}])
def test_is_byr_valid_returns_false(passport):
    assert _is_byr_valid(passport) is False


@mark.parametrize('passport', [{'byr': 1920},
                               {'byr': 2002}])
def test_is_byr_valid_returns_true(passport):
    assert _is_byr_valid(passport) is True


@mark.parametrize('passport', [{},
                               {'iyr': 2009},
                               {'iyr': 2021}])
def test_is_iyr_valid_returns_false(passport):
    assert _is_iyr_valid(passport) is False


@mark.parametrize('passport', [{'iyr': 2010},
                               {'iyr': 2020}])
def test_is_iyr_valid_returns_true(passport):
    assert _is_iyr_valid(passport) is True


@mark.parametrize('passport', [{},
                               {'eyr': 2019},
                               {'eyr': 2031}])
def test_is_eyr_valid_returns_false(passport):
    assert _is_eyr_valid(passport) is False


@mark.parametrize('passport', [{'eyr': 2020},
                               {'eyr': 2030}])
def test_is_eyr_valid_returns_true(passport):
    assert _is_eyr_valid(passport) is True


@mark.parametrize('passport', [{},
                               {'hgt': ''},
                               {'hgt': '132'},
                               {'hgt': '149cm'},
                               {'hgt': '194cm'},
                               {'hgt': '58in'},
                               {'hgt': '77in'}])
def test_is_hgt_valid_returns_false(passport):
    assert _is_hgt_valid(passport) is False


@mark.parametrize('passport', [{'hgt': '150cm'},
                               {'hgt': '193cm'},
                               {'hgt': '59in'},
                               {'hgt': '76in'}])
def test_is_hgt_valid_returns_true(passport):
    assert _is_hgt_valid(passport) is True
