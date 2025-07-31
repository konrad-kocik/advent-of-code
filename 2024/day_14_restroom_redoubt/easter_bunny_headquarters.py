from typing import List, Tuple
from math import prod

Coords = Tuple[int, int]
Sector = Tuple[Coords, Coords]


class Robot:
    _next_id = 1

    def __init__(self, position_x: int, position_y: int, velocity_x: int, velocity_y: int):
        self._id = Robot._next_id
        Robot._next_id += 1
        self._position_x = position_x
        self._position_y = position_y
        self._velocity_x = velocity_x
        self._velocity_y = velocity_y

    def move(self, area_width: int, area_height: int):
        new_x = self._position_x + self._velocity_x
        new_y = self._position_y + self._velocity_y

        if new_x >= area_width:
            new_x = new_x - area_width
        elif new_x < 0:
            new_x = area_width + new_x

        if new_y >= area_height:
            new_y = new_y - area_height
        elif new_y < 0:
            new_y = area_height + new_y

        self._position_x = new_x
        self._position_y = new_y

    def is_in_sector(self, sector: Sector) -> bool:
        sector_start_x = sector[0][0]
        sector_start_y = sector[0][1]
        sector_end_x = sector[1][0]
        sector_end_y = sector[1][1]

        return sector_start_x <= self._position_x <= sector_end_x and sector_start_y <= self._position_y <= sector_end_y


def calculate_safety_factor(input_file_path: str, area_width: int, area_height: int) -> int:
    robots = _scout_robots(input_file_path)
    robots = _simulate_robots_patrol(robots, area_width, area_height, seconds=100)
    sectors = _divide_area_into_sectors(area_width, area_height)
    robots_count_in_sectors = _count_robots_in_sectors(robots, sectors)
    return prod(robots_count_in_sectors)


def _scout_robots(input_file_path: str) -> List[Robot]:
    robots = []

    with open(input_file_path, 'r') as file:
        for line in file:
            position, velocity = line.strip().split(' ')
            position_x, position_y = position.replace('p=', '').split(',')
            velocity_x, velocity_y = velocity.replace('v=', '').split(',')
            robots.append(Robot(int(position_x), int(position_y), int(velocity_x), int(velocity_y)))

    return robots


def _simulate_robots_patrol(robots: List[Robot], area_width: int, area_height: int, seconds: int) -> List[Robot]:
    for second in range(1, seconds + 1):
        for robot in robots:
            robot.move(area_width, area_height)

    return robots


def _divide_area_into_sectors(area_width: int, area_height: int) -> List[Sector]:
    x_border = area_width // 2
    y_border = area_height // 2

    nw_sector = ((0, 0), (x_border - 1, y_border - 1))
    ne_sector = ((x_border + 1, 0), (area_width - 1, y_border - 1))
    sw_sector = ((0, y_border + 1), (x_border - 1, area_height - 1))
    se_sector = ((x_border + 1, y_border + 1), (area_width - 1, area_height - 1))

    return [nw_sector, ne_sector, sw_sector, se_sector]


def _count_robots_in_sectors(robots: List[Robot], sectors: List[Sector]):
    robots_count_in_sectors = []

    for sector in sectors:
        robots_count_in_sector = 0

        for robot in robots:
            if robot.is_in_sector(sector):
                robots_count_in_sector += 1

        robots_count_in_sectors.append(robots_count_in_sector)

    return robots_count_in_sectors
