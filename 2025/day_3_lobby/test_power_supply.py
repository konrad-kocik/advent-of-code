from power_supply import PowerSupply


def test_total_output_joltage():
    power_supply = PowerSupply()
    power_supply.configure_batteries('test_input.raw')
    assert power_supply.total_output_joltage == 357
