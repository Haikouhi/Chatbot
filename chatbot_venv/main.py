from Query import *

import nltk
import numpy
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

query = Query()
list_query = []

word_list = ["age", "mail", "name", "city", "birthdate", "number", "lastname", "zodiac", "bye", "goodbye", "exit"]
firstname_list = query.firstname_list()


firstname = ""
print("Hi there, I'm Chit-Chat, let me know if you need my help !")

Continue = True
while Continue:

    firstname = ""



    sentence = input("What would you like to know ?\n")



    tokens = nltk.word_tokenize(sentence)

    for elt in tokens:
        if elt.capitalize() in firstname_list:
            firstname = elt.capitalize()
        if elt.lower() in word_list:
            list_query.append(elt.lower())



    for elt in list_query:
        if elt == "lastname":
            query.name(firstname)
        elif elt == "birthdate":
            query.date(firstname)
        elif elt == "city":
            query.city(firstname)
        elif elt == "number":
            query.number(firstname)
        elif elt == "age":
            query.age(firstname)
        elif elt == "mail":
            query.mail(firstname)
        elif elt == "zodiac":
            query.zodiac_sign(firstname)
        elif elt == "bye" or elt == "goodbye" or elt == "exit":
            print("See you soon loser!")
            Continue = False

    if len(list_query) == 0:
        print("I don't understand your question...")

    for elt in list_query:
        list_query.remove(elt)

