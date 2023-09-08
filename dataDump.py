from connect import *
import readSongs
import time

#subroutine function
def bulkInsert():
    # load script (songs.sql) from file 
    with open(r"Pt9_10DB\newSongs.sql") as sqlFile:
        # read content in the sqlFile and save it in the dumpData variable
        dumpData = sqlFile.read()

        # call the executescript() and pass the dumpData variable as argument
        dbCursor.executescript(dumpData)
        dbCon.commit()

        time.sleep(3)

        # call readSongs.read()
        readSongs.read()
if __name__=="__main__":
    bulkInsert()