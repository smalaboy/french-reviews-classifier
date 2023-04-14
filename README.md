# French allocine reviews classifier
 Interface intuitive pour classifier les critiques de film en français
 
 Ce projet présente une interface simple et intuitive pour classifier des critiques de films en français.
 Il a été développé avec Django, JQuery et Bootstrap pour le web.
 Le modèle de classification est un modèle de deep learning développé avec tensorflow et keras. Le code d'entrainement est sur Kaggle: https://www.kaggle.com/moctarsmal/allocine-reviews-classification
 
 ## Installation et exécution
 - Python 3 (>.10 de préférence) doit être installé 
 - Cloner le projet avec *`git clone https://github.com/smalaboy/french-reviews-classifier.git`*
 - Naviguer dans le répertoire du projet
 - Créer un environnement virtuel pour isoler les dépendances: *`python -m venv venv`*
 - Activer l'environnement virtuel
   - Pour windows: *`./venv/Scripts/activate`*
   - Pour linux: *`source ./venv/bin/activate`*
 - Installer les dépendances (django et tensorflow): *`pip install -r requirements.txt`*
 - Lancer le serveur test : *`python manage.py startserver`*
 - Ouvrir l'adresse qui sera indiquée sur la console. Généralement: *127.0.0.1:8000*
 
 ## Fonctionnalités
 - Classifier
 - L'application expose une API json pour la classification. Elle prend un paramètre text dans l'url: 
 Par exemple *127.0.0.1:8000/api/classify?text=Ce+film+est+magnifique*


## Images
![Critique positive](https://drive.google.com/file/d/1MIwJzYgFy_m-mBqnerNpfs4JmwvTUDz2/view?usp=sharing)
