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
    for y in range(m.get_dy()):
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
            else:
                # print("■ ", end='')
                LMD.set_pixel(y, 18-x, 4)
        print()
    time.sleep(0.06)

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

### integer variables: must always be integer!
iScreenDy = 32
iScreenDx = 16
iScreenDw = 3
top = 27
left = iScreenDw + iScreenDx//2 - 2
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
            [2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2]]

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

myCar = [[0, 3, 3, 3],
         [0, 3, 3, 3],
         [0, 3, 3, 3],
         [0, 3, 3, 3]]

obstCar = [[0, 3, 3, 3],
           [0, 3, 3, 3],
           [0, 3, 3, 3],
           [0, 3, 3, 3]]

iScreen = Matrix(arrayMap)
oScreen = Matrix(iScreen)
currBlk = Matrix(myCar)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk

ones = zero
tens = zero
hunds = zero
thnds = zero

oScreen.paste(Matrix(thnds),0,2)
oScreen.paste(Matrix(hunds),0,6)
oScreen.paste(Matrix(tens),0,11)
oScreen.paste(Matrix(ones),0,15)
oScreen.paste(tempBlk, top, left)
LED_init()
draw_matrix(oScreen)
print()

start = timeit.default_timer()

while True:
    now = timeit.default_timer()
    score = round(now-start, 1)*10

    thnds = num_matrix(int(score // 1000))
    hunds = num_matrix(int((score - ((score // 1000)*1000)) // 100))
    tens = num_matrix(int((score - ((score // 1000)*1000) - ((score - ((score // 1000)*1000)) // 100*100)) // 10))
    ones = num_matrix(int(score % 10))

    oScreen = Matrix(iScreen)

    # key = input('Enter a key from [ q (quit), a (left), d (right) : ')
    if keyboard.is_pressed('q'):
        key = 'q'
        print('Game terminated...')
        break
    elif keyboard.is_pressed('a'):    # move left
        key = 'a'
        left -= 1
    elif keyboard.is_pressed('d'):    # move right
        key = 'd'
        left += 1
    # else:               # wrong key
    #     print('Wrong key...')

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(4): # 5 이상
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(Matrix(thnds),0,2)
    oScreen.paste(Matrix(hunds),0,6)
    oScreen.paste(Matrix(tens),0,11)
    oScreen.paste(Matrix(ones),0,15)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen)
    print()

    print(score)
    print(score)
    # ~999.9 secs ( about 16 mins )
    if(score == 9999):
        print("!! You WIN !!")
        break

    if newCarNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newCarNeeded = False
        currBlk = Matrix(myCar)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(6):
            print('!!! Game Over !!!')
            print('Score: {0}'.format(score))
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        oScreen.paste(Matrix(thnds),0,3)
        draw_matrix(oScreen)
        print()
###
### end of the loop
###