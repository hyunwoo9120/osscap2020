import pickle
import operator    
import numpy as np

#score는 게임오버 후 게임에서 받아오기

apb = {'A': [[0,7,7,7], [0,7,0,7], [0,7,7,7], [0,7,0,7], [0,7,0,7]],
       'B': [[0,7,7,0], [0,7,0,7], [0,7,7,7], [0,7,0,7], [0,7,7,0]],
       'C': [[0,7,7,7], [0,7,0,0], [0,7,0,0], [0,7,0,0], [0,7,7,7]],
       'D': [[0,7,7,0], [0,7,0,7], [0,7,0,7], [0,7,0,7], [0,7,7,0]],
       'E': [[0,7,7,7], [0,7,0,0], [0,7,7,7], [0,7,0,0], [0,7,7,7]],
       'F': [[0,7,7,7], [0,7,0,0], [0,7,7,7], [0,7,0,0], [0,7,0,0]],
       'G': [[0,7,7,7], [0,7,0,0], [0,7,0,7], [0,7,0,7], [0,7,7,7]],
       'H': [[0,7,0,7], [0,7,0,7], [0,7,7,7], [0,7,0,7], [0,7,0,7]],
       'I': [[0,7,7,7], [0,0,7,0], [0,0,7,0], [0,0,7,0], [0,7,7,7]],
       'J': [[0,0,0,7], [0,0,0,7], [0,0,0,7], [0,0,0,7], [0,7,7,7]],
       'K': [[0,7,0,7], [0,7,0,7], [0,7,7,0], [0,7,0,7], [0,7,0,7]],
       'L': [[0,7,0,0], [0,7,0,0], [0,7,0,0], [0,7,0,0], [0,7,7,7]],
       'M': [[0,7,0,7], [0,7,7,7], [0,7,7,7], [0,7,0,7], [0,7,0,7]],
       'N': [[0,7,7,7], [0,7,0,7], [0,7,0,7], [0,7,0,7], [0,7,0,7]],
       'O': [[0,0,7,0], [0,7,0,7], [0,7,0,7], [0,7,0,7], [0,0,7,0]],
       'P': [[0,7,7,7], [0,7,0,7], [0,7,7,7], [0,7,0,0], [0,7,0,0]],
       'Q': [[0,7,7,7], [0,7,0,7], [0,7,7,7], [0,0,0,7], [0,0,0,7]],
       'R': [[0,7,7,7], [0,7,0,7], [0,7,7,0], [0,7,0,7], [0,7,0,7]],
       'S': [[0,0,7,7], [0,7,0,0], [0,7,7,7], [0,0,0,7], [0,7,7,0]],
       'T': [[0,7,7,7], [0,0,7,0], [0,0,7,0], [0,0,7,0], [0,0,7,0]],
       'U': [[0,7,0,7], [0,7,0,7], [0,7,0,7], [0,7,0,7], [0,7,7,7]],
       'V': [[0,7,0,7], [0,7,0,7], [0,7,0,7], [0,7,7,7], [0,0,7,0]],
       'W': [[0,7,0,7], [0,7,0,7], [0,7,7,7], [0,7,7,7], [0,7,0,7]],
       'X': [[0,7,0,7], [0,7,0,7], [0,0,7,0], [0,7,0,7], [0,7,0,7]],
       'Y': [[0,7,0,7], [0,7,0,7], [0,7,7,7], [0,0,0,7], [0,7,7,7]],
       'Z': [[0,7,7,7], [0,0,0,7], [0,0,7,0], [0,7,0,0], [0,7,7,7]]}

zero = [[0, 7, 7, 7],
        [0, 7, 0, 7],
        [0, 7, 0, 7],
        [0, 7, 0, 7],
        [0, 7, 7, 7]]
one = [[0, 0, 0, 7],
       [0, 0, 7, 7],
       [0, 0, 0, 7],
       [0, 0, 0, 7],
       [0, 0, 0, 7]]
two = [[0, 7, 7, 7],
       [0, 0, 0, 7],
       [0, 7, 7, 7],
       [0, 7, 0, 0],
       [0, 7, 7, 7]]
