from pytest import mark
from look_and_say import play



@mark.parametrize('sequence, result', [('1', '11'),
                                       ('11', '21'),
                                       ('21', '1211'),
                                       ('1211', '111221'),
                                       ('111221', '312211')])
def test_play(sequence, result):
    assert play(sequence, repeat=1) == result
