from math import dist, prod


class JunctionBox:
    def __init__(self, x: str, y: str, z: str) -> None:
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self._connections: list[JunctionBox] = []

    @property
    def connected(self) -> bool:
        return bool(self._connections)

    def connect(self, junction_box: JunctionBox):
        self._connections.append(junction_box)

    # TODO: remove
    def __repr__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'


class DecorationProject:
    def __init__(self) -> None:
        self._junction_boxes: list[JunctionBox] = []
        self._distances: list[tuple[float, JunctionBox, JunctionBox]] = []
        self._circuits: list[list[JunctionBox]] = []

    def map_junction_boxes(self, input_file_path: str):
        with open(input_file_path) as input_file:
            self._junction_boxes = [JunctionBox(*line.strip().split(',')) for line in input_file.readlines()]
        self._measure_distances()

    def connect_junction_boxes(self, count: int):
        print('Connecting junction boxes...')
        connections = 0

        for junction_boxes_distance in self._distances:
            _, first_junction_box, second_junction_box = junction_boxes_distance

            print('----------------------------------------------------------')
            print(f'ANALYSING: \t\t{first_junction_box}, {second_junction_box}')

            if not self._are_in_same_circuit(first_junction_box, second_junction_box):
                print(f'CONNECTING: \t\t{first_junction_box}, {second_junction_box}')

                connections += 1
                first_junction_box.connect(second_junction_box)
                second_junction_box.connect(first_junction_box)

                in_circuit = False

                for circuit in self._circuits:
                    if first_junction_box in circuit:
                        circuit.append(second_junction_box)
                        in_circuit = True
                        break
                    if second_junction_box in circuit:
                        circuit.append(first_junction_box)
                        in_circuit = True
                        break
                
                if not in_circuit:
                    self._circuits.append([first_junction_box, second_junction_box])

                print('CIRCUITS:')
                for circuit in self._circuits:
                    print(circuit)
            else:
                print(f'SKIPPING: \t\t{first_junction_box}, {second_junction_box}')

            if connections == count:
                break

    def multiply_sizes_of_largest_circuits(self, count: int) -> int:
        sorted_circuits = sorted(self._circuits, key=lambda c: len(c), reverse=True)
        return prod(map(len, sorted_circuits[:count]))

    def _measure_distances(self):
        print('Measuring distances...')
        for reference_id, reference_junction_box in enumerate(self._junction_boxes):
            for junction_box in self._junction_boxes[reference_id + 1:]:
                distance = dist((reference_junction_box.x, reference_junction_box.y, reference_junction_box.z), 
                                (junction_box.x, junction_box.y, junction_box.z))
                junction_boxes_distance = (distance, reference_junction_box, junction_box)
                self._distances.append(junction_boxes_distance)

        self._distances = sorted(self._distances, key=lambda d: d[0])

    def _are_in_same_circuit(self, first_junction_box: JunctionBox, second_junction_box: JunctionBox):
        for circuit in self._circuits:
            if first_junction_box in circuit and second_junction_box in circuit:
                return True

        return False