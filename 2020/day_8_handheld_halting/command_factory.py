from command import Acc, Jmp, Nop


def create_command(name, arg):
    if name == 'acc':
        return Acc(arg)

    if name == 'jmp':
        return Jmp(arg)

    if name == 'nop':
        return Nop(arg)


def transform_command(cmd):
    cmd_type = type(cmd)

    if cmd_type == Acc:
        return None

    if cmd_type == Jmp:
        return Nop(cmd.arg)

    if cmd_type == Nop:
        return Jmp(cmd.arg)
