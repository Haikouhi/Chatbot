from Query import *

import nltk
import numpy
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

query = Query()
list_query = []

word_list = ["age", "mail", "prenom", "ville", "adresse", "habite", "date", "naissance", "numero", "telephone", "nom", "astrologique", "signe", "bye", "au revoir", "exit"]
firstname_list = query.firstname_list()


firstname = ""
print("Bonjour ! Je suis Chit-Chat (: ")

Continue = True
while Continue:

    prenom = ""



    sentence = input("Que voulez-vous savoir ?\n")



    tokens = nltk.word_tokenize(sentence)

    for elt in tokens:
        if elt.capitalize() in firstname_list:
            firstname = elt.capitalize()
        if elt.lower() in word_list:
            list_query.append(elt.lower())



    for elt in list_query:
        if elt == "nom":
            query.name(firstname)
        elif elt == "date" or elt == "naissance":
            query.date(firstname)
        elif elt == "ville" or elt == "habite" or elt == "adresse":
            query.city(firstname)
        elif elt == "numero" or elt == "telephone":
            query.number(firstname)
        elif elt == "age":
            query.age(firstname)
        elif elt == "mail":
            query.mail(firstname)
        elif elt == "astrologique" or elt == "signe":
            query.zodiac_sign(firstname)
        elif elt == "bye" or elt == "au revoir" or elt == "exit":
            print("See you soon loser!")
            Continue = False

    if len(list_query) == 0:
        print("Je ne comprends pas la question...")

    list_query = []
