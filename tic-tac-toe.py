from IPython.display import clear_output

# -------------PRINT OUT BOARD--------------------
def display_board(board):
    
    print("   " "|" "   " "|" "   ")
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9]+" ")
    print("   " "|" "   " "|" "   ")
    print("-----------")
    print("   " "|" "   " "|" "   ")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6]+" ")
    print("   " "|" "   " "|" "   ")
    print("-----------")
    print("   " "|" "   " "|" "   ")
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3]+" ")
    print("   " "|" "   " "|" "   ")
  
    print(board[0])

# -------------Player chooses X or O--------------------
def player_input():
    choice="wrong"
    while choice not in ["X", "O"]:
        choice=input("Do you want to be X or O? ")
        if choice not in ["X","O"]:
            clear_output()
            print("Sorry, please select X or O")
    return choice

# -------------Assign Marker to the board--------------------
def place_marker(board, marker, position):
    board[position]=marker


# -------------Check for winner--------------------
def win_check(board, mark):
    if board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    elif board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark: 
        return True
    elif board[7]==mark and board[8]==mark and board[9]==mark: 
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark: 
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark: 
        return True
    elif board[3]==mark and board[6]==mark and board[9]==mark: 
        return True
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return True
    else:
        return False


# -------------Which player goes first--------------------
from random import randint

def choose_first():
    random_num=randint(0,1)
    players=["Player 1", "Player 2"]
    return players[random_num]

# -------------Checks if space is empty--------------------
def space_check(board, position):
    return board[position]==" "

# -------------Checks if board is full--------------------
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
        
# -------------Input Position--------------------
def player_choice(board):
    choice='wrong'
    while choice not in ['1','2','3','4','5','6','7','8','9']:
        choice = input("Choose where you would like to play by typing in 1-9? ")
        if choice not in ['1','2','3','4','5','6','7','8','9']:
            print("Sorry invalid input, please type in a number 1-9")
    choice=int(choice)
    space_check(board, choice)
    if space_check(board, choice)==True:
        return choice
    
# -------------Ask to play again--------------------
def replay():
    choice="wrong"
    
    while choice not in ['Y','N']:
        choice=input("Would you like to play again? Y or N? ")
        if choice not in ['Y','N']:
            clear_output()
            print("Sorry I did not understand. Please make sure to choose Y or N")
        if choice=='Y':
            return True
        else:
            return False
        
# -------------Gameplay--------------------
print('Welcome to Tic Tac Toe!')

game_on=True

while game_on==True:
    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    first_player=choose_first()
    print(f'{first_player} goes first!')
    marker=player_input()

    if first_player=='Player 1' and marker=='X':
        player1_marker="X"
        player2_marker="O"
    elif first_player=='Player 1' and marker=='O':
        player1_marker="O"
        player2_marker="X"
    elif first_player=='Player 2' and marker=='X':
        player1_marker="O"
        player2_marker="X"
    elif first_player=='Player 2' and marker=='O':
        player1_marker="X"
        player2_marker="O"

    stop_game=False
    current_player=first_player
    while stop_game==False:
        if current_player=="Player 1":
            print("Player 1's turn")
            position=player_choice(board)
            place_marker(board, player1_marker, position)
            display_board(board)
        
            if win_check(board, player1_marker)==True:
                print("Player 1 wins")
                stop_game=True
            else:
                if full_board_check(board)==True:
                    print("It's a draw")
                    stop_game=True
                else:
                    current_player="Player 2"
                
        
        
        elif current_player=="Player 2":
            print("Player 2's turn")
            position=player_choice(board)
            place_marker(board, player2_marker, position)
            display_board(board)
        
            if win_check(board, player2_marker)==True:
                print("Player 2 wins")
                stop_game=True
            else:
                if full_board_check(board)==True:
                    print("It's a draw")
                    stop_game=True
                else:
                    current_player="Player 1"
    
    if stop_game==True:
        game_on=replay()