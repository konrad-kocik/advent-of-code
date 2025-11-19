from collections import defaultdict


class NuclearReactor:
    def __init__(self):
        self._molecule: str = ''
        self._replacements: dict[str, list[str]] = defaultdict(list)
        self._output: set[str] = set()

    @property
    def output(self) -> set[str]:
        return self._output

    def load_molecule(self, input_file_path: str):
        with open(input_file_path) as input_file:
            lines = input_file.readlines()
            self._molecule = lines[-1].strip()

            for line in lines[:-2]:
                source_atom, result_atom = line.strip().split(' => ')
                self._replacements[source_atom].append(result_atom)

    def fuse(self):
        i = 0

        while i < len(self._molecule):
            char = self._molecule[i]
            next_char = self._molecule[i + 1] if i < len(self._molecule) - 2 else ''
            atom = char + next_char if next_char and next_char.islower() else char
            molecule_head = self._molecule[:i]
            molecule_tail = self._molecule[i + 2:] if next_char and next_char.islower() else self._molecule[i + 1:]

            for atom_replacement in self._replacements[atom]:
                fused_molecule = molecule_head + atom_replacement + molecule_tail
                self._output.add(fused_molecule)

            i += 2 if next_char and next_char.islower() else 1
