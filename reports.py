from connect import *

def genre():
    genreField = input("Enter the name of the song Genre to search for:  ")
    dbCursor.execute(f"SELECT * FROM songs WHERE Genre = '{genreField}' ")# select all records from songs table
    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)


def songID():
    idField = input("Enter the SongID of the record to search forbe deleted: ")
    dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {idField} ")# select all records from songs table
    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



# fieldName = input("Enter Field Name: ")

def readOrder():
    # dbCursor.execute(f"SELECT * FROM songs ORDER BY {fieldName} DESC")
    # dbCursor.execute(f"SELECT * FROM songs ORDER BY SongID DESC")
    # dbCursor.execute(f"SELECT Artist, Genre FROM songs ORDER BY SongID DESC")
    # dbCursor.execute(f"SELECT Artist, Genre FROM songs ORDER BY Artist ASC")
    # dbCursor.execute(f"SELECT * FROM songs WHERE Genre = 'Soul' or Genre = 'Rap' ")
    # dbCursor.execute(f"SELECT * FROM songs WHERE Title Like 't%' ")
    dbCursor.execute(f"SELECT * FROM songs WHERE Title NOT Like 't%' ")
       
     
    records = dbCursor.fetchall()# fetches all records selected from the songs table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



if __name__=="__main__":
    # artist()
    # title()
    # genre()
    # songID()
    readOrder()