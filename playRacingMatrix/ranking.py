import pickle
import operator
import os    
import numpy as np

def check_file():
    if(os.path.isfile("./score_list.pickle")):
        print("파일 존재함")
        return True
    else:
        print("파일 없음")
        with open('score_list.pickle', 'xb') as x:
            tempPlayer={" ": 0}
            pickle.dump(tempPlayer, x)
        return True

def load_data():                            #load past data
    with open('score_list.pickle', 'rb') as fo:
        ex_data = pickle.load(fo)
        return ex_data

def save_score(new_board, nickname, score):
    name = nickname
    new_board[name] = int(score)
    with open('score_list.pickle', 'wb') as fw:
        pickle.dump(new_board, fw)

def rank_score(score_chart):                    #rank score chart(sorting)
    ranked_score_board = sorted(score_chart.items(), key = operator.itemgetter(1))
    return ranked_score_board
    
def showing_high_rank(ranked_score_board):
    if len(ranked_score_board)<3:
        return ranked_score_board
    else:
        rank1 = ranked_score_board[-1]
        rank2 = ranked_score_board[-2]
        rank3 = ranked_score_board[-3]
    return rank1, rank2, rank3
    
def your_rank(nickname, ranked_score_board):
    for i in range(len(ranked_score_board)):
        if ranked_score_board[i][0] == nickname:
            return len(ranked_score_board)-i    #player's rank
        else:
            print("Does not found")
