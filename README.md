# Vers-de-Paterson

Je me suis beaucoup aidé de ces trois sites : 


-Les deux premiers pour comprendre, parce qu'il y a peu de doc en anglais, alors en français c'était encore pire

http://www.mathpuzzle.com/MAA/01-Paterson's%20Worms/mathgames_10_24_03.html
https://en.wikipedia.org/wiki/Paterson%27s_worms


-Celui-ci pour le fantastique tableau, utilisez le pour trouver les graines, elle y sont toutes (lorsque des graines sont symétriques ils ne les mettent pas dans le tableau)

https://fr.wikipedia.org/wiki/Vers_de_Paterson


Les règles : 

De façon générale, les vers de Paterson sont un type de turmite définis sur les bords d'une grille isométrique hexagonale.

En considérant une grille triangulaire infinie, on considère l'un des nœuds de cette grille comme étant un « ver ». 
Le ver se déplace initialement le long d'une ligne de la grille vers le nœud immédiatement situé à sa droite.

Arrivé à ce nœud, le ver peut prendre cinq directions possibles sans revenir sur ses pas. On pose que le ver prend l'une d'entre elles, 
avance vers le nœud suivant en conséquence et continuera à faire de même tant qu'il arrivera sur un nœud où cinq directions sont possibles :

Si le ver a continué tout droit, il continuera à faire de même indéfiniment
Si le ver a tourné de 60° à gauche ou à droite, il fera de même pendant cinq tours pour finalement retomber après un parcours hexagonal sur le nœud de départ 
où seules quatre directions sont possibles, puisqu'une cinquième a déjà été empruntée par le ver
Si le ver a tourné de 120° à gauche ou à droite, il retombe sur le nœud initial au bout de deux tours et là aussi, seules quatre directions sont possibles.
Dans les deux derniers cas, il est nécessaire de définir une direction que le ver va prendre parmi les quatre possibles. Ensuite, on procède à chaque nœud de la manière suivante :

Si la situation a déjà été rencontrée par le ver, il se déplace comme il l'a fait dans cette situation
Si la situation est inédite, on choisit une direction. Elle sera ensuite utilisée à chaque fois que la même situation se produira
Si le ver arrive sur un nœud dont toutes les directions ont déjà été utilisées, il s'arrête.

PS : J'avais d'abord fait ce programme en TI-Basic sur calculatrice en 2019, le voilà en Python 3 ans après.
