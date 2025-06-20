# Robomanager

⚙️ **Fonctionnalités**

- 🌡️ Carte thermique générée aléatoirement (températures entre -20°C et 80°C)
- 🤖 Robots autonomes se déplaçant sur la carte
- 🔋 Gestion intelligente de la batterie :
  - >50 % : exploration (vert 🟢)
  - ≤50 % : retour à la base (orange 🟠)
  - ≤5 % : arrêt (rouge 🔴)
- 🏠 Recharge automatique après retour à la base pendant `RECHARGE = 5` ticks
- 📁 Enregistrement des données dans des fichiers CSV (température + batterie)
- 🎞️ Animation GIF générée automatiquement à la fin de la simulation

🧠 **Concepts clés**

- Visualisation avec matplotlib (`imshow`, `scatter`, `animation.FuncAnimation`)
- Programmation orientée objet avec la classe `Robot`
- Palette `coolwarm` pour la carte thermique
- Fichier CSV pour le suivi des données
- GIF animé généré automatiquement pour représenter la simulation

🚀 **À propos**

Ce projet a été imaginé et développé par [@hafidhghm24](https://github.com/hafidhghm24) comme projet d’apprentissage Python/robotique.
N'hésitez pas à donner des conseils !
