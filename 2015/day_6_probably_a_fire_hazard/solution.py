from lights_switch import LightsSwitch

print('\nSolving first part of puzzle')
lights_switch = LightsSwitch()
lights_switch.load_instructions('input.raw')
lights_switch.execute_instructions()
print(f'Answer to first part of puzzle is: {lights_switch.lit_lights_count}')

print('\nSolving second part of puzzle')
lights_switch = LightsSwitch()
lights_switch.load_instructions('input.raw')
lights_switch.execute_instructions(dimmer=True)
print(f'Answer to first part of puzzle is: {lights_switch.total_brightness}')
