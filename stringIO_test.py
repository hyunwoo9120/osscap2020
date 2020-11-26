import numpy as np
# 문자열을 입력 받으면 배열로 출력
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
    n = len(string)
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
    print(len(Olist))
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


# lmd_str = trans(InputAndCheck(), numary, apb, space)
# for c in change_str(lmd_str):
#     print()
#     for y in range(len(c)):
#         print()
#         for x in range(len(c[y])):
#             if c[y][x] == 0:
#                 print("□", end='')
#             elif c[y][x] == 7:
#                 print("■", end='')
        
# print()

