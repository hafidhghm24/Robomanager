import random
from config import *

class Robot:
    def __init__(self, identifiant: int, carte: list[list[int]]):
        self.id = identifiant
        self.carte = carte
        self.x = BASE_POSITION[0]
        self.y = BASE_POSITION[1]
        self.batterie = BATTERIE
        self.historique = []

    def deplacement(self):
        for _ in range(TOUR_MAX):
            temperature = self.carte[self.y][self.x]

            if self.batterie <= 5:
                print(f"🟥 Robot {self.id} : Batterie critique. Robot éteint.")
                break

            elif 5 < self.batterie <= 50:
                print(f"🟨 Robot {self.id} : Batterie faible. Retour à la base.")
                self.x, self.y = BASE_POSITION
                break

            else:
                self.batterie -= 5
                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1])
                self.x = max(0, min(MAP_L - 1, self.x + dx))
                self.y = max(0, min(MAP_H - 1, self.y + dy))
                self.historique.append(((self.x, self.y), temperature)) #tuple
                print(f"🔋 Robot {self.id} - Position : ({self.x},{self.y}) | Température : {temperature}°C | Batterie : {self.batterie}%")

        return self.historique #exemple: [((0, 0), 25), ((1, 0), 30), ((2, 1), 27)]

