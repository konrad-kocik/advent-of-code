from dataclasses import dataclass


@dataclass
class Person:
    id: int
    characteristics: dict[str, int]


def match_person(input_evidence_file_path: str, input_persons_file_path: str, retroencabulator_correction: bool = False) -> int | None:
    forensic_data = _analyze_evidence(input_evidence_file_path)
    persons = _get_persons(input_persons_file_path)
    person_id = _match(forensic_data, persons, retroencabulator_correction)
    return person_id


def _get_persons(input_file_path: str) -> list[Person]:
    persons = []

    with open(input_file_path) as input_file:
        for line in input_file:
            name, characteristics = line.split(': ', 1)
            person_id = int(name.split()[1])
            characteristics = {param: int(value) for param, value in (characteristic.split(': ') for characteristic in characteristics.split(', '))}
            persons.append(Person(person_id, characteristics))

    return persons


def _analyze_evidence(input_file_path: str) -> dict[str, int]:
    with open(input_file_path) as input_file:
        return {param: int(value) for param, value in (line.split(': ') for line in input_file)}


def _match(forensic_data: dict[str, int], persons: list[Person], retroencabulator_correction: bool) -> int | None:
    for person in persons:
        characteristics_matched = []

        for param, value in person.characteristics.items():
            if retroencabulator_correction and param in ('cats', 'trees'):
                characteristics_matched.append(forensic_data[param] < value)
            elif retroencabulator_correction and param in ('pomeranians', 'goldfish'):
                characteristics_matched.append(forensic_data[param] > value)
            else:
                characteristics_matched.append(forensic_data[param] == value)

        if all(characteristics_matched):
            return person.id
        
    return None
