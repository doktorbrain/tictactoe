# tic tac toe

# X|.|.
# .|O|.
# .|.|X

class Board:
    def __init__(self):
        self.state = [0,0,0,0,0,0,0,0,0]

    def make_turn(self,cell,player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
            return True
        return False
    
    def is_valid_turn(self,cell):
        if self.state[cell]==0:
            return True
        else:
            return False
    
    def check_win(self,player):
        s=player.symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True
        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True
        else:
            return False


    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True    

    def sign_to_printable(self,sign):
        if sign==0:
            return "."
        elif sign==1:
            return "X"
        else:
            return "O"

    def print_board(self,player):
        print("Player: " + self.sign_to_printable(player.symbol))
        print(" "+self.sign_to_printable(self.state[0])+" | "+self.sign_to_printable(self.state[1])+" | "+self.sign_to_printable(self.state[2])+"\n"+
        " "+self.sign_to_printable(self.state[3])+" | "+self.sign_to_printable(self.state[4])+" | "+self.sign_to_printable(self.state[5])+"\n"+
        " "+self.sign_to_printable(self.state[6])+" | "+self.sign_to_printable(self.state[7])+" | "+self.sign_to_printable(self.state[8])+"\n")

class Player:
    def __init__(self,symbol):
        self.symbol=symbol

if __name__ == '__main__':
    board=Board()
    player_a=Player(1)
    player_b=Player(-1)

    active_player = player_a

    while not board.is_full():
        board.print_board(active_player)

        try:
            cell = int(input("Welches Feld soll gesetzt werden? [1..9] "))           
        except ValueError:
            continue
        
        cell=cell-1
        if cell < 0 or cell > 8:
            print("Bitte eine Zahl von 1-9 eingeben!")
            continue
        if not board.make_turn(cell,active_player):
            print("ungültiger Move!")
            continue

        if board.check_win(active_player):
            print("Sie haben gewonnen!")
            board.print_board(active_player)
            break

        if active_player==player_a:
            active_player=player_b
        else:
            active_player=player_a