three = [[0, 7, 7, 7],
         [0, 0, 0, 7],
         [0, 7, 7, 7],
         [0, 0, 0, 7],
         [0, 7, 7, 7]]
four = [[0, 7, 0, 7],
        [0, 7, 0, 7],
        [0, 7, 7, 7],
        [0, 0, 0, 7],
        [0, 0, 0, 7]]
five = [[0, 7, 7, 7],
        [0, 7, 0, 0],
        [0, 7, 7, 7],
        [0, 0, 0, 7],
        [0, 7, 7, 7]]
six = [[0, 7, 7, 7],
       [0, 7, 0, 0],
       [0, 7, 7, 7],
       [0, 7, 0, 7],
       [0, 7, 7, 7]]
seven = [[0, 7, 7, 7],
         [0, 7, 0, 7],
         [0, 7, 0, 7],
         [0, 0, 0, 7],
         [0, 0, 0, 7]]
eight = [[0, 7, 7, 7],
         [0, 7, 0, 7],
         [0, 7, 7, 7],
         [0, 7, 0, 7],
         [0, 7, 7, 7]]
nine = [[0, 7, 7, 7],
        [0, 7, 0, 7],
        [0, 7, 7, 7],
        [0, 0, 0, 7],
        [0, 7, 7, 7]]

numary=[zero, one, two, three, four, five, six, seven, eight, nine]

space = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]



def initial():
    initialization = input("Do you want initialization?(y / n)")
    if (initialization == 'y'):
        dic = dict()
        with open('score_list.pickle', 'wb') as fi:
            pickle.dump(dic ,fi)
    else:
        pass

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


def InputAndCheck():
    while(1):
        check = True
        string = input("Type your nickname(you can only type capital letter, number and space): ")
        for cn in string:
            if ((cn.isupper()==False) and (cn.isdigit()==False)) and (cn != " "):
                check = False
        if (check == True):
            return string
            break
        else:
            print("Wrong type")
        
def trans(string, numary, apb, space):
    strlist = [ cn for cn in string]
    Olist = list()
    
    for cd in strlist:
        if(cd.isdigit()==True):
            Olist.append(numary[int(cd)])
        elif(cd.isupper()==True):
            Olist.append(apb[cd])
        elif(cd == " "):
            Olist.append(space)
        else:
            print("Error")

    return Olist

def change_str(Olist):
    n = len(Olist)
    if n<=4:
        for i in range(4-n):
            Olist.append(space)
        return Olist
    else :
        # TODO: 앞뒤로 가로길이(16)만큼 여백 만들어서 slicing한 배열을 리턴하기
        newList = list()
        for i in range(4):
            newList.append(space)
        for j in range(n):
            newList.append(Olist[j])
        for k in range(4):
            newList.append(space)
        return newList

def reshape_str(changed_str):
    oneline = list()
    for i in range(5):
        for j in range(len(changed_str)):
            oneline.extend(changed_str[j][i])
    return np.reshape(oneline,(5,-1))






# 게임이 끝난 후 점수는 그대로 받고, 닉넴임은 그 이후 입력 받음.
# 그 후 플레이어 이름과 랭킹을 보여주고 게임 시작화면에서는 높은 순위만을 보여줌.

score = 3000
initial()
nickname = InputAndCheck()
new_board = load_data()
save_score(new_board, nickname, score)
ranked_score_board = rank_score(load_data())
high_rank = list(showing_high_rank(ranked_score_board))
y_rank = your_rank(nickname, ranked_score_board)


#플레이어 랭킹
p_rank = reshape_str(change_str(trans(str(y_rank), numary, apb, space)))
player = reshape_str(change_str(trans(str(nickname), numary, apb, space)))
# p_rank는 플레이어의 순위, player는 플레이어의 닉넴임을 배열화함.



#높은 랭킹 3순위
hr_arr = [[0, 0],[0, 0],[0, 0]]

for i in range(len(high_rank)):
    for k in range(2):
        hr_arr[i][k] = reshape_str(change_str(trans(str(high_rank[i][k]), numary, apb, space)))
        print(hr_arr[i][k])
#high_rank = [(n1,s1), (n2,s2), (n3,s3)]
#hr_s 는 high_rank를 배열화해서 다시 넣음.
