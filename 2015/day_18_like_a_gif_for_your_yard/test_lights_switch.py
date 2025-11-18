from lights_switch import LightsSwitch


def test_lights_switch():
    lights_switch = LightsSwitch()
    lights_switch.configure('test_input.raw')
    lights_switch.animate(steps=4)
    assert lights_switch.lit_lights_count == 4
