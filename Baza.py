import mysql.connector
import cgitb
from mysql.connector import Error

cgitb.enable(format='text')

class Baza:
    @staticmethod
    def selectuserWszystkieDonacje(database, pesel):
        try:
            print('step 0')
            print('step 03242134')
            my_cursor = database.cursor()
            print('step 0.1')
            # tamp = 'call wszytkie_donacje({})'.format(pesel)
            inpt = str(pesel)
            print('step 0.2')
            #my_cursor.callproc('call wszytkie_donacje', (pesel,))
            my_cursor.execute('call wszytkie_donacje({})'.format(pesel))
            print('step 0.3')

            print('step 1   ', my_cursor)
            # print out the result
            # for result in my_cursor.stored_results():
            #     print('fetchall',result.fetchall())

            print('fetchall', my_cursor.fetchall())
            print('step 1.1   ',)
            # print(tamp)
            #print(my_cursor)
            # my_cursor.execute(tamp)
            print(my_cursor)

            #result = my_cursor.fetchall()
            #print('wszytkie_donacje:  ', result)

            my_cursor.close()
            # database.commit()
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
            print('errno: ',error.errno)

        return None
        if result == []:
            return None
        else:
            return result


    @staticmethod
    def selectuserInfo(database,pesel):
        try:
            my_cursor = database.cursor()

            tamp = 'call user_info({})'.format(pesel)

            print(tamp)

            my_cursor.execute(tamp)
            print(my_cursor)

            result = my_cursor.fetchall()
            print('USER INFO:  ', result)




            my_cursor.close()
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
            print("Error code:", error.errno)  # error number
            print("SQLSTATE value:", error.sqlstate)  # SQLSTATE value
            print("Error message:", error.msg)
        return None
        if result == []:
            return None
        else:
            return result

    @staticmethod
    def selectPesels(database):
        my_cursor = database.cursor()

        tamp = 'SELECT distinct pesel FROM darczyncy'
        print(tamp)
        my_cursor.execute(tamp)

        result = my_cursor.fetchall()
        # database.commit()
        print('wynik selecta peseli: ', result)

        my_cursor.close()
        return result

    @staticmethod
    def select(database, table, args):
        try:
            names = Baza.getColumnNamesFromTable(database, table)
            my_cursor = database.cursor()
            final_format = ""
            j = 0
            for i in range(len(args)):
                if args[j] is None:
                    args.pop(j)
                    names.pop(j)
                else:
                    final_format += str(names[j]) + ' = "' + str(args[j]) + '" and '
                    j += 1

            tamp = 'SELECT * FROM {} WHERE {}'.format(table, final_format[:-5])
            print(tamp)
            my_cursor.execute(tamp)

            result = my_cursor.fetchall()
            # database.commit()
            print('wynik selecta: ',result)

            my_cursor.close()
            if result == []:
                return None
            else:
                return result
        except mysql.connector.Error as error:
            print('While inserting')
            print("Failed to execute stored procedure: {}".format(error))
            print("Error code:", error.errno)  # error number
            print("SQLSTATE value:", error.sqlstate)  # SQLSTATE value
            print("Error message:", error.msg)
            return (error.errno)
    @staticmethod
    def insert(database, table, args):
        try:
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

            my_cursor.close()
        except mysql.connector.Error as error:
            print('While inserting')
            print("Failed to execute stored procedure: {}".format(error))
            print("Error code:", error.errno)  # error number
            print("SQLSTATE value:", error.sqlstate)  # SQLSTATE value
            print("Error message:", error.msg)
            return (error.errno)
    @staticmethod
    def update(database, table, args, args2):
        try:
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

            my_cursor.close()
        except mysql.connector.Error as error:
            print('While updating')
            print("Failed to execute stored procedure: {}".format(error))
            print("Error code:", error.errno)  # error number
            print("SQLSTATE value:", error.sqlstate)  # SQLSTATE value
            print("Error message:", error.msg)
            return (error.errno)
    @staticmethod
    def delete(database, table, args):
        try:
            names = Baza.getColumnNamesFromTable(database, table)
            my_cursor = database.cursor()
            final_format = ""
            j = 0
            for i in range(len(args)):
                if args[j] is None:
                    args.pop(j)
                    names.pop(j)
                else:
                    final_format += str(names[j]) + ' = "' + str(args[j]) +  '" and '
                    j += 1

            tamp = 'DELETE FROM {} WHERE {}'.format(table, final_format[:-5])
            print(tamp)
            my_cursor.execute(tamp)
            database.commit()

            my_cursor.close()
        except mysql.connector.Error as error:
            print('While deleting')
            print("Failed to execute stored procedure: {}".format(error))
            print("Error code:", error.errno)  # error number
            print("SQLSTATE value:", error.sqlstate)  # SQLSTATE value
            print("Error message:", error.msg)
            return(error.errno)

    @staticmethod
    def insertPlacowki(database, id_plac, adres):
        my_cursor = database.cursor()
        tamp = 'INSERT INTO placowki (id_plac, adres) VALUES (%s, %s)'
        values = (id_plac, adres)
        my_cursor.execute(tamp, values)
        database.commit()

        my_cursor.close()

    @staticmethod
    def getColumnNamesFromTable(database,table):
        my_cursor = database.cursor()
        my_cursor.execute('show columns from {}'.format(table))
        columns = []
        for i in my_cursor:
            print(i[0])
            columns.append(i[0])

        my_cursor.close()
        return columns




    @staticmethod
    def deletePlacowki(database, id_plac, adres):
        my_cursor = database.cursor()
        tamp = 'DELETE FROM placowki WHERE id_plac = %s and adres = %s'
        values = (id_plac, adres)
        my_cursor.execute(tamp, values)
        database.commit()

        my_cursor.close()

    @staticmethod
    def addTable(database):
        my_cursor = database.cursor()
        my_cursor.execute(
            'CREATE TABLE pracownicy (nazwisko VARCHAR(255), id_zesp INTEGER(10), id_prac INTEGER PRIMARY KEY)')

        my_cursor.close()

    @staticmethod
    def createDatabse(name):
        mydb = mysql.connector.connect(host='localhost', user='root', password='debilkox')

        my_cursor = mydb.cursor()
        my_cursor.execute('CREATE DATABASE {}'.format(name))

        my_cursor.close()

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
        my_cursor.close()

        return(xd)

