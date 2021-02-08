import numpy as np
import random
from time import sleep

def createBoard():
    
    return(np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]]))

    
def user_chance(board):
    position = int(input("Enter The Position Number:"))
    
    #print(position)
    
    if position == 1:
        board[0,0]=1
    elif position == 2:
        board[0,1]=1
    elif position == 3:
        board[0,2]=1
    elif position == 4:
        board[1,0]=1
    elif position == 5:
        board[1,1]=1
    elif position == 6:
        board[1,2]=1
    elif position == 7:
        board[2,0]=1
    elif position == 8:
        board[2,1]=1
    elif position == 9:
        board[2,2]=1
    else:
        print("Wrong Input!!\nEnter Again")
        user_chance(board)
    
    return board
        

def possibilities(board):
    k=1
    l=[]
    for i in range(0,3):
        for j in range(0,3):
            if board[i,j] == k:
                l.append((i,j))
            k+=1
    return l



def ai_chance(board):
    print("Its AI's Chance Now")
    po = possibilities(board)
    current_pos = random.choice(po)
    board[current_pos] = 0
    return board
    
def row_win(board,player):
    for i in range(len(board)):
        win=True
        for j in range(len(board)):
            if board[i,j]!=player:
                win=False
                continue
        if win==True:
            return True
    return win

def col_win(board,player):
    for i in range(len(board)):
        win=True
        for j in range(len(board)):
            if board[j,i]!=player:
                win=False
                continue
        if win==True:
            return True
    return win


def diag_win(board, player): 
    win = True
    y = 0
    for x in range(len(board)): 
        if board[x, x] != player: 
            win = False
    if win: 
        return win 
    win = True
    if win: 
        for x in range(len(board)): 
            y = len(board) - 1 - x 
            if board[x, y] != player: 
                win = False
    return win 
    
    
def win(board,player):
    if row_win(board,player):
        return True
    elif col_win(board,player):
        return True
    elif diag_win(board,player):
        return True
    else:
        return False

#Game Starts from here...
def play_game():
    print("\t\tWelcome to TicTacToe")
    board = createBoard()
    print("\t\tThis is The Board")
    print("\n",board)
    winner = False
    while not winner:
        sleep(2)
        board = user_chance(board)
        print(board)
        if win(board,1):
            sleep(1)
            print("User Won")
            winner = True
            break
        sleep(2)
        board = ai_chance(board)
        print(board)
        if win(board,0):
            sleep(1)
            print("AI Won")
            winner = True
            break


play_game()