import connect
import readSongs
import time

#subroutine/function
def delete():
     #use primary key to delete a record
    idField = input("Enter the SongID of the record to be deleted: ")

    "DELETE FROM songs WHERE SongID = 1/2/3/4/5/......"
    connect.dbCursor.execute(f"DELETE FROM songs WHERE SongID = {idField}")
    connect.dbCon.commit()

    print(f"Record {idField} deleted from the songs table")

    # read from db
    # call/invoke the sleep method from the time module 
    time.sleep(3) # Delay execution(code block below) for a given number of seconds

    # call/invoke the read subroutine/function from the readSongs module
    readSongs.read()


if __name__=="__main__":
    delete()


