PresentDimensions = tuple[int, int, int]


def calculate_wrapping_paper_order(input_file_path: str) -> int:
    presents_dimensions = _get_presents_dimensions(input_file_path)
    return _calculate_total_wrapping_paper_area(presents_dimensions)


def calculate_ribbon_order(input_file_path: str) -> int:
    presents_dimensions = _get_presents_dimensions(input_file_path)
    return _calculate_total_ribbon_length(presents_dimensions)


def _get_presents_dimensions(input_file_path: str) -> list[PresentDimensions]:
    presents_dimensions= []

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            present_dimensions = tuple(int(dimension) for dimension in line.strip().split('x'))
            presents_dimensions.append(present_dimensions)

    return presents_dimensions


def _calculate_total_wrapping_paper_area(presents_dimensions: list[PresentDimensions]) -> int:
    total_wrapping_paper_area = 0

    for present_dimensions in presents_dimensions:
        length, width, height = present_dimensions
        side_areas = [length * width, width * height, height * length]
        present_surface_area = 2 * sum(side_areas) + min(side_areas)
        total_wrapping_paper_area += present_surface_area

    return total_wrapping_paper_area


def _calculate_total_ribbon_length(presents_dimensions: list[PresentDimensions]) -> int:
    total_ribbon_length = 0

    for present_dimensions in presents_dimensions:
        length, width, height = present_dimensions
        smallest_present_perimeter = sum(sorted(present_dimensions)[:2]) * 2
        bow_length = length * width * height
        total_ribbon_length += smallest_present_perimeter + bow_length

    return total_ribbon_length
