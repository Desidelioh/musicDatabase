from connect import * # import the connect.py module
import readSongs #import readSongs
import time #

#subroutine/function
def insertSongs():
    #create an empty list called songs
    songs = []
    #Column Names: SongID("SongID" AUTOINCREMENT), Title, Artist, Genre
    #Ask for user input
    title = input("Enter Song Title: ")
    artist = input("Enter Song Artist: ")
    genre = input("Enter Song Genre: ")
    
    #Working with list: Insert vs append?
    #Insert: songs.insert(2,"Tests")
    #append: songs.append("A")

    #Save the dat capture and held in the respect variables(titles,artist.genre) to the songs list
    
    #songs.append(title)
    #songs.append(artist)
    #songs.append(genre)
    #or
    songs.extend([title,artist,genre])

    #Insert data saved in the list(songs) into the song table
    dbCursor.execute("INSERT INTO songs(Title,Artist,Genre)VALUES(?,?,?)", songs)
    dbCon.commit()#make the changes to the database permanently

    print(f"{title} has been inserted into the songs")

    # call/invoke the sleep method from the time module
    time.sleep(3) # Delay execution(code block below) for a given number of seconds

    # call/invoke the read subroutine/function from the readSongs module
    readSongs.read()

if __name__=="__main__":
    insertSongs()