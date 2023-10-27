

# LIST REPRESENTATION
top_left = ' '
top_middle = ' '
top_right = ' '
middle_left = ' '
middle_middle = ' '
middle_right = ' '
bottom_left = ' '
bottom_middle = ' '
bottom_right = ' '
list_board = [[top_right, top_middle, top_right],
              [middle_left, middle_middle, middle_right],
              [bottom_left, bottom_middle, bottom_right]]


def see_board(list_board):
    print(list_board[0])
    print(list_board[1])
    print(list_board[2])

print('   ')
see_board(list_board)
print('   ')
player1 = (input("Hello! Welcome to my tic-tac-toe game! Would you like to be X's or O's (x/o)? ")).lower()
player2 = ''

if player1 == 'x':
    player2 = 'o'
else:
    player2 = 'x'
    


print(f"Alright! Let us begin the game! {player1}'s will start the game.")
print('To input your game piece, enter a number between 1 and 9, each number correlates to a place in the grid, starting with the number 1 in the top left corner, and ending with 9 in the bottom right corner.')

current_player = player1

while True:
    answer = int(input(f"{current_player}, what's your input? "))
    
    if 4 > answer > 0:
            list_board[0][answer - 1] = current_player
    elif 7 > answer > 3:
        list_board[1][answer - 4] = current_player
    else:
        list_board[2][answer - 7] = current_player

    see_board(list_board)

    #DETERMINE WINNER
    if list_board[0][0] == 'x' and list_board[0][1] == 'x' and list_board[0][2] == 'x':
        print("X WINS!!!")
        break
    if list_board[1][0] == 'x' and list_board[1][1] == 'x' and list_board[1][2] == 'x':
        print("X WINS!!!")
        break
    if list_board[2][0] == 'x' and list_board[2][1] == 'x' and list_board[2][2] == 'x':
        print("X WINS!!!")
        break
    if list_board[0][0] == 'x' and list_board[1][0] == 'x' and list_board[2][0] == 'x':
        print("X WINS!!!")
        break
    if list_board[0][1] == 'x' and list_board[1][1] == 'x' and list_board[2][1] == 'x':
        print("X WINS!!!")
    if list_board[0][2] == 'x' and list_board[1][2] == 'x' and list_board[2][2] == 'x':
        print("X WINS!!!")
        break
    if list_board[0][0] == 'x' and list_board[1][1] == 'x' and list_board[2][2] == 'x':
        print("X WINS!!!")
        break
    if list_board[0][2] == 'x' and list_board[1][1] == 'x' and list_board[2][0] == 'x':
        print("X WINS!!!")
        break
     

    if list_board[0][0] == 'o' and list_board[0][1] == 'o' and list_board[0][2] == 'o':
        print("O WINS!!!")
        break
    if list_board[1][0] == 'o' and list_board[1][1] == 'o' and list_board[1][2] == 'o':
        print("O WINS!!!")
        break
    if list_board[2][0] == 'o' and list_board[2][1] == 'o' and list_board[2][2] == 'o':
        print("O WINS!!!")
        break
    if list_board[0][0] == 'o' and list_board[1][0] == 'o' and list_board[2][0] == 'o':
        print("O WINS!!!")
        break
    if list_board[0][1] == 'o' and list_board[1][1] == 'o' and list_board[2][1] == 'o':
        print("O WINS!!!")
        break
    if list_board[0][2] == 'o' and list_board[1][2] == 'o' and list_board[2][2] == 'o':
        print("O WINS!!!")
        break
    if list_board[0][0] == 'o' and list_board[1][1] == 'o' and list_board[2][2] == 'o':
        print("O WINS!!!")
        break
    if list_board[0][2] == 'o' and list_board[1][1] == 'o' and list_board[2][0] == 'o':
        print("O WINS!!!")
        break

    elif ' ' not in list_board[0] and ' ' not in list_board[1] and ' ' not in list_board[2]:
        print("DRAW!")
        break

    #SWITCH TURNS
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

    

