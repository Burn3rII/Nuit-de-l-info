# Projet nuit de l'info

Projet de groupe ENSISA de la nuit de l'info 2023.

## Connexion Github - Pycharm:

Pour utiliser Github avec Pycharm, suivez ces vidéos (dans le nouvel 
affichage Pycharm, le menu en haut à gauche s'obtient en cliquant sur les 4 
barres horizontales en haut à gauche de la fenêtre) :
- https://www.youtube.com/watch?v=cAnWazo5pFU pour connecter un projet 
  Github existant avec votre Pycharm.
- https://www.youtube.com/watch?v=8ZEssR8VTKo pour importer sur Github un 
  projet local que vous avez sur Pycharm

Rmq : une fois le projet lié, soyez bien sûrs d'avoir ajouté un 
interpréteur Python puis installez les packages requis du fichier 
"requirements.txt" si Pycharm ne l'a pas déjà fait. (En ouvrant ce fichier, 
Pycharm vous proposera automatiquement de les installer.)

### Add

Si vous créez un nouveau fichier, qui n'était pas encore sur Github, il 
faut l'ajouter si vous voulez qu'il soit pris en compte dans votre prochain 
push. Pour cela :
1. Clic droit (dans l'arborescence) sur le dossier/fichier à ajouter
2. Clic sur "Git"
3. Clic sur "Add"

### Update project - Commit - Push

Une fois Github lié, un nouveau menu déroulant a dû apparaitre en haut à 
gauche de Pycharm, à côté du nom du projet. Ce menu permet, entre autres, 
de récupérer une copie du projet sur Github (update), de commit et de push.

#### Commit et push

1. Dans le menu à gauche de la fenêtre, sélectionnez les fichiers à commit 
(ceux modifiés et ceux que vous avez ajoutés avec "Add"). 
2. Ajoutez un message dans la section en dessous.
3. Vous pouvez alors "Commit and Push" pour ajouter directement les 
   fichiers sur Github ou "Commit" pour vérifier le commit, faire d'autres 
   modifications etc... et push plus tard.
4. Vous trouverez alors, en cliquant sur l'icône en forme d'embranchement 
   en bas à gauche de Pycharm (à côté de l'icône pour accéder au terminal), 
   une section "git" contenant un historique des pushs déjà effectués et 
   l'éventuel commit en cours.
   Dans le dossier "local" (toujours au même endroit), vous pouvez, si vous 
   n'avez pas déjà push, faire un clic droit et push les changements.

#### Annuler un commit pas encore push

Vous pouvez aussi annuler le commit en faisant un clic droit sur l'élément 
précédent le commit dans l'historique des modifications puis "Reset Current 
Branch To Here" avec l'option "soft".

### Avant un commit

Si vous avez installé une nouvelle dépendance à une bibliothèque sur votre 
machine, pensez à mettre à jour le fichier "requirements.txt" en exécutant 
la commande `pip freeze > ./requirements.txt` au plus haut niveau.

## Éditer README.md

Par défaut, la vue Pycharm permet seulement la lecture des fichiers .md. 
Lorsqu'un fichier .md est ouvert, en haut à droite de la fenêtre se 
trouvent 3 boutons permettant de modifier la vue du fichier (preview seule, 
édition seule, édition + preview à côté)