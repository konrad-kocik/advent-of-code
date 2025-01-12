from typing import List, Tuple

GardenMap = List[List[str]]
Plot = Tuple[int, int]
Plots = List[Plot]


class Region:
    def __init__(self, plant_type: str):
        self._plant_type: str = plant_type
        self._plots: Plots = []
        self._neighbouring_plots: List[Tuple[Plot, Plot]] = []

    @property
    def plant_type(self) -> str:
        return self._plant_type

    @property
    def area(self) -> int:
        return len(self._plots)

    @property
    def perimeter(self) -> int:
        return self.area * 4 - len(self._neighbouring_plots) * 2

    def contains(self, plot: Plot) -> bool:
        return plot in self._plots

    def add_plot(self, plot: Plot):
        self._plots.append(plot)

    def add_neighbouring_plots(self, plot: Plot, neighbours: Plots):
        for neighbour in neighbours:
            if ((plot, neighbour) not in self._neighbouring_plots and
                (neighbour, plot) not in self._neighbouring_plots):
                self._neighbouring_plots.append((plot, neighbour))


def calculate_total_price_of_fence(input_file_path: str) -> int:
    garden_map = _map_garden(input_file_path)
    regions = _find_regions(garden_map)
    return sum([region.area * region.perimeter for region in regions])


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
