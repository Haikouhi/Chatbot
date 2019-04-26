from Query import *
import discord
from random import randint

import nltk

#nltk.download('punkt')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

token = "NTcwNjY4NzMwNDc3MTgyOTc5.XMF6jA.kdH4AsJhL7VNrM6C_JuKcKJ6AFI"

client = discord.Client()

query = Query()
list_query = []

word_list = ["gueule", "bonjour", "hey", "hi", "yo", "salut", "age", "mail", "prenom", "ville", "adresse",
             "l'adresse", "habite", "naissance", "numero", "telephone", "nom", "astrologique", "signe",
             "bye", "au revoir", "exit", "va", "ça", "ca", "vas", "comment"]
firstname_list = query.firstname_list()
possible_response = ["Bien sur que non", "Je ne pense pas ", "No!",
                     "Arrete de poser des questions", "Qu'est-ce que j'en sais moi ?",
                     "Je suis ton père","Arrete de dire des conneries stp", "Tu sors ou je te sors?", 
                     "C'est qui la patronne?", "Nope", "Demandes à PL", "Demandes à Sumenia", "Plaît-il",
                     "pffffff", ":confused:", ":snake:", ":eye:", ":octopus:"
                     ]


firstname = ""

@client.event
async  def on_message(message):
    if message.author != client.user:
        sentence = message.content

        list_query = []
        firstname = ""
        answer = ""



        tokens = nltk.word_tokenize(sentence)

        for elt in tokens:
            if elt.capitalize() in firstname_list:
                firstname = elt.capitalize()
            if elt.lower() in word_list:
                list_query.append(elt.lower())




        for elt in list_query:
            if elt == "nom":
                answer += query.name(firstname) + '\n'
            elif elt == "naissance":
                answer += query.date(firstname) + '\n'
            elif elt == "ville" or elt == "habite" or elt == "adresse" or elt == "l'adresse":
                answer += query.city(firstname) +'\n'
            elif elt == "numero" or elt == "telephone":
                answer += query.number(firstname) + '\n'
            elif elt == "age":
                answer += query.age(firstname) + '\n'
            elif elt == "mail":
                answer += query.mail(firstname) + '\n'
            elif elt == "astrologique" or elt == "signe":
                answer += query.zodiac_sign(firstname) + '\n'
            elif elt == "bye" or elt == "au revoir" or elt == "exit":
                answer += "See you soon loser!"
            elif elt == "bonjour" or elt == "hey" or elt == "yo" or elt == "salut" or elt == "hi":
                answer += "Bonjour ! Je suis Chit-Chat (: "
            elif elt == "gueule":
                if firstname != "":
                    if firstname == "Theo" or firstname == "Timothée":
                        answer += "Non, j'ai trop de respect pour lui, c'est l'un de mes créateurs"
                    elif firstname == "Caroline" or firstname == "Haikouhi":
                        answer += "Non, j'ai trop de respect pour elle, c'est l'une de mes créatrices"
                    else:
                        answer += "Ta gueule {}".format(firstname)
            elif elt == "va" or elt == "vas":
                if "ca" in list_query or "ça" in list_query or "comment" in list_query:
                    answer += "Je pète la forme"


        if len(list_query) == 0:

            index_response_picked = randint(0,len(possible_response) - 1)
            response = possible_response[index_response_picked]
            answer += response

        list_query = []

        await message.channel.send(answer)

client.run(token)


