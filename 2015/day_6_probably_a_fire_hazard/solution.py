from lights_switch import LightsSwitch

print('\nSolving first part of puzzle')
lights_switch = LightsSwitch()
lights_switch.load_instructions('input.raw')
lights_switch.execute_instructions()
lights_switch.show_grid()
print(f'Answer to first part of puzzle is: {lights_switch.lit_lights_count}')
