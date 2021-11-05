from sys import winver

from numpy.core.defchararray import count
from state import State, State_2
import time
from importlib import import_module
  
def main(player_X, player_O, rule = 1):
    dict_player = {1: 'X', -1: 'O'}
    if rule == 1:
        cur_state = State()
    else:
        cur_state = State_2()
    turn = 1    

    limit = 81
    remain_time_X = 120
    remain_time_O = 120
    
    player_1 = import_module(player_X)
    player_2 = import_module(player_O)
    
    winner = None

    while turn <= limit:
        #print("turn:", turn, end='\n\n')
        if cur_state.game_over:
            winner = dict_player[cur_state.player_to_move * -1]
            #print("winner:", dict_player[cur_state.player_to_move * -1])
            break
        
        start_time = time.time()
        if cur_state.player_to_move == 1:
            new_move = player_1.select_move(cur_state, remain_time_X)
            elapsed_time = time.time() - start_time
            remain_time_X -= elapsed_time
        else:
            new_move = player_2.select_move(cur_state, remain_time_O)
            elapsed_time = time.time() - start_time
            remain_time_O -= elapsed_time
            
        if new_move == None:
            break
        
        if remain_time_X < 0 or remain_time_O < 0:
            #print("out of time")
            #print("winner:", dict_player[cur_state.player_to_move * -1])
            break
                
        if elapsed_time > 10.0:
            #print("elapsed time:", elapsed_time)
            #print("winner: ", dict_player[cur_state.player_to_move * -1])
            break
        
        cur_state.act_move(new_move)
        #print(cur_state)
        
        turn += 1

    #print("X:", cur_state.count_X)
    #print("O:", cur_state.count_O)
    if winner == None:
        if cur_state.count_X > cur_state.count_O:
            winner = 'X'
        elif cur_state.count_O > cur_state.count_X:
            winner = 'O'
        else:
            winner = 'DRAW'

    cur_state.player_to_move = State.O
    new_move = player_2.select_move(cur_state, remain_time_O, winner)
        
    return winner

# from _MSSV import QLearning 
# def learn(n):
#     xwin = 0
#     owin = 0
#     for i in range(n):
#         if i % 1000 == 0:
#             print(i)
#         w = main('random_agent','_MSSV')
#         if w == 'X':
#             xwin += 1
#         if w == 'O':
#             owin += 1
#     print(f"X win: {xwin}, O win: {owin}")
#     QLearning.save_values()


learn(100)

#main( '_MSSV', 'random_agent')

 
