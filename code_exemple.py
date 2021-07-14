

# usage du dictionnaire

# il faut avoir préalablement récupéré des informations
# et les avoir stockés dans des variables

reference = '15698H8963'
titre = "Le petit prince"
auteur = "Antoine de St Exupery"

# création d'un dictionnaire vide

livres = dict()

# ici on prend pour clé une référence unique (un code ISBN, n'importe quoi d'unique et de pas trop long)
# et on y associe une valeur qui sera la liste de toutes les caractèristiques du livre
# cette liste peut être construite directement dans le dictionnaire
# je te conseille d'adopter cette structure de données pour le projet 2
livres[reference] = [titre, auteur]

# pour acceder au titre du livre
livres[reference][0]

# pour acceder au nom de l'auteur
livres[reference][1]

# pour écrire le contenu du dictionnaire dans un fichier
# on pourrait faire le même type d'opération avec une liste ou n'importe quel conteneur
# mais le dictionnaire est la structure la plus appropriée dès lors que l'on veut stocké des groupes d'informations comme c'est le cas ici
with open("fichier.csv", "w"):
	for toutes_les_refs in livres:
		print("{}, {}".format(livres[reference][0], livres[reference][1])


