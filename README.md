# Projet-Avion
Projet Avion. LSIN200
#Double Licence Maths Physique
#Groupe 4

# BENGOCHEA BIXENTE
# MULLER FELIX
# MARDAOUI YANISS
# FEDERSPIEL LUCAS
# BURAT JAMES
# LESUEUR AXEL



I/. Fonctionnement du programme.

    1). Juste après l’exécution du programme, une fenêtre graphique comportant, 1 canevas vide et 3 boutons, apparaît. 
    
    2). Tout d'abords il faut appuyer sur le bouton "Generate Terrain", le premier bouton en haut à gauche de la fenêtre graphique. Comme son nom l'indique, ce bouton permet d'afficher les sièges(en gris) ainsi que le couloir(en blanc) de l'avion. (Attention: si le terrain n'a pas été généré au préalable, le programme ne fonctionnera pas.)
    
    3). Une fois le terrain générer, vous avez la possibilité de visionner étape par étape l’exécution du programme. Pour cela, appuyez sur le bouton du milieu "Prochaine Étape". Une seule étape du programme va alors s’exécuter. Vous pouvez appuyer une nouvelle fois sur "Prochaine Étape" pour lancer la deuxième étapes du programme, (ect...).
    Lors de l’exécution du programme, les passagers (représentés par des cercles de différentes couleurs) avancent dans le couloir central de l'avion. Les passagers sont représentés de différentes couleurs, qui définissent leur situation dans l'avion: 
    -les cercles rouges représentent les passagers possédants 2 bagages avec eux. 
    -les cercles corail représentent les passagers possédants 1 bagage avec eux.
    -les cercles bleu représentent les passagers sans bagage qui ne sont toujours pas arrivés à leur place.
    -les cercles verts représentent les passagers assis à leur place.

    4). Vous avez aussi la possibilité de visionner l’exécution complète du programme. Pour cela vous pouvez cliquer sur le dernier bouton, "Lancer Simulation". Le programme s’exécutera entièrement et s’arrêtera quand tout les passagers auront atteint leur place.

II/. Commentaire sur le Programme.

        1). Nous avons eu des difficultés pour créer le programme. En effet, le nombre de place maximal est limité par les caractéristiques de l'ordinateur dû à l'utilisation trop redondante de la fonction "For". L'ordinateur doit vérifier trop souvent les carractéristiques des différents passagers. Malheureusement ceci est une des caractéristiques de ce projet, qui nous a posé le plus problème. Nous avons essayer de trouver une solution en enlevant les personnes assises a leure places de la liste des passagers, mais ceci n'a pas accéléré l'execution puisque cela nous donnait des étapes en plus (on devra voir pour chaque passagers s'il est a ca place apres chaque étape, ce qui nous rajoute une boucle "for" en plus) et en plus, ces passagers ne vont donc pas pouvoir changer de place avec un autre passagers qui est assis a la fênetre par exemple.
        Par la suite nous avons réussi à pallier cette difficulté en utilisant la fonction "break" dans nos boucles ce qui a vraiement accéléré l'execution du code.  
        Nous avons aussi eu l'idée de représenter les passagers par des images, mais cette idée s'est fait rejetté puisqu'elle posait problème d'interprétation. Un système de couleurs est beaucoup plus intuitif et par conséquent plus compréhensible.
