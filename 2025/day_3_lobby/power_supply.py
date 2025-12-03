class PowerSupply:
    def __init__(self):
        self._banks: list[list[int]] = []

    @property
    def total_output_joltage(self) -> int:
        total_output_joltage = 0

        for bank in self._banks:
            bank_output_joltage = 0

            for first_battery_id, first_battery in enumerate(bank):
                for second_battery in bank[first_battery_id + 1:]:
                    batteries_joltage =  int(f'{first_battery}{second_battery}')
                    bank_output_joltage = batteries_joltage if batteries_joltage > bank_output_joltage else bank_output_joltage

            total_output_joltage += bank_output_joltage

        return total_output_joltage

    def configure_batteries(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for line in input_file:
                bank = [int(battery) for battery in line.strip()]
                self._banks.append(bank)
