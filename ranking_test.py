import pickle
import operator    


def initial():
    dic = dict()
    with open('score_list.pickle', 'wb') as fi:
        pickle.dump(dic ,fi)

def load_data():                            #load past data
    with open('score_list.pickle', 'rb') as fo:
        ex_data = pickle.load(fo)
        return ex_data

def save_score(new_board, nickname, score):
    name = nickname
    new_board[name] = float(score)
    with open('score_list.pickle', 'wb') as fw:
        pickle.dump(new_board, fw)
        
def load_score_chart():              
    with open('score_list.pickle', 'rb') as fr:
        load_score_board = pickle.load(fr)
        return load_score_board

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


nickname = input("input your name: ")
score = input("input your score: ")


initial()
new_board = load_data()
print(new_board)
save_score(new_board, nickname,score)
new_board = load_data()
print(new_board)
ranked_score_board = rank_score(new_board)
print(ranked_score_board)
print(showing_high_rank(ranked_score_board))
print("your rank is :",your_rank(nickname, ranked_score_board))

#return showing_high_rank(ranked_score_board), your_rank(nickname, ranked_score_board)
