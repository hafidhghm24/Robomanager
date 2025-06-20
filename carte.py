import random
from typing import List

from config import MAP_L, MAP_H, TEMP_MIN, TEMP_MAX


def create_map() -> List[List[int]]:
    return [[random.randint(TEMP_MIN, TEMP_MAX) for _ in range(MAP_L)] for _ in range(MAP_H)]
