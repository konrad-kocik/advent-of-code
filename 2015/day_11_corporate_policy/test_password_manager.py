from pytest import mark
from password_manager import change_password, _has_increasing_straight


@mark.parametrize('old_password, new_password', [('abcdefgh', 'abcdffaa'),
                                                 ('ghijklmn', 'ghjaabcc')])
def test_change_password(old_password, new_password):
    assert change_password(old_password) == new_password
