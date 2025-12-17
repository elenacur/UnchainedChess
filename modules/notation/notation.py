class Notation:
    def __init__(self):
        self.__moves = [] #list of all the moves that will turn into a 2D list

    #getters
    def get_moves(self):
        return self.__moves

    #setters
    def set_moves(self, p_moves):
        self.__moves = p_moves

    #records a move into the notation list
    def record_move(self, move, white_moving):
        if white_moving == True: #if it's white's move
            self.__moves.append([move, ""])
        else: #if it's black's move:
            self.__moves[-1][1] = move #in the last pair, accessing the second element, store move there
        

    #returns notation in a text/PGN format
    def get_notation_text(self):
        notation_text = ""

        for i in range(0, len(self.__moves)):
            notation_text += (str(i + 1) + ". ")
            full_move = self.__moves[i]
            notation_text += (full_move[0] + " " + full_move[1]) + " "
        
        return notation_text
    
