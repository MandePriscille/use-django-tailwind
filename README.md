# use-django-tailwind
used django-tailwind dans un project Django


# Guide d'Installation et d'Utilisation de Django avec Tailwind CSS

## 1. Prérequis

Assurez-vous que vous avez installé les prérequis suivants :

- Python 3.x
- Node.js (version 16.x ou supérieure)
- npm (ou yarn) installé globalement
- Django installé

## 2. Installation de `django-tailwind`

1. Installez `django-tailwind` avec pip :
	
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   ```bash
   python -m pip install django-tailwind
   ```

2. Ajoutez `tailwind` à la liste des applications installées dans `settings.py` de votre projet Django :
   
   ```python
   INSTALLED_APPS = [
       ...
       'tailwind',
       'theme',  # Cette ligne sera ajoutée plus tard
   ]
   ```

## 3. Initialisation de l'App `theme` (tailwind)

1. Initialisez l'application `theme` où Tailwind sera configuré :
   
   ```bash
   python manage.py tailwind init theme
   ```
   
   Cela va créer une application Django nommée **`theme`**. Elle contient tous les fichiers nécessaires pour intégrer Tailwind CSS dans votre projet.

## 4. Configuration de Tailwind dans `settings.py`

1. Dans le fichier `settings.py`, ajoutez la configuration suivante :
   
   ```python
   # Spécifie le nom de l'application contenant Tailwind
   TAILWIND_APP_NAME = 'theme'
   
   # Ajoutez aussi les adresses IP internes pour le rechargement automatique (optionnel)
   INTERNAL_IPS = ["127.0.0.1"]
   ```

2. Assurez-vous que **`theme`** est bien dans les `INSTALLED_APPS` de votre projet :
   
   ```python
   INSTALLED_APPS = [
       ...
       'theme',   # L'application Django qui contient Tailwind
       'tailwind',
   ]
   ```

## 5. Installer les dépendances NPM

1. Allez dans le dossier de l'application `theme` :
   
   ```bash
   cd theme
   ```

2. Installez les dépendances NPM (celles nécessaires pour Tailwind) :
   
   ```bash
   npm install
   ```

## 6. Démarrer le serveur Tailwind

1. Lancez la compilation de Tailwind en mode développement avec la commande suivante :
   
   ```bash
   python manage.py tailwind start
   ```
   
   Cette commande va démarrer le processus de compilation et de surveillance des changements dans les fichiers Tailwind. Le fichier CSS compilé sera stocké dans `theme/static/css/dist/styles.css`.

## 7. Configurer les Templates

1. Modifiez le fichier `settings.py` pour ajouter le répertoire `templates` de l'application `theme` :
   
   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'theme/templates')],  # Ajoutez ce chemin
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   ...
               ],
           },
       },
   ]
   ```

2. Dans le dossier `theme/templates/`, créez un fichier `base.html` qui servira de base pour vos autres templates :
   
   ```html
   {% load static %}
   
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Mon Projet Django avec Tailwind</title>
       <link rel="stylesheet" href="{% static 'css/dist/styles.css' %}">
   </head>
   <body class="bg-gray-100 text-gray-800">
       <header class="bg-blue-500 p-4">
           <h1 class="text-white text-3xl">Bienvenue dans mon projet Django avec Tailwind CSS</h1>
       </header>
   
       <main class="p-8">
           {% block content %}
           {% endblock %}
       </main>
   </body>
   </html>
   ```

## 8. Créer un Template Exemple

1. Créez un fichier `home.html` dans le dossier `theme/templates/` :
   
   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <div class="text-center mt-8">
       <p class="text-2xl text-blue-500 font-bold">Bienvenue sur la page d'accueil, propulsée par Django et Tailwind !</p>
   </div>
   {% endblock %}
   ```

## 9. Lancer le Serveur Django

1. Dans le dossier de votre projet, lancez le serveur Django :
   
   ```bash
   python manage.py runserver
   ```

2. Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/` pour voir la page d'accueil stylisée avec Tailwind CSS.

## 10. Résumé des Dossiers

Voici un récapitulatif de la structure des dossiers :

```
myproject/
├── manage.py
├── myproject/                  # Dossier du projet Django
│   ├── settings.py
│   └── ...
├── theme/                      # L'application Django pour Tailwind
│   ├── static/                 # Contient le CSS généré
│   │   └── css/
│   │       └── dist/
│   │           └── styles.css  # Fichier CSS généré par Tailwind
│   ├── static_src/             # Fichiers source de Tailwind
│   │   └── styles.css
│   │   └── tailwind.config.js
│   ├── templates/              # Dossier des templates Django
│   │   ├── base.html           # Template de base
│   │   └── home.html           # Exemple de template
│   └── apps.py
└── ...
```

## 11. Autres Commandes Utiles

- **Compiler Tailwind en mode production** :
  
  ```bash
  python manage.py tailwind build
  ```

- **Recompiler Tailwind lorsque vous apportez des modifications au fichier `styles.css`** :
  
  ```bash
  python manage.py tailwind start
  ```