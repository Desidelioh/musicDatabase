import sqlite3 as sql #import the sqlite3 module

#To use the sqlite3 module, start by creating a db connection object
#sqlite3.connect("dbName.db")# create or open(if exists) dbName.db

dbCon = sql.connect("Pt9_10DB/GLAW4C1.db")

#Create cursor object and call its execute method to perform sql queries

dbCursor = dbCon.cursor()