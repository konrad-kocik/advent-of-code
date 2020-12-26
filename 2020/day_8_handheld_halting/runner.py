def run_program(program):
    acc = 0
    next_cmd_id = 0

    while True:
        if next_cmd_id >= len(program):
            break

        cmd = program[next_cmd_id]

        if cmd.executed:
            break

        acc_inc, cmd_id_offset = cmd.execute()
        acc += acc_inc
        next_cmd_id += cmd_id_offset

    return acc, next_cmd_id
