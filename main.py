from Query import * #pour importer la class Query qui gère toutes les requêtes
import discord # pour pvr utiliser les fonct. de Discord
from random import randint # pour tirer certaines phrases de façons aléatoire

import nltk # librairie qui permet de couper les phrases avec des tokens

#nltk.download('punkt') # les packages à installer lors du lancement initial du programme
#nltk.download('maxent_ne_chunker') # les packages à installer lors du lancement initial du programme
#nltk.download('words') # les packages à installer lors du lancement initial du programme

token = "NTcwNjY4NzMwNDc3MTgyOTc5.XMF6jA.kdH4AsJhL7VNrM6C_JuKcKJ6AFI" # clef d'identif' pour notre bot

client = discord.Client() # initialise Discord

query = Query() # créer un objet de notre class Query qui nosu permetd e faire toutes les requêtes

# liste de tous les noms que le bot doit reconnaître dans les phrases/questions
word_list = ["gueule", "bonjour", "hey", "hi", "yo", "salut", "age", "mail", "prenom", "ville", "adresse",
             "l'adresse", "habite", "naissance", "numero", "telephone", "nom", "astrologique", "signe",
             "bye", "au revoir", "exit", "va", "ça", "ca", "vas", "comment"] 
firstname_list = query.firstname_list() # on recupère la liste des prenoms dans une liste

# réponses aléatoir (voir random)
possible_response = ["Bien sur que non", "Je ne pense pas ", "No!",
                     "Arrete de poser des questions", "Qu'est-ce que j'en sais moi ?",
                     "Je suis ton père","Arrete de dire des conneries stp", "Tu sors ou je te sors?", 
                     "C'est qui la patronne?", "Nope", "Demandes à PL", "Demandes à Sumenia", "Plaît-il",
                     "pffffff", ":confused:", ":snake:", ":eye:", ":octopus:"
                     ]



@client.event # gestion des évènements dans Discord
async  def on_message(message): # l'évèn est celui d'un utilis. qui écrit un message
    if message.author != client.user: # pour éviter que le bot se réponde à lui-même 
        sentence = message.content # initialise sentence qui est le contenu du message envoyé

        list_query = [] # initialisation de la liste des requêtes que l'on va effectuer 
        firstname = "" # init vide pour les demandes de prenoms non connu par la db
        answer = "" # init le message que le bot va envoyer



        tokens = nltk.word_tokenize(sentence) # permet de recupérer la réponse en tokens (mot par mot)

        for elt in tokens: # parcourir tous les tokens 
            if elt.capitalize() in firstname_list: # si l'un des tokens est un prenom dans la liste des prenoms....
                firstname = elt.capitalize() # le prenom devient cet élèment
            if elt.lower() in word_list: # si un des tokens dans la liste des mots...
                list_query.append(elt.lower()) # on l'ajoute dans la liste des requêtes à effectuer




        for elt in list_query: # on parcourt ttes les requ effectuées (les if...)
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


        if len(list_query) == 0: # si liste des Query = 0...

            index_response_picked = randint(0,len(possible_response) - 1) # on tire au sort un index entre 0 et nombre-1...
            response = possible_response[index_response_picked] # réponse choisie...
            answer += response # et ajoutée ! 

        list_query = [] # on reinit la liste de Query à 0 car sinon les premieres req vont être répétées avec les nouvelles 

        await message.channel.send(answer) # envoie le message sur Discord

client.run(token) 


