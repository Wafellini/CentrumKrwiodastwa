import mysql.connector


class Baza:
    @staticmethod
    def selectuserWszystkieDonacje(database, pesel):
        try:
            my_cursor = database.cursor()
            my_cursor.execute('call wszytkie_donacje({})'.format(pesel))
            result = my_cursor.fetchall()

            my_cursor.close()
            return result
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
            print('errno: ',error.errno)

        return None


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
            return result
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
            print("Error code:", error.errno)  # error number
            print("SQLSTATE value:", error.sqlstate)  # SQLSTATE value
            print("Error message:", error.msg)
        return None

    @staticmethod
    def selectPesels(database):
        my_cursor = database.cursor()

        tamp = 'SELECT distinct pesel FROM darczyncy'
        print(tamp)
        my_cursor.execute(tamp)

        result = my_cursor.fetchall()
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
            args = [i for i in args if i is not None]
            print('argumentssss    :',args)
            if args == []:
                tamp = 'SELECT * FROM {}'.format(table)
            else:
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
            if(table == "darczyncy"):
                a = args_format.find('"')
                b = args_format[a+1:].find('"')
                args_format = args_format[a+1:b+1]+args_format[b+2:]
            tamp = 'INSERT INTO {} ({}) VALUES ({})'.format(table, names_format[:-2], args_format[:-2])
            print(tamp)
            my_cursor.execute(tamp)
            database.commit()

            my_cursor.close()

            if table == "donacje":
                print('update_ostatnia_donacja test')
                currsor = database.cursor()
                currsor.execute('call update_ostatnia_donacja({})'.format(int(args[4])))
                database.commit()
                currsor.close()


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


