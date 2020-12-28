import mysql.connector
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def addTable(database):
    my_cursor = database.cursor()
    my_cursor.execute('CREATE TABLE pracownicy (nazwisko VARCHAR(255), id_zesp INTEGER(10), id_prac INTEGER PRIMARY KEY)')

def createDatabse(name):
    mydb = mysql.connector.connect(host= 'localhost', user= 'root', password= 'debilkox')

    my_cursor = mydb.cursor()
    my_cursor.execute('CREATE DATABASE {}'.format(name))

def connect(host, user, password, database):
    mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
    print(mydb)

    return mydb
    # my_cursor = mydb.cursor()
    # #my_cursor.execute('SHOW DATABASES')
    # my_cursor.execute('SELECT * FROM country')
    # print(my_cursor)
    # for i in my_cursor:
    #     print(i)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    name = 'testdb'


    createDatabse(name)
    dtbase = connect("localhost", "root", "debilkox",name)
    addTable(dtbase)

    my_cursor = dtbase.cursor()
    my_cursor.execute('SHOW TABLES')
    for i in my_cursor:
        print(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
