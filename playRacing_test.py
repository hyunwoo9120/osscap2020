from matrix import *
import random
import LED_display as LMD
import threading
import time
import timeit
import keyboard

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()-4):
        for x in range(3, m.get_dx()-3):
            if array[y][x] == 0:
                # print("□ ", end='')
                LMD.set_pixel(y, 18-x, 0)
            elif array[y][x] == 1:
                # print("■ ", end='')
                LMD.set_pixel(y, 18-x, 3)
            elif array[y][x] == 2:
                # print("■ ", end='')
                LMD.set_pixel(y, 18-x, 3)
            elif array[y][x] == 3:
                # print("■ ", end='')
                LMD.set_pixel(y, 18-x, 4)
            elif array[y][x] ==  7:
                # print("X ", end='')
                LMD.set_pixel(y, 18-x, 1)
            elif array[y][x] ==  8:
                # print("X ", end='')
                LMD.set_pixel(y, 18-x, 5)
            else:
                # print("■ ", end='')
                LMD.set_pixel(y, 18-x, 4)
    time.sleep(0.05)

def num_matrix(number):
    if number == 0:
        return zero
    elif number == 1:
        return one
    elif number == 2:
        return two
    elif number == 3:
        return three
    elif number == 4:
        return four
    elif number == 5:
        return five
    elif number == 6:
        return six
    elif number == 7:
        return seven
    elif number == 8:
        return eight
    elif number == 9:
        return nine

def random_car():
    randNum = random.randrange(4,6)
    if randNum==4:
        randNum = random.randrange(4, 15, 5)
    elif randNum==5:
        randNum = random.randrange(5, 16, 5)
    return randNum
### integer variables: must always be integer!
iScreenDy = 32
iScreenDx = 16
iScreenDw = 3
mytop = 27
myleft = iScreenDw + iScreenDx//2 - 2
obstop = 7
obsleft = random_car()
newCarNeeded = False

arrayMap = [
            #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21

            # timer
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            # gauge
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
            # map
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2], 
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

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

ones = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tens = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
hunds = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
thnds = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

myCar = [[3, 3, 3],
         [3, 3, 3],
         [3, 3, 3],
         [3, 3, 3]]

obstCar = [[8, 8, 8],
           [8, 8, 8],
           [8, 8, 8],
           [8, 8, 8]]

iScreen = Matrix(arrayMap)
oScreen = Matrix(iScreen)

currBlk = Matrix(myCar)
tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
tempBlk = tempBlk + currBlk
tempBlk.print()

obstBlk = Matrix(obstCar)
tempOBlk = iScreen.clip(obstop, obsleft, obstop+obstBlk.get_dy(), obsleft+obstBlk.get_dx())
tempOBlk = tempOBlk + obstBlk

ones = zero
tens = zero
hunds = zero
thnds = zero

oScreen.paste(Matrix(thnds),0,2)
oScreen.paste(Matrix(hunds),0,6)
oScreen.paste(Matrix(tens),0,11)
oScreen.paste(Matrix(ones),0,15)

oScreen.paste(tempOBlk, obstop, obsleft)
oScreen.paste(tempBlk, mytop, myleft)
LED_init()
draw_matrix(oScreen)
print()

start = timeit.default_timer()

while True:
    currBlk.print()
    now = timeit.default_timer()
    score = round(now-start, 1)*10

    thnds = num_matrix(int(score // 1000))
    hunds = num_matrix(int((score - ((score // 1000)*1000)) // 100))
    tens = num_matrix(int((score - ((score // 1000)*1000) - ((score - ((score // 1000)*1000)) // 100*100)) // 10))
    ones = num_matrix(int(score % 10))

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, mytop, myleft)

    if keyboard.is_pressed('q'):
        key = 'q'
        print('Game terminated...')
        break
    elif keyboard.is_pressed('a'):    # move left
        key = 'a'
        myleft -= 1
    elif keyboard.is_pressed('d'):    # move right
        key = 'd'
        myleft += 1
    else:
        key = ' '

    tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    tempBlk.print()
    if tempBlk.equal(5): # 양쪽 차선과 내 자동차가 부딪힌 경우
        if key == 'a': # undo: move right
            myleft += 1
        elif key == 'd': # undo: move left
            myleft -= 1
    
        tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        oScreen.paste(tempBlk, mytop, myleft)
    
    tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    tempBlk.print()
    if tempBlk.anyGreaterThan(6):
        currBlk.print()
        print('!!! Game Over !!!')
        print('Score: {0}'.format(score))
        break

    oScreen = Matrix(iScreen)
    oScreen.paste(Matrix(thnds),0,2)
    oScreen.paste(Matrix(hunds),0,6)
    oScreen.paste(Matrix(tens),0,11)
    oScreen.paste(Matrix(ones),0,15)
    oScreen.paste(tempBlk, mytop, myleft)
    oScreen.paste(tempOBlk, obstop, obsleft)
    
    draw_matrix(oScreen)
    if obstop <32:
        obstop+=1
    else:
        obsleft = random_car()
        newCarNeeded = True

    # ~999.9 secs ( about 16 mins )
    if(score == 9999):
        print("!! You WIN !!")
        break

    if newCarNeeded:
        jScreen = Matrix(oScreen)
        obstop = 7
        newCarNeeded = False
        currBlk = Matrix(myCar)
        tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

        obstBlk = Matrix(obstCar)
        tempOBlk = iScreen.clip(obstop, obsleft, obstop+obstBlk.get_dy(), obsleft+obstBlk.get_dx())
        tempOBlk = tempOBlk + obstBlk
        
        if currBlk.anyGreaterThan(6):
            # currBlk.print()
            print('!!! Game Over !!!')
            print('Score: {0}'.format(score))
            break
        
        oScreen = Matrix(jScreen)
        # oScreen.paste(tempBlk, mytop, myleft)
        draw_matrix(oScreen)
        
###
### end of the loop
###