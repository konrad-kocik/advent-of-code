class Command:
    def __init__(self, arg):
        self._arg = arg
        self._executed = False

    def __repr__(self):
        return '{} {}'.format(self.__class__.__name__.lower(), self._arg)

    @property
    def arg(self):
        return self._arg

    @property
    def executed(self):
        return self._executed

    def execute(self):
        self._executed = True
        return self._execute()


class Acc(Command):
    def _execute(self):
        return self._arg, 1


class Jmp(Command):
    def _execute(self):
        return 0, self._arg


class Nop(Command):
    def _execute(self):
        return 0, 1
