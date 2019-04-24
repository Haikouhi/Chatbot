from Query import *

import nltk
import numpy
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

query = Query()
list_query = []

word_list = ["age", "mail", "name", "city", "birthdate", "number", "lastname"]
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
    if elt == "name":
        query.name(firstname.capitalize())
    elif elt == "birthdate":
        query.date(firstname.capitalize())

