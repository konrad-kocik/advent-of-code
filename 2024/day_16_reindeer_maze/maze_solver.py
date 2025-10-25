from typing import List, Tuple, Optional, Any
from dataclasses import dataclass
from random import shuffle

Map = List[List['Field']]
Coords = Tuple[int, int]
Vector = Tuple[int, int]
MovementData = Tuple['Field', Vector]


class FieldContent:
    REINDEER_FACING_UP = '^'
    REINDEER_FACING_DOWN = 'v'
    REINDEER_FACING_LEFT = '<'
    REINDEER_FACING_RIGHT = '>'
    WALL = '#'
    EMPTY = '.'
    START = 'S'
    END = 'E'


class Vectors:
    UP: Vector = (0, -1)
    RIGHT: Vector = (1, 0)
    DOWN: Vector = (0, 1)
    LEFT: Vector = (-1, 0)
    ALL: List[Vector] = [UP, RIGHT, DOWN, LEFT]


class Field:
    def __init__(self, x: int, y: int, content: str):
        self._x = x
        self._y = y
        self._content: str = content
        self._prio: Optional[int] = None
        self._visited = False
        self._on_path = False

    def __str__(self):
        return f'{self.coords}'

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def coords(self) -> Coords:
        return self._x, self._y

    @property
    def content(self) -> str:
        return self._content

    @property
    def prio(self) -> Optional[int]:
        return self._prio

    @prio.setter
    def prio(self, prio: int):
        self._prio = prio

    @property
    def visited(self) -> bool:
        return self._visited

    @property
    def on_path(self) -> bool:
        return self._on_path

    def show(self):
        if self._on_path:
            color = '92'  # green
        elif self._visited:
            color = '91'  # red
        elif self._content == FieldContent.WALL:
            color = ''  # default
        else:
            color = '93'  # yellow

        print(f'\033[{color}m{self._content}\033[0m', end='')

    def insert(self, reindeer: str):
        self._content = reindeer
        self._visited = True
        self._on_path = True

    def rotate(self, new_direction: str):
        self._content = new_direction

    def clear(self, undoing: bool):
        self._content = FieldContent.EMPTY
        self._on_path = not undoing


class ActionNames:
    MOVEMENT = 'movement'
    ROTATION = 'rotation'


class Maze:
    def __init__(self):
        self._map: Map = []

    def load(self, input_file_path: str):
        with open(input_file_path, 'r') as file:
            for y, line in enumerate(file):
                row = []
                line = line.strip()
                for x, char in enumerate(line):
                    row.append(Field(x, y, char))
                self._map.append(row)

        end_field = self.find_field(FieldContent.END)

        for row in self._map:
            for field in row:
                field.prio = self._calculate_prio(end_field, field)

    def show(self,):
        print()

        for row in self._map:
            for field in row:
                field.show()
            print()

    def find_reindeer_field(self) -> Optional[Field]:
        return (self.find_field(FieldContent.REINDEER_FACING_UP)
                or self.find_field(FieldContent.REINDEER_FACING_DOWN)
                or self.find_field(FieldContent.REINDEER_FACING_LEFT)
                or self.find_field(FieldContent.REINDEER_FACING_RIGHT))

    def find_field(self, field_content: str) -> Optional[Field]:
        for row in self._map:
            for field in row:
                if field.content == field_content:
                    return field
        return None

    def get_field(self, x: int, y: int) -> Optional[Field]:
        try:
            return self._map[y][x]
        except IndexError:
            return None

    @staticmethod
    def _calculate_prio(end_field: Field, field: Field) -> int:
        return abs(end_field.x - field.x) + abs(end_field.y - field.y)


@dataclass
class Action:
    name: str
    start_state: Any
    end_state: Any


@dataclass
class Solution:
    id: int
    score: int
    maze: Maze
    actions: List[Action]


