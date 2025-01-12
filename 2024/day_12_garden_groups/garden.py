from typing import List, Tuple
from itertools import chain

GardenMap = List[List[str]]
Plot = Tuple[int, int]
Plots = List[Plot]
Fence = Tuple[Plot, str]
Fences = List[Fence]
Sides = List[Fences]


class Region:
    def __init__(self, plant_type: str):
        self._plant_type: str = plant_type
        self._plots: Plots = []
        self._neighbouring_plots: List[Tuple[Plot, Plot]] = []
        self._fences: Fences = []
        self._sides: Sides = []

    @property
    def plant_type(self) -> str:
        return self._plant_type

    @property
    def area(self) -> int:
        return len(self._plots)

    @property
    def perimeter(self) -> int:
        return len(self._find_fences())

    @property
    def sides_count(self) -> int:
        return len(self._find_sides())

    def contains(self, plot: Plot) -> bool:
        return plot in self._plots

    def add_plot(self, plot: Plot):
        self._plots.append(plot)

    def add_neighbouring_plots(self, plot: Plot, neighbours: Plots):
        for neighbour in neighbours:
            if ((plot, neighbour) not in self._neighbouring_plots and
                (neighbour, plot) not in self._neighbouring_plots):
                self._neighbouring_plots.append((plot, neighbour))

    def _find_sides(self) -> Sides:
        fences = self._find_fences()
        sides = []

        for fence in fences:
            fences_added_to_sides = chain(*sides)

            if fence not in fences_added_to_sides:
                side = []
                self._add_fences_to_side(fences, fence, side)
                sides.append(side)

        return sides

    def _find_fences(self) -> Fences:
        fences = []

        for plot in self._plots:
            y, x = plot
            potential_neighbours = {'north': (y - 1, x),
                                    'south': (y + 1, x),
                                    'east': (y, x + 1),
                                    'west': (y, x - 1)}

            for direction, potential_neighbour in potential_neighbours.items():
                has_neighbour = any([neighbours for neighbours in self._neighbouring_plots
                                    if plot in neighbours and potential_neighbour in neighbours])
                if not has_neighbour:
                    fences.append((plot, direction))

        return fences

    def _add_fences_to_side(self, fences: Fences, fence: Fence, side: Fences):
        side.append(fence)
        plot, direction = fence
        y, x, = plot
        plots_to_check = [(y, x - 1), (y, x + 1)] if direction in ['north', 'south'] else [(y - 1, x), (y + 1, x)]
        next_fences = []

        for plot_to_check in plots_to_check:
            fence_to_check = (plot_to_check, direction)

            if fence_to_check in fences and fence_to_check not in side:
                next_fences.append(fence_to_check)

        for next_fence in next_fences:
            self._add_fences_to_side(fences, next_fence, side)


def calculate_total_price_of_fence(input_file_path: str, bulk_discount: bool = False) -> int:
    garden_map = _map_garden(input_file_path)
    regions = _find_regions(garden_map)
    return _calculate_fence_price(regions, bulk_discount)


def _map_garden(input_file_path: str) -> GardenMap:
    garden = []

    with open(input_file_path, 'r') as file:
        for line in file:
            row = [plot for plot in line.strip()]
            garden.append(row)

    return garden


def _find_regions(garden_map: GardenMap) -> List[Region]:
    regions = []

    for y, row in enumerate(garden_map):
        for x, plant_type in enumerate(row):
            plot = (y, x)

            if not any([region.contains(plot) for region in regions]):
                region = Region(plant_type)
                _add_plots_to_region(garden_map, plot, region)
                regions.append(region)

    return regions


def _add_plots_to_region(garden_map: GardenMap, plot: Plot, region: Region):
    if not region.contains(plot):
        region.add_plot(plot)
        neighbours = _find_neighbours(garden_map, plot, region.plant_type)
        region.add_neighbouring_plots(plot, neighbours)

        for neighbour in neighbours:
            _add_plots_to_region(garden_map, neighbour, region)


def _find_neighbours(garden_map: GardenMap, plot: Plot, plant_type: str) -> Plots:
    y, x = plot
    neighbours = []

    if y - 1 >= 0 and garden_map[y - 1][x] == plant_type:
        neighbours.append((y - 1, x))

    if y + 1 < len(garden_map) and garden_map[y + 1][x] == plant_type:
        neighbours.append((y + 1, x))

    if x + 1 < len(garden_map[0]) and garden_map[y][x + 1] == plant_type:
        neighbours.append((y, x + 1))

    if x - 1 >= 0 and garden_map[y][x - 1] == plant_type:
        neighbours.append((y, x - 1))

    return neighbours


def _calculate_fence_price(regions: List[Region], bulk_discount: bool) -> int:
    if bulk_discount:
        return sum([region.area * region.sides_count for region in regions])
    else:
        return sum([region.area * region.perimeter for region in regions])
