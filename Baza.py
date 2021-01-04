import mysql.connector


class Baza:

    @staticmethod
    def insertPlacowki(database, id_plac, adres):
        my_cursor = database.cursor()
        tamp = 'INSERT INTO placowki (id_plac, adres) VALUES (%s, %s)'
        values = (id_plac, adres)
        my_cursor.execute(tamp, values)
        database.commit()

    @staticmethod
    def addTable(database):
        my_cursor = database.cursor()
        my_cursor.execute(
            'CREATE TABLE pracownicy (nazwisko VARCHAR(255), id_zesp INTEGER(10), id_prac INTEGER PRIMARY KEY)')

    @staticmethod
    def createDatabse(name):
        mydb = mysql.connector.connect(host='localhost', user='root', password='debilkox')

        my_cursor = mydb.cursor()
        my_cursor.execute('CREATE DATABASE {}'.format(name))

    @staticmethod
    def connect(host, user, password, database):
        mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)
        # print(mydb)

        return mydb
