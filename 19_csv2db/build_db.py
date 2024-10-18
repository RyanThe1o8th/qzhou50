#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


#DB_FILE="discobandit.db"

db = sqlite3.connect("saveFile.txt") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

database = open("students.csv", newline = '')
reader = csv.reader(database)
#for row in reader:
#    print (row)
#database.split("\n")
c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER)")
for row in reader:
    c.execute("INSERT INTO students VALUES(?, ?, ?)", row)
#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement
print( c.execute("SELECT * FROM students"))
#==========================================================

db.commit() #save changes
db.close()  #close database
