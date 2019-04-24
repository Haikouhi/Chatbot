from Query import *

import nltk
import numpy
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

query = Query()
list_query = []

liste_mot = ["age", "mail", "lastname", "city", "date", "phone"]
liste_firstname = query.liste_firstname()

prenom = ""


sentence = input("Que voulez vous savoir ?\n")



tokens = nltk.word_tokenize(sentence)

for elt in tokens:
    if elt in liste_fristname:
        prenom = elt
    if elt in liste_mot:
        list_query.append(elt)



for elt in list_query:
    if elt == "nom":
        query.nom(prenom.capitalize())
    elif elt == "date":
        query.date(prenom.capitalize())

