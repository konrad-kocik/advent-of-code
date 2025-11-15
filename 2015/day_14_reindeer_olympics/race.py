from dataclasses import dataclass


@dataclass
class Reindeer:
    name: str
    speed: int
    fly_duration: int
    rest_duration: int
    is_flying: bool = False
    fly_time_remaining: int = 0
    rest_time_remaining: int = 0
    distance: int = 0


def race(input_file_path: str, duration: int) -> tuple[str, int]:
    reindeers = _get_reindeers(input_file_path)
    _simulate_race(reindeers, duration)
    winner, distance = _find_winner(reindeers)
    return winner, distance


def _get_reindeers(input_file_path: str) -> list[Reindeer]:
    reindeers = []
    
    with open(input_file_path) as input_file:
        for line in input_file:
            parts = line.split()
            name = parts[0]
            speed = int(parts[3])
            fly_duration = int(parts[6])
            rest_duration = int(parts[13])
            reindeers.append(Reindeer(name, speed, fly_duration, rest_duration))

    return reindeers


def _simulate_race(reindeers: list[Reindeer], duration: int):
    _launch_reindeers(reindeers)

    for _ in range(duration):
        for reindeer in reindeers:
            if reindeer.is_flying:
                reindeer.distance += reindeer.speed
                reindeer.fly_time_remaining -= 1
                if reindeer.fly_time_remaining == 0:
                    reindeer.is_flying = False
                    reindeer.rest_time_remaining = reindeer.rest_duration
            else:
                reindeer.rest_time_remaining -= 1
                if reindeer.rest_time_remaining == 0:
                    reindeer.is_flying = True
                    reindeer.fly_time_remaining = reindeer.fly_duration


def _launch_reindeers(reindeers: list[Reindeer]):
    for reindeer in reindeers:
        reindeer.is_flying = True
        reindeer.fly_time_remaining = reindeer.fly_duration


def _find_winner(reindeers: list[Reindeer]) -> tuple[str, int]:
    winner: Reindeer = reindeers[0]

    for reindeer in reindeers:
        if reindeer.distance > winner.distance:
            winner = reindeer

    return winner.name, winner.distance
