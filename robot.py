import os
import csv
import random
from datetime import datetime
from typing import List, Tuple

from config import (
    BASE_POS,
    BASE_X,
    BASE_Y,
    BATTERIE_INIT,
    MAP_L,
    MAP_H,
    RECHARGE,
)


class Robot:
    def __init__(self, rid: int, world: List[List[int]]):
        self.id = rid
        self.world = world
        self.x, self.y = BASE_POS
        self.battery = BATTERIE_INIT
        self.returning = False
        self.recharge_time = 0
        self.logs: List[Tuple[datetime, int, int]] = []
        print(f"[Init] Robot {self.id} initialisé avec {self.battery}%.")

    def color(self) -> str:
        if self.battery <= 5:
            return "red"
        if self.battery <= 50:
            return "orange"
        return "lime"

    def step(self) -> bool:
        temp = self.world[self.y][self.x]
        self.logs.append((datetime.now(), temp, self.battery))
        print(f"[Step] R{self.id} @({self.x},{self.y}) | T={temp}°C | B={self.battery}%")

        if self.recharge_time > 0:
            self.recharge_time -= 1
            self.battery = min(BATTERIE_INIT, self.battery + 20)
            return True

        if self.battery <= 5:
            return False

        if self.battery <= 50 or self.returning:
            self.returning = True
            dx = -1 if self.x > BASE_X else (1 if self.x < BASE_X else 0)
            dy = -1 if self.y > BASE_Y else (1 if self.y < BASE_Y else 0)
        else:
            dx = random.choice([-1, 0, 1])
            dy = random.choice([-1, 0, 1])

        self.x = max(0, min(MAP_L - 1, self.x + dx))
        self.y = max(0, min(MAP_H - 1, self.y + dy))
        self.battery -= random.choice([5, 10])

        if (self.x, self.y) == BASE_POS and self.returning:
            self.recharge_time = RECHARGE
            self.returning = False
        return True

    def save_csv(self) -> None:
        os.makedirs("data", exist_ok=True)
        with open(f"data/robot_{self.id}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["datetime", "temperature", "battery"])
            for dt, temp, bat in self.logs:
                writer.writerow([dt.strftime("%Y-%m-%d %H:%M:%S"), temp, bat])
