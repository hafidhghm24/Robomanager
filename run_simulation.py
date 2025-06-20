from robots.robot import Robot  # ✅ pas de /, majuscule au nom de classe
from carte import creation_map
from config import *

def run_simulation():
    # 🗺️ Création de la carte
    carte = creation_map(MAP_H, MAP_L)

    # 🤖 Création des robots
    robots = []
    for i in range(NB_BOTS):
        r = Robot(i, carte)
        robots.append(r)

    # 🚶‍♂️ Chaque robot se déplace
    for robot in robots:
        robot.deplacement()

    # 🔍 Affichage de la carte
    print("\n🗺️ Carte finale :\n")
    for ligne in carte:
        print(ligne)

if __name__ == "__main__":
    run_simulation()
