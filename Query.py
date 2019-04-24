import pymysql

class Query():

    def __init__(self):

        self.connexion = pymysql.connect(host='localhost',
                                    user='foobar',
                                    password='foobar',
                                    db='chit_chat',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        self.curseur = self.connexion.cursor()


    def liste_prenom(self):

        liste = []

        sql = "SELECT firstname FROM class"
        self.curseur.execute(sql)
        data = self.curseur.fetchall()
        for person in data:
            liste.append(person["firstname"])

        return liste


    def nom(self, prenom):


        if prenom != "":
            sql = "SELECT lastname FROM class WHERE firstname = '{}'".format(prenom)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("Son nom est " + output["lastname"])
        else:
            print("Je ne connais pas cette personne")

    def date(self, prenom):


        if prenom != "":
            sql = "SELECT birthdate FROM class WHERE firstname = '{}'".format(prenom)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("Sa date de naissance est " + str(output["birthdate"]))
        else:
            print("Je ne connais pas cette personne")
