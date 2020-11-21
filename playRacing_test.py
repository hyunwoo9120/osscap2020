from matrix import *
import random
import LED_display as LMD
import threading
import time

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
                print("□ ", end='')
                LMD.set_pixel(y, 18-x, 0)
            elif array[y][x] == 1:
                print("■ ", end='')
                LMD.set_pixel(y, 18-x, 3)
            elif array[y][x] == 2:
                print("■ ", end='')
                LMD.set_pixel(y, 18-x, 3)
            elif array[y][x] == 3:
                print("■ ", end='')
                LMD.set_pixel(y, 18-x, 4)
            elif array[y][x] ==  7:
                print("X ", end='')
                LMD.set_pixel(y, 18-x, 1)
            else:
                print("■ ", end='')
                LMD.set_pixel(y, 18-x, 4)
        print()

### integer variables: must always be integer!
iScreenDy = 32
iScreenDx = 16
iScreenDw = 3
top = 27
left = iScreenDw + iScreenDx//2 - 2
newCarNeeded = False

arrayMap = [
            #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21

            # timer 2379
            #[0, 0, 0, 0, 7, 7, 7, 0, 7, 7, 7, 0, 7, 7, 7, 0, 7, 7, 7, 0, 0, 0], 
            #[0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 0, 0], 
            #[0, 0, 0, 0, 7, 7, 7, 0, 7, 7, 7, 0, 7, 0, 7, 0, 7, 7, 7, 0, 0, 0], 
            #[0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0], 
            #[0, 0, 0, 0, 7, 7, 7, 0, 7, 7, 7, 0, 0, 0, 7, 0, 7, 7, 7, 0, 0, 0],
            [0, 0, 0, 7, 7, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 7, 0, 0, 7, 7, 0, 0, 7, 7, 0, 7, 0, 7, 0, 0, 0, 0], 
            [0, 0, 0, 7, 7, 7, 0, 7, 7, 7, 0, 0, 0, 7, 0, 7, 7, 7, 0, 0, 0, 0], 
            [0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0], 
            [0, 0, 0, 7, 7, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0], 
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
print("top: {0}, left: {1}, top+y: {2}, left+x: {3}". format(top, left, top+currBlk.get_dy(), left+currBlk.get_dx()))
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
LED_init()
draw_matrix(oScreen)
print()

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right) : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a':    # move left
        left -= 1
    elif key == 'd':    # move right
        left += 1
    else:               # wrong key
        print('Wrong key...')

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
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen)
    print()

    if newCarNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newCarNeeded = False
        currBlk = Matrix(myCar)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(4):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen)
        print()
        
###
### end of the loop
###