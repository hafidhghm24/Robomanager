import random 
from config import *

def creation_map(hauteur: int, largeur: int):
    carte = []
    for _ in range(hauteur):
        ligne = []
        for _ in range(largeur):
            temperature = random.randint(TEMP_MIN, TEMP_MAX)
            ligne.append(temperature)
        carte.append(ligne)
    return carte

if __name__ == "__main__":
    carte = creation_map(MAP_H, MAP_L)
    for ligne in carte:
        print(ligne)
