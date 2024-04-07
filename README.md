## Implementation de l'algorithme Minimax dans un jeu
Ce projet est le jeu du morpion  en __GUI__ où deux adversaires s'affrontent: un joueur principal et l'ordinateur. Il met l'accent sur une sorte d'intelligence de l'ordinateur pour contrer les plans de l'adversaire et essayer de remporter la partie. Dans ce projet, l'accent est plutôt mis sur l'algorithme __minimax__ qui est utilisé par l'ordinateur pour jouer ces coups.

![L'arbre illustrant l'algorithme minimax](https://cdn.educba.com/academy/wp-content/uploads/2020/03/Minimax-Algorithm.jpg)

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
  
Exécutez le script du jeu avec la commande :
 ```
python minimax.py
 ```

## Comment ça fonctionne
- ``` main.py```  héberge la classe ```TicTacToe```  qui se chargent de toute la partie logique du programme en ce qui concerne le choix des symboles des joeurs, le coup de l'ordinateur, l'identification du gagnant et autes et la classe ```TicTacToeGUI```  pour gérer la partie interface graphique où toutes les interactions sont visuels par l'utilisateur.
- Dans notre classe  ```TicTacToe```  se trouvent la fonction  ```minmax```  qui se chargent de choisir le meilleur coup possible à jouer pour l'ordinateur en explorant l'arbre de jeu en profondeur d'où l'intelligence derrière.
## Licence
Ce projet est open source sous la [licence MIT](LICENSE)

## Contribuant
N'hésitez pas à contribuer à ce projet. Les améliorations suggérées, les rapports de bogues ou les demandes d'extraction sont toujours les bienvenus.

## Quelques ressources

Pour approofondir vos connaissances ou en savoir plus sur l'algorithme __minimax__, voici quelques ressources:
1. __Livre__ : ```Artificial Intelligence: A Modern Approach```  par __Stuart Russell__ et __Peter Norvig__. Ce livre couvre divers aspects de l'intelligence artificielle, y compris l'algorithme Minimax pour les jeux.
   
   [Artificial Intelligence: A Modern Approach](https://dl.ebooksworld.ir/books/Artificial.Intelligence.A.Modern.Approach.4th.Edition.Peter.Norvig.%20Stuart.Russell.Pearson.9780134610993.EBooksWorld.ir.pdf)
