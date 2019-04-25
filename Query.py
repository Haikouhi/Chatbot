import pymysql
import datetime

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


    def firstname_list(self):

        list = []

        sql = "SELECT firstname FROM class"
        self.curseur.execute(sql)
        data = self.curseur.fetchall()
        for person in data:
            list.append(person["firstname"])

        return list


    def name(self, firstname):


        if firstname != "":
            sql = "SELECT lastname, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            if output["gender"] == "M":
                print("Son nom est " + output["lastname"])
            else:
                print("Son nom est " + output["lastname"])
        else:
            print("Huuum, je ne connais pas cette personne ! ")

# defining birthdate for any chosen name: 
    def date(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            if output["gender"] == "M":
                print("Il est né le " + str(output["birthdate"]))
            else:
                print("Elle est née le" + str(output["birthdate"]))
        else:
            print("Huuum, je ne connais pas cette personne ! ")


# defining city for any chosen name:
    def city(self, firstname):

        if firstname != "":
            sql = "SELECT city, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            if output["gender"] == "M":
                print("Il habite à " + str(output["city"]))
            else:
                print("Elle habite à " + str(output["city"]))
        else: 
            print("Huuum, je ne connais pas cette personne ! ")


# defining phone number for any chosen name:
    def number(self, firstname):

        if firstname != "":
            sql = "SELECT phone_number, gender FROM class WHERE firstname ='{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            if output["gender"] == "M":
                print("Son numéro de téléphone est +33" + str(output["phone_number"]))
            else:
                print("Son numéro de téléphone est +33" + str(output["phone_number"]))

        else:
            print("Huuum, je ne connais pas cette personne ! ")

    def age(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            date = output["birthdate"]

            now = datetime.datetime.now()

            if date.month <= now.month:
                if date.day <= now.day:
                    person_age = now.year - date.year
            else:
                person_age = now.year - date.year - 1

            if output["gender"] == "M":
                print("Il a {} ans".format(person_age))
            else:
                print("Elle a {} ans".format(person_age))

        else:
            print("Huuum, je ne connais pas cette personne !")

    def mail(self, firstname):

        if firstname != "":
            sql = "SELECT email, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            if output["gender"] == "M":
                print("Son adresse email est " + str(output["email"]))
            else:
                print("Son adresse email est " + str(output["email"]))
        else:
            print("Huuum, je ne connais pas cette personne !")

    def zodiac_sign(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            date = output["birthdate"]

            if (date.month == 3 and date.day >= 21) or (date.month == 4 and date.day <= 19):
                sign = "Belier"
            elif (date.month == 4 and date.day >= 20) or (date.month == 5 and date.day <= 20):
                sign = "Taureau"
            elif (date.month == 5 and date.day >= 21) or (date.month == 6 and date.day <= 20):
                sign = "Gemeaux"
            elif (date.month == 6 and date.day >= 21) or (date.month == 7 and date.day <= 22):
                sign = "Cancer"
            elif (date.month == 7 and date.day >= 23) or (date.month == 8 and date.day <= 23):
                sign = "Lion"
            elif (date.month == 8 and date.day >= 24) or (date.month == 9 and date.day <= 22):
                sign = "Vierge"
            elif (date.month == 9 and date.day >= 23) or (date.month == 10 and date.day <= 22):
                sign = "Balance"
            elif (date.month == 10 and date.day >= 23) or (date.month == 11 and date.day <= 21):
                sign = "Scorpion"
            elif (date.month == 11 and date.day >= 22) or (date.month == 12 and date.day <= 21):
                sign = "Sagittaire"
            elif (date.month == 12 and date.day >= 22) or (date.month == 1 and date.day <= 19):
                sign = "Capricorne"
            elif (date.month == 1 and date.day >= 20) or (date.month == 2 and date.day <= 19):
                sign = "Verseau"
            else:
                sign = "Poisson"

            if output["gender"] == "M":
                print("Il est " + sign)
            else:
                print("Elle est " + sign)

        else:
            print("Huuum, je ne connais pas cette personne ! ")
