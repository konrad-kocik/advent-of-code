from lights_switch import LightsSwitch


def test_lights_switch():
    lights_switch = LightsSwitch()
    lights_switch.load_instructions('test_input_1.raw')
    lights_switch.execute_instructions()
    assert lights_switch.lit_lights_count == 998996


def test_lights_switch_with_dimmer():
    lights_switch = LightsSwitch()
    lights_switch.load_instructions('test_input_2.raw')
    lights_switch.execute_instructions(dimmer=True)
    assert lights_switch.total_brightness == 2000001
