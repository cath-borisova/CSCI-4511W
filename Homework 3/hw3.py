import sys
sys.path.append('aima-python')
from search import *
from games import *
import math
import time


#globals
player = 'X'
opponent = 'O'

def k_in_row(k, board, move, player, delta_x_y):
    '''Adapted from AIMA code in games.py
    Purpose:
        Function to help determine a winner in k-in-a-row 
        type games like TicTacToe, Connect4, Gomoku

    Parameters:
        k: int number in a row necessary to win
        board: dictionary with (row,col) keys, 'X' or 'O' values
        move: where to search from
        player: str 'X' or 'O'
        delta_x_y: which direction to search in

    Return Value:
        True if there is a line through move on board for player.
    '''
    (delta_x, delta_y) = delta_x_y
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y
    x, y = move
    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y
    n -= 1  # Because we counted move itself twice
    return n >= k

def is_winner(k, h, v, board, player):
    '''Adapted from AIMA code in games.py 
    Purpose: 
        Determine if given player wins in a k-in-a-row type game.

    Parameters:
        k: int number in a row necessary to win
        h: width (horizontal) of board
        v: height (vertical) of board
        board: dictionary with (row,col) keys, 'X' or 'O' values
        player: str 'X' or 'O'

    Return Value:
        True if player wins, False otherwise
    '''
    for row in range(1, h+1):
        for col in range(1, v+1):
            if (k_in_row(k, board, (row,col), player, (0,1)) or
                k_in_row(k, board, (row,col), player, (1,0)) or
                k_in_row(k, board, (row,col), player, (1,-1)) or
                k_in_row(k, board, (row,col), player, (1,1))):
                return True
    return False


