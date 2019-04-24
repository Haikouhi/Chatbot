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

        sql = "SELECT prenom FROM eleves"
        self.curseur.execute(sql)
        data = self.curseur.fetchall()
        for person in data:
            liste.append(person["prenom"])

        return liste


    def nom(self, prenom):


        if prenom != "":
            sql = "SELECT nom FROM eleves WHERE prenom = '{}'".format(prenom)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("Son nom est " + output["nom"])
        else:
            print("Je ne connais pas cette personne")

    def date(self, prenom):


        if prenom != "":
            sql = "SELECT date_de_naissance FROM eleves WHERE prenom = '{}'".format(prenom)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("Sa date de naissance est " + str(output["date_de_naissance"]))
        else:
            print("Je ne connais pas cette personne")
