# Report 1

## Id: #1

**Title:** UnboundLocalError lors de l'execution

**Version:** 4a261044

**Category:** Plantage

**Priority:** 1

**Description:** Lors de l'execution de cette commande "python renommage_series.py series_2000-2019.txt --memoisation=default titles bonjour", une UnboundLocalError est throw.

StackTrace:
```
Traceback (most recent call last):
  File "renommage_series.py", line 236, in <module>
    main()
  File "renommage_series.py", line 227, in main
    print(title + " --> " + closer_mem(title, series, mem))
  File "renommage_series.py", line 106, in closer_mem
    tmpDist = distance2(string1, p, mem_dict)
UnboundLocalError: local variable 'mem_dict' referenced before assignment
```

-------------------------------------------------------------------------------

## Id: #2

**Title:** Erreur dans la lecture des options ou dans la documentation

**Version:** 4a261044

**Category:** Expérience utilisateur

**Priority:** 1

**Description:** Lors de l'exécution de cette commande "python renommage_series.py series_2000-2019.txt Titles bonjour", le programme a affiché 
```
INFO: No test launched
Illegal memoisation argument, run 'python renommage_series.py -h' for help
```
alors que lorsque je lance la commande avec l'option "-h", les seules arguments obligatoires sont "Path  Titles"

-------------------------------------------------------------------------------

## Id: #3

**Title:** Erreur dans la lecture des options ou dans la documentation - 2

**Version:** 4a261044

**Category:** Expérience utilisateur

**Priority:** 1

**Description:** Lors de l'exécution de cette commande "python renommage_series.py series_2000-2019.txt --titles bonjour", le programme affiche la manière d'utiliser le programme et un ligne d'erreur indiquant que l'option "--titles" est inconnu :
```
usage: renommage_series.py [-h] [--memoisation Memoisation]
                           [--test test index]
                           [--memo-file path to memoisation file]
                           [--question question]
                           Path Titles [Titles ...]
renommage_series.py: error: unrecognized arguments: --titles
```

Alors que lors de l'utilisation de la commande "-h", il est indiqué qu'il faut utiliser le programme de cette manière 'python renommage_series.py --titles "something"..."'

-------------------------------------------------------------------------------

## Id: #4

**Title:** Affichage INFO: No test launched

**Version:** 4a261044

**Category:** Expérience Utilisateur

**Priority:** 4

**Description:** Lors du lancement du programme de cette manière par exemple "", cette ligne est affiché avant le résultat "INFO: No test launched" alors que le fait de lancer des tests n'est pas vraiment le but principal du programme.

-------------------------------------------------------------------------------

## Id: #5

**Title:** Chargement infini

**Version:** 4a261044

**Category:** Plantage

**Priority:** 3

**Description:** Lors de l'exécution du programme avec "--memoisation none" et un mot de plus de 3 caractères exemple : "python renommage_series.py series_2000-2019.txt --memoisation none aaaa", le programme n'affiche aucun résultat (même après plusieurs minutes d'exécution)

-------------------------------------------------------------------------------

## Id: #6

**Title:** Nom des valeurs de options en anglais

**Version:** 4a261044

**Category:** Fonctionnalité

**Priority:** 4

**Description:** Le nom des valeurs des options sont en anglais alors qu'ils sont en francais dans l'énoncé

-------------------------------------------------------------------------------

## Id: #6

**Title:** Typo dans la documentation

**Version:** 4a261044

**Category:** Expérience Utilisateur

**Priority:** 2

**Description:** Il y a plusieurs typos dans le texte affiché par l'option "-h" :
```
usage: renommage_series.py [-h] [--memoisation Memoisation]       Memoisation peut être remplacé par memoisation_mode
                           [--test test index]                      Les mots test et index sont séparés par espace ce qui 
                                                                    peut préter à confusion (à remplacer par un '_') 
                           [--memo-file path to memoisation file]   Même remarque
                           [--question question]
                           Path Titles [Titles ...]                 Les mots path et tiles devrait être mis en minuscule
                                                                    et "Titles [Titles ...]" par "titles..." car cela donne 
                                                                    l'impression qu'il faut utiliser le programme de cette manière
                                                                    "python renommage_series.py path.txt
                           

Find closest title

positional arguments:
  Path                  Absolute path to the file you want to test
  Titles                List of titles you want to find.ex: python
                        renommage_series.py --titles "something"...

optional arguments:
  -h, --help            show this help message and exit
  --memoisation Memoisation
                        Set memoisation (--memoisation none,i --memoisation
                        by_target, by_arg --memoisation default, --memoisation
                        global)
  --test test index     --test 0 launches a basic test--test 1 launches.. TBA
  --memo-file path to memoisation file
                        --memo-file ./<file_name>
  --question question   --question 7a | 7b

```

-------------------------------------------------------------------------------

## Identifiant: #7

**Titre**: Défauts méthode closer()

**Version concernée**:  4a261044

**Catégorie**: Qualité du code

**Priorité**: 3

**Description**: La méthode closer (qui n'est pas utilisé dans le code ce qui peut être la source de #5) à plusieurs défaut.

Elle ne vérifie pas la taille de possibilities (pas un problème si la taille est 0, elle reverra None de toute manière. Par contre si la taille est 1 on peut directement renvoyer le seul élément de possibilities).

Ensuite concernant les variables word et dist. Je ne pense pas que leurs donner None comme valeur par défaut est une bonne idée (par exemple pour dist tu est obligé à cause de ca de faire un if (dist is none) à chaque boucle du for). Tu pourrais plutôt leurs donner comme valeur le premier element de possibilities (possibilities[0]) et faire ta boucle for sur possibilities[1:].

-------------------------------------------------------------------------------

## Identifiant: #7

**Titre**: mem_dict comme argument

**Version concernée**:  4a261044

**Catégorie**: Qualité du code

**Priorité**: 4

Description: Tu utilise mem_dict comme une variable que tu passe en argument dans la méthode distance2 ce qui peut peut-être être lourd en cas d'appel récursif avec un mem_dict très remplie. Il serait peut-être plus jusdicieux d'en faire une variable globale étant donné qu'il est utilisé dans plusieurs fonction du programme (cette remarque est plus une question qu'un conseil/défaut observé).

-------------------------------------------------------------------------------

## Identifiant: #8

**Titre**: Enlever les TODO

**Version concernée**:  4a261044

**Catégorie**: Qualité du code

**Priorité**: 4

**Description**: Il faudrais soit supprimer les TODO (par exemple concernant la doc), soit le faire. Laissé de cette manière, ils donnent l'impression d'un brouillon pas terminé.

-------------------------------------------------------------------------------

## Identifiant: #9

**Titre**: Ecrire plus de fonction plutôt que de vérifier les arguments

**Version concernée**:  4a261044

**Catégorie**: Qualité du code

**Priorité**: 2

**Description**: Je pense que dans la fonction closer_mem(), il serait plus judicieux et efficace au niveau du programme de séparer cette méthode en une méthode pour chaque mode de mémoisation, ca rendra le code plus efficace (pas besoin de faire de if à chaque loop du for), plus lisible (chaque méthode sera plus courte) et plus facile à maintenir (une nouvelle option = une nouvelle méthode). Ce n'est que mon point de vue, cet élément peut-être discuté.