## Implementation de l'algorithme Minimax dans un jeu
Ce projet est le jeu du morpion  en __GUI__ où deux adversaires s'affrontent: un joueur principal et l'ordinateur. Il met en avant une sorte d'intelligence de l'ordinateur pour contrer les plans de l'adversaire et essayer de remporter la partie. Dans ce projet, l'accent est plutôt mis sur l'algorithme __minimax__ qui est utilisé par l'ordinateur pour jouer ces coups.

Dans ce projet j'ai eu à utiliser des compétences en **POO**, et en **Tkinter** pour l'interface graphique
<!--├──
├──
├──-->
## Installation
1. Clonez le référentiel sur votre ordinateur local
   ```
   git clone https://github.com/eliakimceleste/minimax.git
   ```
2. Accéder au dossier du projet
	 ```
   cd minimax
   ```
3. Assurez-vous d'avoir installer __python__ sur votre ordinateur
## Usage
- Sur windows
  
	Exécutez le script du jeu avec la commande :
```
  python minimax.py
```
- Sur Ubuntu
  
	Exécutez le script du jeu avec la commande :
```
  python3 minimax.py
```
## Comment ça fonctionne
- __main.py__ héberge la __TicTacToe__ class qui se chargent de toute la partie logique du programme en ce qui concerne le choix des symboles des joeurs, le coup de l'ordinateur, l'identification du gagnant et autes et la __TicTacToeGUI__ class pour gérer la partie interface graphique où toutes les interactions sont visuels par l'utilisateur.
- Dans notre classe __TicTacToe se trouvent la fonction __minmax__ qui se chargent de choisir le meilleur coup possible à jouer pour l'ordinateur en explorant l'arbre de jeu en profondeur d'où l'intelligence derrière.
## Licence
Ce projet est open source sous la [licence MIT](LICENCE)
