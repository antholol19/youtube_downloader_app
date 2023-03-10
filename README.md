# Application pour télécharger des séquences audio sur youtube

## Fonctionnement
L'utilisateur a accès une application web (pas encore accessible au public). Cet API donne l'option à l'utilisateur d'entrer le lien url d'une video youtube. Il peut aussi entrer la séquence audio en secondes qu'il souhaite récupéré (à faire bientôt). Ces paramètres sont ensuite récupérés par Flask et traités en Python qui va s'occuper de télécharger l'audio de la video.

## Technologies
Ce projet utilise les technologies suivantes:
* Python 3.7 et plus
* Flask 2.0 et plus

## Liens pour ces technologies
Pour en connaître davantage sur ces technologies, voici leurs liens
* Python: <a href="url">https://www.python.org/</a>
* Flask: <a href="url">https://flask.palletsprojects.com/en/2.2.x/</a>

## Libraires Python utilisées
Les librairies nécessaires pour Python:
* pytube 12.1.2
* moviepy 1.0.3

## Installation
Voici comment installer ce projet
1. Cloner ce projet
2. Créer un environnement virtuel pour ce projet et activer l'environnement:
2. Vérifier que la version 3.7 ou plus de Python soit installée: `$ python --version`
3. Installer Flask avec pip: `$ pip install Flask`
4. Vérifier que la version 2.0 ou plus de Flask soit installée: `$ flask --version`
5. Installer les librairies Python requises:
  * `$ pip install pytube`
  * `$ pip install moviepy`
<hr>
