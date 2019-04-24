from Query import *

import nltk
import numpy
nltk.download('maxent_ne_chunker')
nltk.download('words')

query = Query()
list_query = []

liste_mot = ["age", "mail", "nom", "adresse", "date", "numero"]
liste_prenom = query.liste_prenom()

prenom = ""


sentence = input("Que voulez vous savoir ?\n")



tokens = nltk.word_tokenize(sentence)

for elt in tokens:
    if elt in liste_prenom:
        prenom = elt
    if elt in liste_mot:
        list_query.append(elt)



for elt in list_query:
    if elt == "nom":
        query.nom(prenom.capitalize())
    elif elt == "date":
        query.date(prenom.capitalize())

