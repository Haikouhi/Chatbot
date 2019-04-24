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
            print("His/Her/Their name is " + output["lastname"])
        else:
            print("Huuum, I don't know this person ! ")

# defining birthdate for any chosen name: 
    def date(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("His/Her/Their birthdate is " + str(output["birthdate"]))
        else:
            print("Huuum, I don't know this person ! ")


# defining city for any chosen name:
    def city(self, firstname):

        if firstname != "":
            sql = "SELECT city FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("He/She/They live in " + str(output["city"]))
        else: 
            print("Huuum, I don't know this person ! ")


# defining phone number for any chosen name:
    def number(self, firstname):

        if firstname != "":
            sql = "SELECT phone_number FROM class WHERE firstname ='{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            print("His/her/Their phone number is +33" + str(output["phone_number"]))
        else: 
            print("Huuum, I don't know this person ! ")