def connect4_eval_bad(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the 7th row
    (that is, the bottom row) 

    This is a terrible plan, but at least you can see it in action, 
    as the agent will prefer to put its pieces on across the bottom row
    if at all possible. 

    (Change it to row 2 or 3 if you want to see different behavior)
    '''
    if is_winner(4, 7, 6, state.board, 'X'):
        return 1
    if is_winner(4,7,6, state.board, 'O'):
        return -1
    ev = 0
    for col in range(1,7):
        if (7,col) in state.board and state.board[(7,col)] == 'X':
            ev += 1
    
    # Divide by 42 to make sure that ev is less than 1
    # It is important to make sure that your evaluation is never better or worse than
    #   actual win/loss utility (represented by 1/-1)
    return ev / 42

def connect4_eval(state):
    '''Your Connect 4 evaluation function
    Hopefully better than mine!
    '''
    if is_winner(4, 7, 6, state.board, player):
        return 1
    if is_winner(4,7,6, state.board, opponent):
        return -1
    x_ev = 0
    for row in range(1,8):
        for col in range(1,7):
            if (row,col) in state.board and state.board[(row, col)] == player:
                in_a_row = 0
                possible = 1
                if row < 7 and (row+1,col) in state.board:
                    possible += 1
                    if state.board[(row + 1, col)] == player:
                        in_a_row += 1
                    
                if row > 1 and(row-1,col) in state.board:
                    possible += 1
                    if state.board[(row - 1, col)] == player:
                        in_a_row += 1

                if col < 6 and (row,col+1) in state.board:
                    possible += 1
                    if state.board[(row , col+1)] == player:
                        in_a_row += 1
                    
                if col > 1 and(row,col-1) in state.board:
                    possible += 1
                    if state.board[(row, col-1)] == player:
                        in_a_row += 1
                if row < 7 and col < 6 and (row+1,col+1) in state.board:
                    possible += 1
                    if state.board[(row+1, col+1)] == player:
                        in_a_row += 1
                if row > 1 and col> 1 and (row-1,col-1) in state.board:
                    possible += 1
                    if state.board[(row-1, col-1)] == player:
                        in_a_row += 1
                if row < 7 and col > 1 and (row+1,col-1) in state.board:
                    possible += 1
                    if state.board[(row+1, col-1)] == player:
                        in_a_row += 1
                if row> 1 and col < 6 and (row-1,col+1) in state.board:
                    possible += 1
                    if state.board[(row-1, col+1)] == player:
                        in_a_row += 1
                x_ev += (in_a_row/possible)
    return x_ev / 42

def gomoku_eval(state):
    '''Your Connect 4 evaluation function
    Hopefully better than mine!
    '''
    if is_winner(5, 15, 16, state.board, 'X'):
        return 1
    if is_winner(5, 15, 16, state.board, 'O'):
        return -1
    x_ev = 0
    for row in range(1,16):
        for col in range(1,15):
            if (row,col) in state.board and state.board[(row, col)] == player:
                in_a_row = 0
                possible = 1
                if row < 15 and (row+1,col) in state.board:
                    possible += 1
                    if state.board[(row + 1, col)] == player:
                        in_a_row += 1
                    
                if row > 1 and(row-1,col) in state.board:
                    possible += 1
                    if state.board[(row - 1, col)] == player:
                        in_a_row += 1

                if col < 14 and (row,col+1) in state.board:
                    possible += 1
                    if state.board[(row , col+1)] == player:
                        in_a_row += 1
                    
                if col > 1 and(row,col-1) in state.board:
                    possible += 1
                    if state.board[(row, col-1)] == player:
                        in_a_row += 1
                if row < 15 and col < 14 and (row+1,col+1) in state.board:
                    possible += 1
                    if state.board[(row+1, col+1)] == player:
                        in_a_row += 1
                if row > 1 and col> 1 and (row-1,col-1) in state.board:
                    possible += 1
                    if state.board[(row-1, col-1)] == player:
                        in_a_row += 1
                if row < 15 and col > 1 and (row+1,col-1) in state.board:
                    possible += 1
                    if state.board[(row+1, col-1)] == player:
                        in_a_row += 1
                if row> 1 and col < 14 and (row-1,col+1) in state.board:
                    possible += 1
                    if state.board[(row-1, col+1)] == player:
                        in_a_row += 1
                x_ev += (in_a_row/possible)
    return x_ev / (15*16)

def ab_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, d=2, eval_fn=connect4_eval_bad)

def ab_cutoff_1d(game, state):
    return alpha_beta_cutoff_search(state, game, d=4, eval_fn=connect4_eval)

def ab_cutoff_2b(game, state):
    return alpha_beta_cutoff_search(state, game, d=1, eval_fn=gomoku_eval)


class HW3:
    def __init__(self):
        pass

    def ttt_game(self):
        tt = TicTacToe()
        tt.play_game(alpha_beta_player,query_player)

    def c4_game(self):
        c4 = ConnectFour()
        c4.play_game(ab_cutoff_player,query_player)

    def problem_1d(self):
        # write your code for problem 1d here
        c4 = ConnectFour()
        x = 0
        o = 0
        player = 'X'
        opponent = 'O'
        for i in range(10):
            result = c4.play_game(ab_cutoff_1d, random_player)
            if result == 1:
                x += 1
            print("\n")
        player = 'O'
        opponent = 'X'
        for i in range(10):
            result = c4.play_game(random_player, ab_cutoff_1d)
            if result == 1:
                o += 1
            print("\n")
        return (x,o)

    def problem_2b(self): 
        # write your code for problem 2b here
        gomoku = Gomoku()
        x = 0
        o = 0
        player = 'X'
        opponent = 'O'
        for i in range(10):
            st = time.time()
            result = gomoku.play_game(ab_cutoff_2b, random_player)
            end = time.time()
            print(end - st)
            if result == 1:
                x += 1
            print("\n")
        player = 'O'
        opponent = 'X'
        for i in range(10):
            result = gomoku.play_game(random_player, ab_cutoff_2b)
            if result == 1:
                o += 1
            print("\n")
        return (x,o)
    
def main():
    hw3 = HW3()
    # An example for you to follow to get you started on Games
    # print('Playing Tic-Tac-Toe...')
    # print('======================')
    # hw3.ttt_game()

    ## uncomment the following lines to play connect 4
    # print('Playing Connect 4...')
    # print('====================')
    # hw3.c4_game()

    print('Playing Connect 4...')
    print('====================')
    print( hw3.problem_1d())
    print('Playing Gomoku...')
    print('====================')
    print( hw3.problem_2b())
if __name__ == '__main__':
    main()
