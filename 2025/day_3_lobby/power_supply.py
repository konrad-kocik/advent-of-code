class PowerSupply:
    def __init__(self):
        self._banks: list[list[int]] = []
        self._safety = True

    def configure_batteries(self, input_file_path: str):
        with open(input_file_path) as input_file:
            for line in input_file:
                bank = [int(battery) for battery in line.strip()]
                self._banks.append(bank)

    def override_safety(self):
        self._safety = False

    def calculate_total_output_joltage(self) -> int:
        total_output_joltage = 0

        for bank in self._banks:
            if self._safety:
                total_output_joltage += self._calculate_bank_output_joltage_with_safety(bank)
            else:
                total_output_joltage += self._calculate_bank_output_joltage_without_safety(bank)

        return total_output_joltage

    def _calculate_bank_output_joltage_with_safety(self, bank: list[int]) -> int:
        bank_output_joltage = 0

        for first_battery_id, first_battery in enumerate(bank):
            for second_battery in bank[first_battery_id + 1:]:
                batteries_joltage =  int(f'{first_battery}{second_battery}')
                bank_output_joltage = batteries_joltage if batteries_joltage > bank_output_joltage else bank_output_joltage

        return bank_output_joltage

    def _calculate_bank_output_joltage_without_safety(self, bank: list[int]) -> int:
        selected_batteries = []
        batteries_left = bank[:]
        missing_batteries_count = 12

        while missing_batteries_count > 0:
            battery = batteries_left.pop(0)
            last_battery_id_to_check = (missing_batteries_count - 1) * -1
            batteries_to_check = batteries_left[:last_battery_id_to_check] if last_battery_id_to_check < 0 else batteries_left

            if not batteries_to_check or battery >= max(batteries_to_check):
                selected_batteries.append(battery)
            
            missing_batteries_count = 12 - len(selected_batteries)

        return int(''.join([str(battery) for battery in selected_batteries]))
