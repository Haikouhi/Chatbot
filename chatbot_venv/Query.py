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
            sql = "SELECT lastname FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("His/Her name is " + output["lastname"])
        else:
            print("Huuum, I don't know this person ! ")

    def date(self, firstname):


        if firstname != "":
            sql = "SELECT birthdate FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("His/Her birthdate is " + str(output["birthdate"]))
        else:
            print("Huuum, I don't know this person ! ")

    def age(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            date = output["birthdate"]

            now = datetime.datetime.now()

            if date.month <= now.month:
                if date.day <= now.day:
                    person_age = now.year - date.year
            else:
                person_age = now.year - date.year - 1

            print("He/She is {} years old".format(person_age))

        else:
            print("Huuum, I don't know this person ! ")
    def mail(self, firstname):

        if firstname != "":
            sql = "SELECT email FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("His/Her mail is " + str(output["email"]))
        else:
            print("Huuum, I don't know this person !")
