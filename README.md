## Implementation de l'algorithme Minimax dans un jeu
Ce projet est le jeu du morpion  en __GUI__ où deux adversaires s'affrontent: un joueur principal et l'ordinateur. Il met l'accent sur une sorte d'intelligence de l'ordinateur pour contrer les plans de l'adversaire et essayer de remporter la partie. Dans ce projet, l'accent est plutôt mis sur l'algorithme __minimax__ qui est utilisé par l'ordinateur pour jouer ses coups.

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

Pour approfondir vos connaissances ou en savoir plus sur l'algorithme __minimax__, voici quelques ressources:
1. __Livre__ : [Artificial Intelligence: A Modern Approach](https://dl.ebooksworld.ir/books/Artificial.Intelligence.A.Modern.Approach.4th.Edition.Peter.Norvig.%20Stuart.Russell.Pearson.9780134610993.EBooksWorld.ir.pdf)  par __Stuart Russell__ et __Peter Norvig__ que l'on surnomme la ```Bible de l'IA```  :wink:.  Ce livre couvre divers aspects de l'intelligence artificielle, y compris l'algorithme Minimax pour les jeux.

2. __Article__ : [Understanding the Minimax Algorithm](https://medium.com/towards-data-science/understanding-the-minimax-algorithm-726582e4f2c6) par Dorian Lazar. Cet article explique l'algorithme Minimax de manière détaillée avec des exemples et des illustrations.

3. __Vidéo Youtube__ : [Minimax Algorithm Explained](https://www.youtube.com/watch?v=l-hh51ncgDI&t=54s) par __Sebastian Lague__. Cette vidéo offre une explication visuelle de l'algorithme Minimax et de son fonctionnement.

__Je pense que ces ressources peuvent aller pour un début. Il y a tellement de ressources qu'on ne peut tout citer.__


