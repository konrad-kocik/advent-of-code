def move_crates(file_path):
    stacks, procedure = _read_manual(file_path)
    stacks = _rearrange_stacks(stacks, procedure)
    top_crates = _get_top_crates(stacks)
    return top_crates


def move_crates_with_cm9001(file_path):
    stacks, procedure = _read_manual(file_path)
    stacks = _rearrange_stacks_with_cm9001(stacks, procedure)
    top_crates = _get_top_crates(stacks)
    return top_crates


def _read_manual(file_path):
    stacks = {}
    procedure = []
    file_section = 'stacks'

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == '':
                file_section = 'procedure'
                continue

            if file_section == 'stacks':
                _handle_stack_line(line, stacks)

            if file_section == 'procedure':
                _handle_procedure_line(line, procedure)

    return stacks, procedure


def _handle_stack_line(line, stacks):
    line = line[:-1].replace('[', '').replace(']', '')

    if line.startswith(' 1'):
        return

    stack_id = 1

    while line:
        if line[0] != ' ':
            if stack_id in stacks:
                stacks[stack_id].append(line[0])
            else:
                stacks[stack_id] = [line[0]]
            line = line[2:]
        else:
            line = line[4:]

        stack_id += 1


def _handle_procedure_line(line, procedure):
    procedure.append([int(line_part) for line_part in line.strip().split(' ') if line_part.isdigit()])


def _rearrange_stacks(stacks, procedure):
    for step in procedure:
        repetitions, source_stack_id, target_stack_id = step

        for _ in range(repetitions):
            stacks[target_stack_id].insert(0, stacks[source_stack_id].pop(0))

    return stacks


def _rearrange_stacks_with_cm9001(stacks, procedure):
    for step in procedure:
        crates_count, source_stack_id, target_stack_id = step

        for crate in stacks[source_stack_id][0:crates_count][::-1]:
            stacks[target_stack_id].insert(0, crate)

        stacks[source_stack_id] = stacks[source_stack_id][crates_count:]

    return stacks


def _get_top_crates(stacks):
    return ''.join(stacks[stack_id][0] for stack_id in sorted(stacks.keys()))
