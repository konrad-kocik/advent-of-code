from dataclasses import dataclass
from itertools import product
from typing import Iterator


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def find_best_recipe(input_file_path: str) -> int:
    ingredients = _get_ingredients(input_file_path)
    score = _find_best_recipe(ingredients)
    return score


def _get_ingredients(input_file_path: str) -> list[Ingredient]:
    ingredients = []

    with open(input_file_path) as input_file:
        for line in input_file:
            name, properties = line.split(': ')
            properties = properties.split()
            capacity = int(properties[1][:-1])
            durability = int(properties[3][:-1])
            flavor = int(properties[5][:-1])
            texture = int(properties[7][:-1])
            calories = int(properties[9])
            ingredients.append(Ingredient(name, capacity, durability, flavor, texture, calories))

    return ingredients


def _find_best_recipe(ingredients: list[Ingredient]) -> int:
    best_score = 0

    for ingredients_combination in _ingredients_combinations(total_spoons=100, ingredients_count=len(ingredients)):
        capacity_score, durability_score, flavor_score, texture_score = 0, 0, 0, 0

        for ingredient_id, ingredient in enumerate(ingredients):
            spoons_count = ingredients_combination[ingredient_id]
            capacity_score += spoons_count * ingredient.capacity
            durability_score += spoons_count * ingredient.durability
            flavor_score += spoons_count * ingredient.flavor
            texture_score += spoons_count * ingredient.texture

        combination_score = ((capacity_score if capacity_score > 0 else 0) * 
                             (durability_score if durability_score > 0 else 0) * 
                             (flavor_score if flavor_score > 0 else 0) * 
                             (texture_score if texture_score > 0 else 0))

        if combination_score > best_score:
            best_score = combination_score

    return best_score


def _ingredients_combinations(total_spoons: int, ingredients_count: int) -> Iterator[tuple[int, ...]]:
    for spoons_of_ingredients in product(range(total_spoons+1), repeat=ingredients_count):
        if sum(spoons_of_ingredients) == total_spoons:
            yield spoons_of_ingredients
