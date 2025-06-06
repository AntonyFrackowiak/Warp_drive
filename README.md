#English version

# Program created as part of a Master's internship.
Author: Antony Frackowiak  
Master's Degree in Cosmology at Claude Bernard University Lyon 1.

**Alcubierre**  
This project is part of a Master's 2 degree internship focused on modeling the Alcubierre warp bubble — a theoretical model of faster-than-light propulsion in general relativity.


## Table of Contents

- [Installation]
- [Usage]
- [Project Structure]
- [Program explanations]
- [License]

## Installation

Make sure you've installed these different Packages:

- `numpy`
- `matplotlib`
- `scipy`-
-
-


To install **Alcubierre**, follow these steps:

1. Clone the GitHub repository:
   
    ```bash
    $ git clone https://github.com/AntonyFrackowiak/Warp_drive.git
    $ cd Warp_drive

   
2. Go into the folder containing `__main__.py`:
	```bash
    $ cd Program
    ```
	And choose between:
	```bash
    $ cd Alcubierre
    ```
    or 
    ```bash
    $ cd General_warp_drive
    ```

## Usage

To run any of the programs corresponding to a specific section, simply enter the following in the command terminal:

	```bash
	$ python .
	```	

In the terminal, the following message will appear: 

	```bash
	Choose an option:
	1.1 - Section 1.1
	1.2.3 - Section 1.2.3
	2 - Section 2
	Enter your choice (1.1, 1.2.3, 2): 
	```

Just type in the desired section number, for example: 
	```bash
	"1.1" or "1.2.3" or "2".
	```

## Project Structure

This project includes the following files:  

Warp_drive/
│
├── README.md               ← This documentation file
├── LICENSE                 ← License file (MIT)
│
└── Program/
    ├── General_warp_drive/       ← Generic warp drive framework (WIP)
    │
    └── Alcubierre/               ← Main Alcubierre module
        ├── __main__.py           ← Entry point
        ├── __init__.py           ← Package initializer
        ├── Initial_data.py       ← Initial configuration and visualization
        ├── caustic_constant_velocity.py
        ├── caustic_acceleration.py
        ├── Lagrange_constant_velocity.py
        ├── Eulerian_constant_velocity.py
        ├── Lagrange_acceleration.py
        ├── Eulerian_acceleration.py
        └── Vizualize_bubble_Eulerian.py


## Program explanations 

. Initial_data.py : 

Ce script simule et visualise les propriétés dynamiques d'une bulle de distorsion d'Alcubierre dans un espace 2D.

Les propriétés étudiées sont :

1. θ (theta)   : Taux d'expansion du champ de vitesse
2. σ² (sigma²) : Cisaillement du champ
3. ω² (omega²) : Vorticité du champ
4. V           : Champ de vitesse dans la direction x

Le tout est visualisé en 3D à l'aide de matplotlib, puis animé dans le temps.


. caustic_constant_velocity.py:

Ce script trace les **trajectoires eulériennes des particules** en fonction du temps sous l'effet d'une bulle en translation à vitesse constante `v_s`.  
Il permet de visualiser l'apparition d'une **caustique**, une zone où les trajectoires se concentrent fortement (divergence du gradient local).

Contexte :
--------------
La position apparente `x(t)` d'une particule initialement à `X` est donnée par :
    x(t) = X + v_s * W(r_s) * (t - t₀)

où `W(r_s)` est une fonction de distorsion centrée autour de `r_s = sqrt(X² + Y²)`.

Paramètres principaux :
---------------------------
- `R = 1`           : Rayon de la bulle
- `σ = 5`           : Paramètre de raideur (contrôle la transition dans `tanh`)
- `v_s = 0.9`       : Vitesse constante de la bulle
- `t₀ = 0.0`        : Temps initial
- `Y = 0.0`         : Coordonnée transverse (on travaille ici sur une coupe Y = 0)

Expression du champ :
--------------------------
La distorsion `W(r_s)` est définie par :
    W(r_s) = (tanh[σ(r_s + R)] - tanh[σ(r_s - R)]) / (2 * tanh[σR])

Fonctionnement :
--------------------
1. Pour un ensemble de valeurs initiales `X`, on trace `x(t)` pour chaque particule.
2. Un **zoom** sur la région de formation de la **caustique** (forte accumulation des trajectoires) est ajouté.

Visualisation :
-------------------
- Le graphe principal affiche les trajectoires dans le plan (x, t).
- Une **zone zoomée** met en évidence la concentration des trajectoires vers `x ≈ 1.2`.
- Les trajectoires sont en noir pour lisibilité, avec certaines étiquetées dans la zone zoomée.


. caustic_acceleration.py

- (In construction)

. Lagrange_constant_velocity.py

Ce script effectue une simulation avancée de la dynamique d’une bulle de distorsion selon le modèle d’Alcubierre.
Il visualise plusieurs grandeurs physiques évolutives en 3D et dans le temps à travers une animation.

Objectif :
-------------
Étudier la structure dynamique de la bulle à travers 6 champs physiques dérivés du champ de vitesse de distorsion.

Variables calculées et visualisées :
---------------------------------------
1. Θ(t, X)    : Taux d'expansion
2. Ω²(t, X)   : Vorticité au carré
3. Σ²(t, X)   : Cisaillement au carré
4. Π²(t, X)   : Quantité d'énergie de distorsion
5. πₓₓ(t, X) : Tenseur d’énergie impulsion (composante xx)
6. Vˣ(t, X)   : Vitesse lagrangienne de la bulle


--------------------------
- R     = 1         → Rayon de la bulle
- σ     = 5         → Raideur de la paroi
- v_s   = 0.9       → Vitesse de la bulle (en unités relativistes)
- G     = 1         → Constante gravitationnelle (unités naturelles)
- t₀    = 0.0       → Temps initial

Grille d’espace :
---------------------

6 sous-graphes 3D affichés côte à côte :

| Graphique     | Description                                  
|---------------|----------------------------------------------
| Θ(t, X)       | Expansion locale                             
| Ω²(t, X)      | Vorticité                                     
| Σ²(t, X)      | Cisaillement                                  
| Π²(t, X)      | Densité d’énergie de la distorsion      
| πₓₓ(t, X)     | Tenseur énergie-impulsion (composante xx)    
| Vˣ(t, X)      | Vitesse lagrangienne (vue co-mouvante)       


- Une animation temporelle montre l’évolution de chaque champ de `t = 0.0` à `t = 0.44`.


. Eulerian_constant_velocity.py

Objectif :
--------------
Ce script simule et visualise l'évolution des champs cinématiques associés à une **bulle de distorsion en mouvement uniforme**,
modélisée selon une version eulérienne du modèle d'Alcubierre avec vitesse constante `v_s`.

Contenu :
-------------
Ce modèle permet de suivre les **champs cinématiques dynamiques** autour de la bulle via des équations dérivées du champ de vitesse.

Paramètres principaux :
---------------------------
- `R = 1.0`        : Rayon caractéristique de la bulle
- `σ = 5.0`        : Raideur de la paroi (commande la pente du champ tanh)
- `v_s = 0.9`      : Vitesse constante de la bulle
- `l = 0`          : Position initiale du centre de la bulle
- `t_0 = 0`        : Temps initial

Champs calculés :
---------------------
1. **θ (theta)**     : Taux d’expansion (∇·v)
2. **σ² (sigma²)**   : Tenseur de cisaillement au carré
3. **ω² (omega²)**   : Vorticité au carré
4. **Vˣ(x,ρ,t)**     : Composante x de la vitesse dans la jauge eulérienne



.Lagrange_acceleration.py



- (In construction)



.Eulerian_acceleration.py



- (In construction)



.Vizualize_bubble_Eulerian.py

Ce script simule la **déformation radiale d'une sphère** initialement parfaite, sous l'effet d'une bulle warp en déplacement **à vitesse constante** `v_s(t) = 0.9`.  
La déformation dépend d’un champ scalaire `W(rₛ)` centré sur la bulle se déplaçant selon `x = l + v_s * t`.

Paramètres :
----------------
- `R = 1.5`    : Rayon de la bulle warp (zone affectée)
- `R0 = 1.0`   : Rayon initial de la sphère
- `σ = 5.0`    : Raideur du champ `W(rₛ)` (définit la transition du `tanh`)
- `v_s(t)`     : Vitesse constante de la bulle warp
- `t₀ = 0`     : Temps initial

Définition du champ :
-------------------------
Pour chaque point `(X, Y, Z)` de la sphère initiale :
1. On estime la distance `rₛ` entre ce point et la position actuelle du centre de la bulle.
2. Le champ de distorsion est donné par :

       W(rₛ) = [tanh(σ(rₛ + R)) - tanh(σ(rₛ - R))] / [2 * tanh(σR)]

3. Le rayon local est modifié selon `R_def = R0 * W(rₛ)`
4. Une sphère déformée est recalculée avec ce rayon variable à chaque instant `t`.



## License

This project is under the MIT license. See the LICENSE file for more details.










#French version
# Programme réalisé dans le cadre d'un stage de Master 2.
Auteur :  Antony Frackowiak
Master 2 de Cosmologie à l'université Claude Bernard Lyon 1. 

Ce projet fait partie d'un stage de Master 2 axé sur la modélisation de la bulle de distorsion d'Alcubierre — un modèle théorique de propulsion supraluminique en relativité générale.

**Alcubierre** 


## Table des matières

- [Installation]
- [Utilisation](
- [Structure du projet]
- [Explications des programmes]
- [License]

## Installation

Assurer vous d'avoir installer ces differentes Packages:
-
-
-
-

Pour installer **Alcubierre**, suivez ces étapes :

1. Clonez le dépôt GitHub :
   
    ```bash
    $ git clone https://github.com/AntonyFrackowiak/Warp_drive.git
    ```
   
2. Allez dans le dossier du package :

    ```bash
    $ cd Alcubierre
    ```
3. Allez dans le dossier du __main__.py
	```bash
    $ cd Program
    ```
## Utilisation

Pour lancer l'un des programme qui correspond à une section particulière, il suffit d'entrer dans un terminal de commande :

	```bash
	$ python .
	```	

Dans le terminal un message s'affichera : 

	```bash
	Choisissez une option :
	1.1 - Section 1.1
	1.2.3 - Section 1.2.3
	2 - Section 2
	Entrez votre choix (1.1, 1.2.3, 2) : 
	```

Il suffit de rentrer la section voulu pour que le programme correspondant s'exécute 
	```bash
	"1.1" ou "1.2.3" ou "2".
	```

## Structure du projet

Ce projet comprend les fichiers suivants :  


📁 Warp_drive/
│
├── README.md
├── LICENCE
│
└──📁 Program/
	│ 
	├──📁 General_warp_drive
	│  	
	└──📁 Alcubierre/
		│	
		├── __main__.py
		├── __init__.py
		│
   		├── Initial_data.py
   		│
   		├── caustic_constant_velocity.py
   		├── caustic_acceleration.py
   		│
   		├── Lagrange_constant_velocity.py
   		├── Eulerian_constant_velocity.py
   		│
   		├── Lagrange_acceleration.py
   		├── Eulerian_acceleration.py
   		│
   		└── Vizualize_bubble_Eulerian.py
   


## Explications des programmes

. Initial_data.py : 

Ce script simule et visualise les propriétés dynamiques d'une bulle de distorsion d'Alcubierre dans un espace 2D.

Les propriétés étudiées sont :

1. θ (theta)   : Taux d'expansion du champ de vitesse
2. σ² (sigma²) : Cisaillement du champ
3. ω² (omega²) : Vorticité du champ
4. V           : Champ de vitesse dans la direction x

Le tout est visualisé en 3D à l'aide de matplotlib, puis animé dans le temps.


. caustic_constant_velocity.py:

Ce script trace les **trajectoires eulériennes des particules** en fonction du temps sous l'effet d'une bulle en translation à vitesse constante `v_s`.  
Il permet de visualiser l'apparition d'une **caustique**, une zone où les trajectoires se concentrent fortement (divergence du gradient local).

Contexte :
--------------
La position apparente `x(t)` d'une particule initialement à `X` est donnée par :
    x(t) = X + v_s * W(r_s) * (t - t₀)

où `W(r_s)` est une fonction de distorsion centrée autour de `r_s = sqrt(X² + Y²)`.

Paramètres principaux :
---------------------------
- `R = 1`           : Rayon de la bulle
- `σ = 5`           : Paramètre de raideur (contrôle la transition dans `tanh`)
- `v_s = 0.9`       : Vitesse constante de la bulle
- `t₀ = 0.0`        : Temps initial
- `Y = 0.0`         : Coordonnée transverse (on travaille ici sur une coupe Y = 0)

Expression du champ :
--------------------------
La distorsion `W(r_s)` est définie par :
    W(r_s) = (tanh[σ(r_s + R)] - tanh[σ(r_s - R)]) / (2 * tanh[σR])

Fonctionnement :
--------------------
1. Pour un ensemble de valeurs initiales `X`, on trace `x(t)` pour chaque particule.
2. Un **zoom** sur la région de formation de la **caustique** (forte accumulation des trajectoires) est ajouté.

Visualisation :
-------------------
- Le graphe principal affiche les trajectoires dans le plan (x, t).
- Une **zone zoomée** met en évidence la concentration des trajectoires vers `x ≈ 1.2`.
- Les trajectoires sont en noir pour lisibilité, avec certaines étiquetées dans la zone zoomée.


. caustic_constant_velocity.py:

-

. caustic_acceleration.py

-

. Lagrange_constant_velocity.py

Ce script effectue une simulation avancée de la dynamique d’une bulle de distorsion selon le modèle d’Alcubierre.
Il visualise plusieurs grandeurs physiques évolutives en 3D et dans le temps à travers une animation.

Objectif :
-------------
Étudier la structure dynamique de la bulle à travers 6 champs physiques dérivés du champ de vitesse de distorsion.

Variables calculées et visualisées :
---------------------------------------
1. Θ(t, X)    : Taux d'expansion
2. Ω²(t, X)   : Vorticité au carré
3. Σ²(t, X)   : Cisaillement au carré
4. Π²(t, X)   : Quantité d'énergie de distorsion
5. πₓₓ(t, X) : Tenseur d’énergie impulsion (composante xx)
6. Vˣ(t, X)   : Vitesse lagrangienne de la bulle


--------------------------
- R     = 1         → Rayon de la bulle
- σ     = 5         → Raideur de la paroi
- v_s   = 0.9       → Vitesse de la bulle (en unités relativistes)
- G     = 1         → Constante gravitationnelle (unités naturelles)
- t₀    = 0.0       → Temps initial

Grille d’espace :
---------------------

6 sous-graphes 3D affichés côte à côte :

| Graphique     | Description                                  
|---------------|----------------------------------------------
| Θ(t, X)       | Expansion locale                             
| Ω²(t, X)      | Vorticité                                     
| Σ²(t, X)      | Cisaillement                                  
| Π²(t, X)      | Densité d’énergie de la distorsion      
| πₓₓ(t, X)     | Tenseur énergie-impulsion (composante xx)    
| Vˣ(t, X)      | Vitesse lagrangienne (vue co-mouvante)       


- Une animation temporelle montre l’évolution de chaque champ de `t = 0.0` à `t = 0.44`.


. Eulerian_constant_velocity.py

Objectif :
--------------
Ce script simule et visualise l'évolution des champs cinématiques associés à une **bulle de distorsion en mouvement uniforme**,
modélisée selon une version eulérienne du modèle d'Alcubierre avec vitesse constante `v_s`.

Contenu :
-------------
Ce modèle permet de suivre les **champs cinématiques dynamiques** autour de la bulle via des équations dérivées du champ de vitesse.

Paramètres principaux :
---------------------------
- `R = 1.0`        : Rayon caractéristique de la bulle
- `σ = 5.0`        : Raideur de la paroi (commande la pente du champ tanh)
- `v_s = 0.9`      : Vitesse constante de la bulle
- `l = 0`          : Position initiale du centre de la bulle
- `t_0 = 0`        : Temps initial

Champs calculés :
---------------------
1. **θ (theta)**     : Taux d’expansion (∇·v)
2. **σ² (sigma²)**   : Tenseur de cisaillement au carré
3. **ω² (omega²)**   : Vorticité au carré
4. **Vˣ(x,ρ,t)**     : Composante x de la vitesse dans la jauge eulérienne


.Lagrange_acceleration.py


- (En construction)


.Eulerian_acceleration.py


- (En construction)


.Vizualize_bubble_Eulerian.py

Ce script simule la **déformation radiale d'une sphère** initialement parfaite, sous l'effet d'une bulle warp en déplacement **à vitesse constante** `v_s(t) = 0.9`.  
La déformation dépend d’un champ scalaire `W(rₛ)` centré sur la bulle se déplaçant selon `x = l + v_s * t`.

Paramètres :
----------------
- `R = 1.5`    : Rayon de la bulle warp (zone affectée)
- `R0 = 1.0`   : Rayon initial de la sphère
- `σ = 5.0`    : Raideur du champ `W(rₛ)` (définit la transition du `tanh`)
- `v_s(t)`     : Vitesse constante de la bulle warp
- `t₀ = 0`     : Temps initial

Définition du champ :
-------------------------
Pour chaque point `(X, Y, Z)` de la sphère initiale :
1. On estime la distance `rₛ` entre ce point et la position actuelle du centre de la bulle.
2. Le champ de distorsion est donné par :

       W(rₛ) = [tanh(σ(rₛ + R)) - tanh(σ(rₛ - R))] / [2 * tanh(σR)]

3. Le rayon local est modifié selon `R_def = R0 * W(rₛ)`
4. Une sphère déformée est recalculée avec ce rayon variable à chaque instant `t`.


## License

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.

