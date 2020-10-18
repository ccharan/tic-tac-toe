import random
from os import system
import time


# the function accepts one parameter containing the board's current status
# and prints it out to the console
def display_board(board):
    system('cls')
    display_score(computer_score, your_score)
    for i in range(3):
        print("+-------------+-------------+-------------+")
        print("|             |             |             |")
        print("|             |             |             |")
        print("|      {}      |      {}      |      {}      |".format(blank_broard[i][0], blank_broard[i][1], blank_broard[i][2]))
        print("|             |             |             |")
        print("|             |             |             |")
    print("+-------------+-------------+-------------+")

    make_list_of_free_fields(board)


# the function accepts the board current status, asks the user about their move,
# checks the input and updates the board according to the user's decision
def enter_move(board):
    move = input("Enter your move: ")

    index_pos = ()
    for i, x in enumerate(board):
        if move in x:
            index_pos = (i, x.index(move))

    # checks valid move
    if index_pos in free_square:
        board[index_pos[0]][index_pos[1]] = '0'
        blank_broard[index_pos[0]][index_pos[1]] = '0'
        display_board(board)
    else:
        print("Please select proper box")
        enter_move(board)


# the function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers
free_square = []
def make_list_of_free_fields(board):
    free_square.clear()
    for row in range(3):
        for column in range(3):
            if board[row][column] in '123456789':
                free_square.append((row, column))


# the function analyzes the board status in order to check if
# the player using 'O's or 'X's has won the game
def victory_for(board, sign):
    global keep_running

    for i in range(3):
        if (sign in board[i][0]) \
                and (sign in board[i][1]) \
                and (sign in board[i][2]):
            return True
        if (sign in board[0][i]) \
                and (sign in board[1][i]) \
                and (sign in board[2][i]):
            return True

    if (sign in board[0][0]) \
            and (sign in board[1][1])\
            and (sign in board[2][2]):
        return True
    if (sign in board[0][2]) \
            and (sign in board[1][1]) \
            and (sign in board[2][0]):
        return True


# the function draws the computer's move and updates the board
def draw_move(board):
    make_list_of_free_fields(board)
    move = str(random.randint(1, 9))
    index_pos = ()
    for i, x in enumerate(board):
        if move in x:
            index_pos = (i, x.index(move))

    # checks valid move
    if index_pos in free_square:

        board[index_pos[0]][index_pos[1]] = 'X'
        blank_broard[index_pos[0]][index_pos[1]] = 'X'
        time.sleep(0.5)
        display_board(board)

    else:
        draw_move(board)


# Checking if user wants to continue playing or wants to quit the game
def one_more_chance():
    global keep_running
    global board, blank_broard

    decision = input("\nOne more game (Y/N): ")

    if decision in "Yy":
        board = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]

        blank_broard = [[' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' ']]

        keep_running = True
        system('cls')
        return True
    elif decision in "Nn":
        print("Exiting...")
        keep_running = False
        system('cls')
        return False
    else:
        print("Invalid input, Exiting...")
        keep_running = False
        system('cls')
        return False


# displays the scores
def display_score(c_score, y_score):
    print("Computer score: ", c_score)
    print("Your score :", y_score)


# program starts from here
board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]

blank_broard = [[' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']]

your_score = 0
computer_score = 0
keep_running = True

while keep_running:
    #system('cls')
    draw_move(board)
    if victory_for(board, 'X') is True:
        computer_score += 1

        display_board(board)
        print("COMPUTER won the game\n")

        if one_more_chance() is False:
            break
        else:
            draw_move(board)

    if len(free_square) is 0:
        display_board(board)
        print("Draw\n")

        if one_more_chance() is False:
            break
        else:
            draw_move(board)


    enter_move(board)
    if victory_for(board, '0') is True:
        your_score += 1

        display_board(board)
        print("YOU won the game\n")

        if one_more_chance() is False:
            break

