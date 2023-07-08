# Documentation du système de gestion de produits

Ce système de gestion de produits vous permet de gérer les produits périssables et non périssables.

## Installation

Pour installer le système de gestion de produits, suivez les étapes suivantes :

1. Clonez le repository du projet depuis [GitHub](lien bientot disponible ici).
2. Assurez-vous d'avoir Python 3 installé sur votre système.
3. Naviguez vers le dossier racine du projet.
4. Exécutez la commande suivante pour installer les dépendances :
   pip install -r requirements.txt
5. Vous êtes prêt à utiliser le système de gestion de produits !

## Utilisation

Le système de gestion de produits offre les fonctionnalités suivantes :

1. Ajouter un produit
2. Supprimer un produit
3. Mettre à jour la quantité d'un produit
4. Afficher tous les produits
5. Afficher les produits qui expirent dans les 30 jours
6. Rechercher un produit
7. Afficher les operations

Pour utiliser ces fonctionnalités, exécutez le fichier `main.py` depuis la ligne de commande :
python main.py

Suivez ensuite les instructions affichées à l'écran pour sélectionner les actions à effectuer.

## Structure du code source

Le code source est organisé comme suit :

'main.py': Point d'entrée du programme.
'produit.py': Contient la classe 'Product' pour représenter un produit.
'perishable.py': Contient la classe `Perishable` pour gérer les produits périssables.
'non_perishable.py': Contient la classe 'NonPerishable' pour gérer les produits non périssables.
'stackop.py': Contient les classes 'ProductManagement', `Operation` et 'StackOperations' pour gérer les opérations sur les produits.

## Contributions

Les contributions à ce projet sont les bienvenues. Si vous souhaitez apporter des améliorations ou signaler des problèmes, veuillez créer une issue sur [GitHub](lien bientot disponible ici).

## License

Ce projet est sous license MIT. Veuillez consulter le fichier `LICENSE` pour plus d'informations.
