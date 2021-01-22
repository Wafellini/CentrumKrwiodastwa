import mysql.connector
import cgitb

cgitb.enable(format='text')

class Baza:

    @staticmethod
    def insert(database, table, args):
        names = Baza.getColumnNamesFromTable(database, table)
        my_cursor = database.cursor()
        names_format = ""
        args_format = ""
        j = 0
        for i in range(len(args)):
            if args[j] is None:
                args.pop(j)
                names.pop(j)
            else:
                names_format += str(names[j]) + ", "
                args_format += '"' + str(args[j]) + '"' + ', '
                j += 1
        tamp = 'INSERT INTO {} ({}) VALUES ({})'.format(table, names_format[:-2], args_format[:-2])
        print(tamp)
        my_cursor.execute(tamp)
        database.commit()

    @staticmethod
    def update(database, table, args, args2):
        names = Baza.getColumnNamesFromTable(database, table)
        names2 = names.copy()
        my_cursor = database.cursor()
        set_values = ""
        where_values = ""
        j = 0
        for i in range(len(args)):
            if args[j] is None:
                args.pop(j)
                names.pop(j)
            else:
                where_values += str(names[j]) + ' = "' + str(args[j]) + '" and '
                j += 1
        print(where_values)

        for it in range(len(args2)):
            #musza być wypełnione wszystkie
            if args2[it] is None:
                set_values += str(names2[it]) + ' = "", '
            else:
                set_values += str(names2[it]) + ' = "' + str(args2[it]) + '", '
        print(set_values)
        tamp = 'UPDATE {} SET {} WHERE {}'.format(table, set_values[:-2], where_values[:-4])
        print(tamp)
        my_cursor.execute(tamp)
        database.commit()

    @staticmethod
    def delete(database, table, args):
        names = Baza.getColumnNamesFromTable(database, table)
        my_cursor = database.cursor()
        names_format = ""
        args_format = ""
        final_format = ""
        j = 0
        for i in range(len(args)):
            if args[j] is None:
                args.pop(j)
                names.pop(j)
            else:
                names_format += str(names[j]) + ", "
                args_format += '"' + str(args[j]) + '"' + ', '
                final_format += str(names[j]) + ' = "' + str(args[j]) +  '" and '
                j += 1

        tamp = 'DELETE FROM {} WHERE {}'.format(table, final_format[:-5])
        print(tamp)
        my_cursor.execute(tamp)
        database.commit()

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

