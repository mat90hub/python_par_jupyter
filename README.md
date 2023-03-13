# python_par_jupyter

<em>
This directory contains French notes taken while learning Python, using the file format ipython (file extension is ipynb). You can read such file either by starting the notebook Jupyter as a server an opening them under your own default browser or under Visual Studio Code, after installation of the jupyter extensions.
</em>

# Apprendre Python en utilisant Jupyter

Ce répertoire contient des notes en français prises en apprenant Python. Elles utilisent le format de fichier `ipython`, qui permet de mélanger du texte enrichi (de formats, mais aussi d’images) avec du code Python directement utilisable et dont les résultats sont immédiatement affichés, qu’ils soient en mode graphique ou non.

Pour lire ces fichiers, il faut avoir installé Python (version 3) sur son ordinateur et le [notebook jupyter](https://jupyter.org/). Ensuite deux méthodes sont possibles pour visualiser localement ces fichiers.

1) on démarre un serveur [notebook Jupyter](https://docs.jupyter.org/en/latest/install/notebook-classic.html) qui permet ensuite d’ouvrir ce fichier pour les visualiser correctement sur votre navigateur par défaut. Le site de [Jupyter](https://docs.jupyter.org/en/latest/install.html#jupyter-notebook-interface) montre les autres serveurs de la même famille qui permettent tous de visualiser et éditer ces cahiers au format `ipynb`.

2) on peut aussi visualiser ces fichiers directement sur [Visual Studio Code](https://code.visualstudio.com/docs/python/environments) en ayant installé les extensions Jupyter qui sont disponibles (voir plus loin). C’est cette dernière solution que j’utilise par défaut.


# Plus de détails sur les installations nécessaires

Vous aurez sûrement téléchargé ce dépôt depuis github. Il faut avoir installé Python3 sur son ordinateur. 

Ensuite, je préconise d’installer un environnement virtuel, pour être sûr que vous ayez les mêmes extensions que celles que j’ai utilisées. Je présente d’abord la méthode générale pour installer un environnement virtuel Python. Mais si comme moi vous utilisez Visual Studio Code, attendez d’arriver jusqu’à la fin de ce chapitre avant de lancer ces commandes, car Visual Studio Code propose sa méthode propre, qui a l’avantage de régler en même temps d’autres problèmes sous-jacents liés à cet éditeur. Donc lisez la méthode générale pour comprendre comment ça marche, mais appliquez la méthode dédiée à Visual Studio Code pour ensuite gagner du temps.

Dans la méthode générale, l’installation se fait dans un shell. L’environnement virtuel se construit avec la commande suivante.

```bash
python3 -m venv .venv
```
(`python3` est le nom supposé de l’exécutable de Python3, ce peut être aussi `python` sur votre installation).

Cette commande installe les exécutables Python sur le sous-répertoire `.venv` (vous pouvez changer le nom de ce répertoire, mais celui-ci sera le nom par défaut qui sera proposé avec la méthode proposée par Visual Studio Code). Quand vous ouvrez un terminal, le ligne de commande devrait normalement commencer par `(.venv)` qui indique que vous êtes bien dans l’environnement virtuel Python.

Vous pouvez ensuite installer toutes les extensions dont vous aurez besoin avec la commande suivante sous cet environnement.

```bash
pip install -r requirements.txt
```

Cette commande va télécharger toutes les extensions utiles.

Sous Visual Studio Code, il faut utiliser les commandes prévues dans l’éditeur pour installer un environnement virtuel. Pour cela on appelle la palette de commande avec les touches `Ctrl-Shift-p` et on entre la phrase `Python: Créer l'environnement` (si sous êtes avec un affichage anglais, il faut l’écrire en anglais). La commande exacte devrait apparaître et vous la sélectionner. Elle propose de créer un environnement virtuel Python. Vous sélectionnerez le programme Python à utiliser (au cas où vous en ayez plusieurs versions localement comme sous Linux ou j’ai encore Python2). Ensuite on vous demande si vous voulez sélectionner le fichier `requirements.txt`, ce qu’il faut faire. Ceci chargera toutes les extensions que j’ai prévues d’utiliser (selon votre configuration et votre connexion internet, cela peut être long). On trouvera ces explications (en anglais) sur [le site de Visual Studio Code](https://code.visualstudio.com/docs/python/environments).



# Contenu rapide

Des répertoires numérotés ont été écrits pour donner un ordre de lecture. Commencez de préférence par le répertoire `01_les_bases`.


# Augmenter les exemples

Si vous ajoutez des exemples qui utilisent d’autres extensions, n’oubliez pas de mettre à jour régulièrement le fichier [requirements.txt](requirements.txt) avec la commande suivante.

```bash
pip freeze > requirements.txt
```


# Imprimer !

Pour imprimer un cahier ou au moins le mettre sous forme de fichier pdf lisible par une autre personne, j’ai retenu deux méthodes possibles.

- enregistrer le fichier sous forme HTML, l’ouvrir dans son navigateur et à partir de là l’imprimer sur une imprimante ou dans un fichier pdf.
- ouvrir le fichier `ipynb` avec le notebook jupyter. Dans mon installation, le lecteur de fichier propose de de lancer le serveur Jupyter pour ouvrir le fichier. Ensuite on peut imprimer directement, sans avoir à passer par un format HTML.

Je n’ai pas réussi à faire fonctionner l’impression directement sous format pdf de puis Visual Studio Code, bien que j’aie bien installé toutes les extensions.


Bonne lecture !