class MazeSolver:
    def __init__(self, input_file_path: str, log_level: str = 'info'):
        self._input_file_path = input_file_path
        self._log_level: str = log_level
        self._maze: Maze = Maze()
        self._actions: List[Action] = []
        self._solutions: List[Solution] = []

    def score_best_solution(self, number_of_solutions: int = 1):
        for solution_id in range(1, number_of_solutions + 1):
            print('\n=================') if self._log_level in ('debug', 'trace') else None
            print(f'\nSOLUTION: #{solution_id}') if self._log_level in ('debug', 'trace') else None
            self._load_maze()
            self._solve_maze()
            self._register_solution(solution_id)
            print(f'\nSCORE: {self._score_actions()}') if self._log_level in ('debug', 'trace') else None

        best_solution = self._find_best_solution()
        print('\n=================')
        print(f'\nBEST SOLUTION: #{best_solution.id}')
        best_solution.maze.show()
        print(f'\nSCORE: {best_solution.score}')

        return best_solution.score

    def _load_maze(self):
        self._maze = Maze()
        self._maze.load(self._input_file_path)

    def _solve_maze(self):
        self._actions = []
        self._put_reindeer_on_start()
        end_field = self._maze.find_field(FieldContent.END)

        while self._maze.find_reindeer_field().coords != end_field.coords:
            reindeer_field = self._maze.find_reindeer_field()

            if movement_data := self._find_on_course_not_visited_unique_field(reindeer_field):
                target_field, vector = movement_data
                self._move_reindeer(reindeer_field, target_field)
            # elif movement_data := self._find_not_visited_unique_field(reindeer_field):
            #     target_field, vector = movement_data
            #     self._rotate_reindeer(reindeer_field, vector)
            #     self._move_reindeer(reindeer_field, target_field)
            elif movement_data := self._find_best_prio_not_visited_unique_field(reindeer_field):
                target_field, vector = movement_data
                self._rotate_reindeer(reindeer_field, vector)
                self._move_reindeer(reindeer_field, target_field)
            # elif movement_data := self._find_best_prio_not_visited_field(reindeer_field):
            #     target_field, vector = movement_data
            #     self._rotate_reindeer(reindeer_field, vector)
            #     self._move_reindeer(reindeer_field, target_field)
            elif movement_data := self._find_random_not_visited_field(reindeer_field):
                target_field, vector = movement_data
                self._rotate_reindeer(reindeer_field, vector)
                self._move_reindeer(reindeer_field, target_field)
            else:
                self._undo_last_action()

        self._maze.show() if self._log_level in ('debug', 'trace') else None

    def _put_reindeer_on_start(self):
        if start_field := self._maze.find_field(FieldContent.START):
            start_field.insert(FieldContent.REINDEER_FACING_RIGHT)
            self._maze.show() if self._log_level == 'trace' else None

    def _find_on_course_not_visited_unique_field(self, reindeer_field: Field) -> Optional[MovementData]:
        vectors_for_directions = {FieldContent.REINDEER_FACING_UP: Vectors.UP,
                                  FieldContent.REINDEER_FACING_RIGHT: Vectors.RIGHT,
                                  FieldContent.REINDEER_FACING_DOWN: Vectors.DOWN,
                                  FieldContent.REINDEER_FACING_LEFT: Vectors.LEFT}
        vector = vectors_for_directions[reindeer_field.content]
        field = self._maze.get_field(reindeer_field.x + vector[0], reindeer_field.y + vector[1])

        if field and field.content != FieldContent.WALL and not field.visited and not self._is_field_on_path_in_previous_solutions(field):
            return field, vector
        else:
            return None

    def _find_not_visited_unique_field(self, reindeer_field: Field) -> Optional[MovementData]:
        for vector in Vectors.ALL:
            field = self._maze.get_field(reindeer_field.x + vector[0], reindeer_field.y + vector[1])
            if field and field.content != FieldContent.WALL and not field.visited and not self._is_field_on_path_in_previous_solutions(field):
                return field, vector
        return None

    def _find_random_not_visited_field(self, reindeer_field: Field) -> Optional[MovementData]:
        vectors = Vectors.ALL.copy()
        shuffle(vectors)

        for vector in vectors:
            field = self._maze.get_field(reindeer_field.x + vector[0], reindeer_field.y + vector[1])
            if field and field.content != FieldContent.WALL and not field.visited:
                return field, vector
        return None

    def _find_best_prio_not_visited_unique_field(self, reindeer_field: Field) -> Optional[MovementData]:
        vectors_to_fields = {}

        for vector in Vectors.ALL:
            field = self._maze.get_field(reindeer_field.x + vector[0], reindeer_field.y + vector[1])
            if field and field.content != FieldContent.WALL and not field.visited and not self._is_field_on_path_in_previous_solutions(field):
                vectors_to_fields[vector] = field

        best_movement_data = tuple()

        for vector, field in vectors_to_fields.items():
            if not best_movement_data or field.prio < best_movement_data[0].prio:
                best_movement_data = field, vector

        return best_movement_data

    def _find_best_prio_not_visited_field(self, reindeer_field: Field) -> Optional[MovementData]:
        vectors_to_fields = {}

        for vector in Vectors.ALL:
            field = self._maze.get_field(reindeer_field.x + vector[0], reindeer_field.y + vector[1])
            if field and field.content != FieldContent.WALL and not field.visited:
                vectors_to_fields[vector] = field

        best_movement_data = tuple()

        for vector, field in vectors_to_fields.items():
            if not best_movement_data or field.prio < best_movement_data[0].prio:
                best_movement_data = field, vector

        return best_movement_data

    def _is_field_on_path_in_previous_solutions(self, field: Field):
        for solution in self._solutions:
            field_in_previous_solution = solution.maze.get_field(field.x, field.y)
            if field_in_previous_solution.on_path:
                return True
        return False

    def _rotate_reindeer(self, reindeer_field: Field, vector: Vector):
        directions_for_vectors = {Vectors.UP: FieldContent.REINDEER_FACING_UP,
                                  Vectors.RIGHT: FieldContent.REINDEER_FACING_RIGHT,
                                  Vectors.DOWN: FieldContent.REINDEER_FACING_DOWN,
                                  Vectors.LEFT: FieldContent.REINDEER_FACING_LEFT}
        direction = directions_for_vectors[vector]

        if direction != reindeer_field.content:
            self._add_action(ActionNames.ROTATION, reindeer_field.content, direction)
            reindeer_field.rotate(direction)

            self._show_actions() if self._log_level == 'trace' else None
            self._maze.show() if self._log_level == 'trace' else None

    def _move_reindeer(self, reindeer_field: Field, target_field: Field, undoing: bool = False):
        if target_field.content != FieldContent.WALL:
            target_field.insert(reindeer_field.content)
            reindeer_field.clear(undoing)

            if not undoing:
                self._add_action(ActionNames.MOVEMENT, reindeer_field, target_field)

            self._show_actions() if self._log_level == 'trace' else None
            self._maze.show() if self._log_level == 'trace' else None

    def _undo_last_action(self):
        last_action = self._actions.pop()

        if last_action.name == ActionNames.MOVEMENT:
            self._move_reindeer(last_action.end_state, last_action.start_state, undoing=True)
            if self._actions and self._actions[-1].name == ActionNames.ROTATION:
                last_action = self._actions.pop()

        if last_action.name == ActionNames.ROTATION:
            self._maze.find_reindeer_field().rotate(last_action.start_state)

    def _add_action(self, name: str, start_state: Any, end_state: Any):
        self._actions.append(Action(name, start_state, end_state))

    def _show_actions(self):
        print('\nACTIONS:')

        for action in self._actions:
            print(f'{action.name} from {action.start_state} to {action.end_state}')

    def _score_actions(self):
        score = 0

        for action in self._actions:
            score += 1000 if action.name == ActionNames.ROTATION else 1

        return score

    def _register_solution(self, solution_id: int):
        score = self._score_actions()
        self._solutions.append(Solution(solution_id, score, self._maze, self._actions))

    def _find_best_solution(self) -> Solution:
        best_solution = None

        for solution in self._solutions:
            if not best_solution or solution.score < best_solution.score:
                best_solution = solution

        return best_solution
