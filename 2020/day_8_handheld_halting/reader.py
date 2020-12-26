from command_factory import create_command


def get_program(input_file):
    commands = []

    with open(input_file, 'r') as file:
        for line in file:
            cmd_name, cmd_arg = line.strip().split(' ')
            cmd_arg = int(cmd_arg) if cmd_arg.startswith('-') else int(cmd_arg[1:])
            commands.append(create_command(cmd_name, cmd_arg))

    return commands
