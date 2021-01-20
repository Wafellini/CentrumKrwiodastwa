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
    def getColumnNamesFromTable(database,table):
        my_cursor = database.cursor()
        my_cursor.execute('show columns from {}'.format(table))
        columns = []
        for i in my_cursor:
            print(i[0])
            columns.append(i[0])
        return columns


    @staticmethod
    def deletePlacowki(database, id_plac, adres):
        my_cursor = database.cursor()
        tamp = 'DELETE FROM placowki WHERE id_plac = %s and adres = %s'
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

    @staticmethod
    def getTableNamesFromDb(database):
        mydb = mysql.connector.connect(host='localhost', user='root', password='debilkox')

        my_cursor = mydb.cursor()
        # my_cursor.execute('select table_name from {}'.format(database))
        my_cursor.execute('use {}'.format(database))
        my_cursor.execute('show tables')

        xd = [i[0] for i in my_cursor]
        return(xd)

