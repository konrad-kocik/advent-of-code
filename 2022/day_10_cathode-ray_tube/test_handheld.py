from handheld import calculate_sum_of_signal_strengths, render_image


def test_calculate_sum_of_signal_strengths():
    cycles = [20, 60, 100, 140, 180, 220]
    assert calculate_sum_of_signal_strengths('test_input.raw', cycles) == 13140


def test_render_image():
    assert render_image('test_input.raw') == ['##..##..##..##..##..##..##..##..##..##..',
                                              '###...###...###...###...###...###...###.',
                                              '####....####....####....####....####....',
                                              '#####.....#####.....#####.....#####.....',
                                              '######......######......######......####',
                                              '#######.......#######.......#######.....']
