#creates a text file and saves the notation in PGN format there
def save_game(notation_text):

    #creating the unique name of the file
    import datetime
    datetime = datetime.datetime.now()

    #not using %x or it the date is written in the american way
    #%x and %X also generate characters that can't be in file names
    date = datetime.strftime("%d") + "-" + datetime.strftime("%m") + "-" + datetime.strftime("%Y") + " "
    time = datetime.strftime("%H") + "-" + datetime.strftime("%M") + "-" + datetime.strftime("%S") + "-" + datetime.strftime("%f")

    file_name = "UnchainedChess Game " + date + time + ".txt"

    #creating the text file and writing notation to it
    file = open(file_name, "x")
    file.write(notation_text)
    file.close()