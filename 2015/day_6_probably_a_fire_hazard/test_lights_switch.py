from lights_switch import LightsSwitch


def test_lights_switch():
    lights_switch = LightsSwitch()
    lights_switch.load_instructions('test_input.raw')
    lights_switch.execute_instructions()
    assert lights_switch.lit_lights_count == 998996
