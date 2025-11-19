from lights_switch import LightsSwitch

print('Solving first part of puzzle')
lights_switch = LightsSwitch()
lights_switch.configure('input.raw')
lights_switch.animate(steps=100)
print(f'Answer to first part of puzzle is: {lights_switch.lit_lights_count}')

print('Solving second part of puzzle')
lights_switch = LightsSwitch()
lights_switch.configure('input.raw')
lights_switch.animate(steps=100, corner_lights_stuck=True)
print(f'Answer to second part of puzzle is: {lights_switch.lit_lights_count}')
