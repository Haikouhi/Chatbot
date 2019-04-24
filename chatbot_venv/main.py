from Query import *

import nltk
import numpy
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

query = Query()
list_query = []

word_list = ["age", "mail", "name", "city", "birthdate", "number", "lastname", "zodiac"]
firstname_list = query.firstname_list()

firstname = ""


sentence = input("WHat would you like to know ?\n")



tokens = nltk.word_tokenize(sentence)

for elt in tokens:
    if elt in firstname_list:
        firstname = elt
    if elt in word_list:
        list_query.append(elt)



for elt in list_query:
    if elt == "lastname":
        query.name(firstname.capitalize())
    elif elt == "birthdate":
        query.date(firstname.capitalize())
    elif elt == "age":
        query.age(firstname.capitalize())
    elif elt == "mail":
        query.mail(firstname.capitalize())
    elif elt == "zodiac":
        query.zodiac_sign(firstname)

