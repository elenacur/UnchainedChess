
pgn = "1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5"

file = open("file_prototype.txt", "w")
file.write(pgn)

file = open("file_prototype.txt", "r")
print(file.read())

file.close()