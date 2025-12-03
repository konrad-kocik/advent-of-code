from pytest import fixture

from power_supply import PowerSupply


@fixture
def power_supply():
    ps = PowerSupply()
    ps.configure_batteries('test_input.raw')
    return ps


def test_calculate_total_output_joltage(power_supply: PowerSupply):
    assert power_supply.calculate_total_output_joltage() == 357


def test_calculate_total_output_joltage_with_safety_override(power_supply: PowerSupply):
    power_supply.override_safety()
    assert power_supply.calculate_total_output_joltage() == 3121910778619
