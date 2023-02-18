# python_par_jupyter

<em>
This directory contains French notes taken while learning Python, using the file format ipython (file extension is ipynb). You can read such file either by starting the notebook Jupyter as a server an opening them under your own default browser or under Visual Studio Code, after installation of the jupyter extensions.
</em>

# Apprendre Python en utilisant Jupyter

Ce répertoire contient de notes en français prises en apprenant Python, écrites en utilisant le format de fichier `ipython`. Pour lire ces fichiers, il faut démarrer un serveur  **notebook Jupyter** puis en les ouvrir sur votre navigateur. En installant les extensions **Jupyter** dans **Visual Studio Code**, on peut aussi les lire directement sous cet éditeur.

Ce format permet de tester et de vérifier que les lignes de code Python fonctionnent bien sur votre ordinateur.


# Installation

Vous aurez sûrement téléchargé ce dépôt depuis github. Il faut avoir installé Python3 sur son ordinateur et ensuite, ce dépôt propose d'installer un environnement virtuel.

En vous plaçant sur ce répertoire dans un shell, vous pouvez re-créer l'environnement virtuel avec la commande suivante.

```bash
python3 -m venv .venv
```
(`python3` est le nom supposé de l'exécutable de Python3, ce peut être aussi `python` sur votre installation).

Cette commande installe les exécutables Python sur le sous-répertoire `.venv`. Quand vous ouvrez un terminal, le ligne de commande devrait normalement commencer par `(.venv)` qui indique que vous êtes bien dans l'environnement virtuel Python.

Vous pouvez ensuite installer toutes les extensions dont vous aurez besoin avec la commande suivante sous cet environnement.

```bash
pip install -r requirements.txt
```

# Contenu rapide

Des répertoires numérotés ont été écrits pour donner un ordre de lecture. Commencez de préférence par le répertoire `01_les_bases`.


Bonne lecture !
