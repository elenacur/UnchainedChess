
#mock of 2D pieces array
pieces = [["r", "n", "b", "q", "k", "b", "n", "r"], ["p", "p", "p", "p", "p", "p", "p", "p"], 
         ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
         ["", "", "", "", "", "", "", ""], ["p", "p", "p", "p", "p", "p", "p", "p"], 
         ["r", "n", "b", "q", "k", "b", "n", "r"]]

notation = [] #list of moves

#adds a move to notation
def notate_move(current_row, current_column, new_row, new_column):
    move = pieces[current_row][current_column] + str(new_column) + str(new_row)
    notation.append(move)

#moves piece to new index of pieces
def move_piece(current_row, current_column, new_row, new_column):
    notate_move(current_row, current_column, new_row, new_column)
    pieces[new_row][new_column] = pieces[current_row][current_column]
    pieces[current_row][current_column] = ""
    print("")
    for i in pieces:
        print(i)
    

#test moves
move_piece(6, 4, 4, 4)
print(notation)
move_piece(1, 4, 3, 4)
print(notation)
