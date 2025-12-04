from collections import defaultdict


class NuclearReactor:
    def __init__(self):
        self._medicine: str = ''
        self._fission_replacements: dict[str, list[str]] = defaultdict(list)
        self._fusion_replacements: dict[str, str] = dict()

    def load_medicine_recipe(self, input_file_path: str):
        with open(input_file_path) as input_file:
            lines = input_file.readlines()
            self._medicine = lines[-1].strip()

            for line in lines[:-2]:
                source_atom, target_atom = line.strip().split(' => ')
                self._fission_replacements[source_atom].append(target_atom)
                self._fusion_replacements[target_atom] = source_atom

    def calibrate(self) -> int:
        fissioned_molecules = self._fission(self._medicine)
        return len(fissioned_molecules)

    def calculate_fewest_steps_to_create_medicine(self) -> int:
        return self._fusion(molecule=self._medicine, steps=0, fewest_steps=0)

    def _fission(self, molecule: str) -> set[str]:
        fissioned_molecules: set[str] = set()
        i = 0

        while i < len(molecule):
            char = molecule[i]
            next_char = molecule[i + 1] if i < len(molecule) - 2 else ''
            atom = char + next_char if next_char and next_char.islower() else char
            molecule_head = molecule[:i]
            molecule_tail = molecule[i + 2:] if next_char and next_char.islower() else molecule[i + 1:]

            for atom_replacement in self._fission_replacements[atom]:
                fissioned_molecule = molecule_head + atom_replacement + molecule_tail
                fissioned_molecules.add(fissioned_molecule)

            i += 2 if next_char and next_char.islower() else 1

        return fissioned_molecules

    def _fusion(self, molecule: str, steps: int, fewest_steps: int) -> int:
        i = 0
        submolecule = ''

        while i < len(molecule):
            submolecule += molecule[i]

            if i < len(molecule) - 1 and molecule[i].isupper() and molecule[i + 1].islower():
                i += 1
                continue

            # self._show_molecule(molecule, i, submolecule)
            replacement_possible = any([molecule.startswith(submolecule) for molecule in self._fusion_replacements.keys()])

            if replacement_possible:
                replacement = self._fusion_replacements.get(submolecule)

                if replacement:
                    molecule_head = molecule[:i - len(submolecule) + 1]
                    molecule_tail = molecule[i + 1:]

                    if replacement == 'e' and not molecule_head and not molecule_tail:
                        steps += 1
                        # self._show_molecule(molecule, i, submolecule, replacement)
                        self._show_steps(steps, fewest_steps)
                        return steps if steps < fewest_steps or fewest_steps == 0 else fewest_steps
                    elif replacement == 'e' and (molecule_head or molecule_tail) and i < len(molecule) - 1:
                        next_replacement_possible = any([replacement.startswith(submolecule + molecule[i + 1]) for replacement in self._fusion_replacements.keys()])
                        
                        if next_replacement_possible:
                            i += 1
                        else:
                            if i == len(molecule) - 1:
                                i += 1
                            else:
                                # set i to the second to first atom in submolecule
                                i = i - len(submolecule) + (2 if molecule[i - len(submolecule) + 2].isupper() else 3)
                            submolecule = ''
                    else:
                        steps += 1
                        new_molecule = molecule_head + replacement + molecule_tail
                        # self._show_molecule(molecule, i, submolecule, replacement)
                        fewest_steps = self._fusion(new_molecule, steps, fewest_steps)
                        i += 1
                else:
                    i += 1
            else:
                if i == len(molecule) - 1:
                    i += 1
                else:
                    # set i to the second to first atom in submolecule
                    i = i - len(submolecule) + (2 if molecule[i - len(submolecule) + 2].isupper() else 3)
                submolecule = ''

        return fewest_steps

    def _show_molecule(self, molecule: str, i: int, sub_molecule: str, replacement: str = ''):
        # from time import sleep; sleep(0.5)
        molecule_head = molecule[:i - len(sub_molecule) + 1]
        molecule_tail = molecule[i + 1:]
        color = '92' if replacement else '91'
        print(f'{molecule_head}\033[{color}m{replacement if replacement else sub_molecule}\033[0m{molecule_tail}')

    def _show_steps(self, steps: int, fewest_steps: int):
        print(f'\nSTEPS: {steps}')
        print(f'FEWEST STEPS: {steps if steps < fewest_steps or fewest_steps == 0 else fewest_steps}\n')