from connect import *
import readSongs
import time

#subroutine/function
def update():
    #use primary key to update
    idField = input("Enter the SongID of the record to be updated: ")

    #field to be updated: Title,Artist, Genre
    fieldName = input("Enter the Title,Artist or GenreAbdul as field name: ").title()
    #fieldValue: ask for the value for the field to be updated
    fieldValue = input(f"Enter the value for {fieldName}: ")
    #print(fieldValue)

    #add single quote on either side of the string
    fieldValue = "'" + fieldValue + "'"
    #print(fieldValue)

    # update a record in songs table
    " UPDATE songs SET {Title or Artist or Genre} = {fieldValue for Title or Artist or Genre} WHERE SongID ={1/2/3/4..}                "
    dbCursor.execute(F"UPDATE songs SET {fieldName} = {fieldValue} WHERE SongID = {idField} ")
    dbCon.commit()# save changes to the db table permanently
    print(f"Record {idField}: {fieldValue} updated in the songs table")

    # read from db
    # call/invoke the sleep method from the time module 
    time.sleep(3) # Delay execution(code block below) for a given number of seconds

    # call/invoke the read subroutine/function from the readSongs module
    readSongs.read()
    
if __name__=="__main__":
    update()