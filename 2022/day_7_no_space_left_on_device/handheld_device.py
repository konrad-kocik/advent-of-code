def get_total_size_of_small_dirs(file_path):
    terminal_output = _get_terminal_output(file_path)
    file_system = _build_file_system(terminal_output)
    small_dirs = _get_dirs_with_size_below(100000, file_system)
    total_size_of_dirs = _get_total_size_of_dirs(small_dirs)
    return total_size_of_dirs


def get_total_size_of_smallest_dir_to_delete(file_path):
    terminal_output = _get_terminal_output(file_path)
    file_system = _build_file_system(terminal_output)
    missing_free_space = _calculate_missing_free_space_for_update(file_system)
    big_dirs = _get_dirs_with_size_above(missing_free_space, file_system)
    total_size_of_smallest_dir = _get_total_size_of_smallest_dir(big_dirs)
    return total_size_of_smallest_dir


def _get_terminal_output(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def _build_file_system(terminal_output):
    root_dir = Dir(name='/', parent=None)
    current_dir = root_dir

    for line in terminal_output:
        if line.startswith('$'):
            current_dir = _execute_command(line, current_dir)
        else:
            _update_file_system(line, current_dir)

    return root_dir


def _execute_command(command, current_dir):
    if command.startswith('$ cd'):
        target_dir = command.split(' ')[2]

        if target_dir == '/':
            return current_dir.root_dir
        elif target_dir == '..':
            return current_dir.parent
        else:
            return current_dir.get_child_dir(target_dir)

    return current_dir


def _update_file_system(line, current_dir):
    if line.startswith('dir'):
        current_dir.add_child_dir(name=line.split(' ')[1])
    else:
        file_size, file_name = line.split(' ')
        current_dir.add_file(name=file_name, size=int(file_size))


def _get_dirs_with_size_below(max_size, file_system):
    return file_system.get_child_dirs_with_size_below(max_size)


def _get_dirs_with_size_above(min_size, file_system):
    return file_system.get_child_dirs_with_size_above(min_size)


def _get_total_size_of_dirs(dirs):
    return sum([dir.total_size for dir in dirs])


def _get_total_size_of_smallest_dir(dirs):
    return min([dir.total_size for dir in dirs])


def _calculate_missing_free_space_for_update(file_system):
    disk_space = 70000000
    free_space = disk_space - file_system.total_size
    update_size = 30000000
    return update_size - free_space


class Dir:
    def __init__(self, name, parent):
        self._name = name
        self._parent = parent
        self._children = []
        self._files = []

    @property
    def name(self):
        return self._name

    @property
    def parent(self):
        return self._parent

    @property
    def root_dir(self):
        return self if self._parent is None else self.root_dir

    @property
    def total_size(self):
        files_total_size = sum([file.size for file in self._files])
        children_total_size = sum([child.total_size for child in self._children])
        return files_total_size + children_total_size

    def add_child_dir(self, name):
        self._children.append(Dir(name, self))

    def add_file(self, name, size):
        self._files.append(File(name, size))

    def get_child_dir(self, name):
        for child in self._children:
            if child.name == name:
                return child

    def get_child_dirs_with_size_below(self, size):
        matching_dirs = []

        for child in self._children:
            if child.total_size <= size:
                matching_dirs.append(child)

            matching_dirs.extend(child.get_child_dirs_with_size_below(size))

        return matching_dirs

    def get_child_dirs_with_size_above(self, size):
        matching_dirs = []

        for child in self._children:
            if child.total_size >= size:
                matching_dirs.append(child)

            matching_dirs.extend(child.get_child_dirs_with_size_above(size))

        return matching_dirs


class File:
    def __init__(self, name, size):
        self._name = name
        self._size = size

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size
