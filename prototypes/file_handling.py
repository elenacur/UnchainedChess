
pgn = "1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5" #example pgn

file = open("file_prototype.txt", "w") #open file
file.write(pgn) #write the pgn to the file

file = open("file_prototype.txt", "r") 
print(file.read()) #print contents of file for testing

file.close() #close file