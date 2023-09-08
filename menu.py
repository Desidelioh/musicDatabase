# import modules listed below
import  readSongs, addSongs, updateSongs, deleteSongs, reports
import time


# create a function with a return statement
def menuOptions():
    options = 0 # flag variable
    # print(type(options))
    # concept of iteration 
    optionList = ["1","2","3","4","5","6"]
    # print(type(optionList))
    userChoices = "Songs Menu Options\nEnter:\n1. Print.\n2. Add.\n3. Update.\n4. Delete.\n5. Reports.\n6. Exit."
    while options not in optionList:# ["1","2","3","4","5"] : execute the indented code block below
        print(userChoices)
        # re-assign the value held in the options variable
        # concept of sequence
        options = input("Enter an option from the songs main menu choices above: ") # "1" , "2"
        # print(type(options))

        # concept of selection
        if options not in optionList: #["1","2","3","4","5"]
            print(f"{options} is not a valid choice in the songs main menu!: ")
    return options


# reports options  
def reportOptions():
    options = 0 # flag variable
    # print(type(options))
    # concept of iteration 
    optionList = ["1","2","3","4","5","6"]
    # print(type(optionList))
    userChoices = "Reports Menu Options\nEnter:\n1. Artists.\n2. Titles.\n3. Genres.\n4. SongID.\n5. Order.\n6. Exit."
    while options not in optionList:# ["1","2","3","4","5"] : execute the indented code block below
        print(userChoices)
        # re-assign the value held in the options variable
        # concept of sequence
        options = input("Enter an option from the songs report menu choices above: ") # "1" , "2"
        # print(type(options))

        # concept of selection
        if options not in optionList: #["1","2","3","4","5"]
            print(f"{options} is not a valid choice in the songs main menu!: ")
    return options
# ########################################
#create a boolean varible with a True value
mainProgram = True
while mainProgram: # Same as while True
    mainMenu = menuOptions() # assign the menuOptions function to the mainMenu variable

    # selecion
    if mainMenu == "1":
        # call/invoke the respective modules and function for each option  
        readSongs.read() 
    elif mainMenu == "2":
        addSongs.insertSongs()
    elif mainMenu == "3":
        updateSongs.update()
    elif mainMenu == "4":
        deleteSongs.delete()
    elif mainMenu == "5":
        # reports.readOrder()
        reportsProgram = True
        while reportsProgram: # Same as while True
            reportsMenu = reportOptions()# assign the menuOptions function to the mainMenu variable
            if reportsMenu == "1":
                reports.artist()
            elif reportsMenu == "2":
                reports.title()
            elif reportsMenu =="3":
                reports.genre()
            elif reportsMenu == "4":
                reports.songID()
            elif reportsMenu == "5":
                reports.readOrder()
            else:
                # re-assign the reportsProgram with a boolean False value
                reportsProgram = False
                input(f"Press enter to exit th Sub Mene: reports program")
    else:
       # re-assign the mainProgram with a boolean False value
       mainProgram = False
input(f"Press enter to exit th program in 3 seconds ")
