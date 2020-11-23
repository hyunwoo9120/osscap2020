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
                LMD.set_pixel(y, 18-x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, 18-x, 3)
            elif array[y][x] == 2:
                LMD.set_pixel(y, 18-x, 3)
            elif array[y][x] == 3:
                LMD.set_pixel(y, 18-x, 4)
            elif array[y][x] ==  7:
                LMD.set_pixel(y, 18-x, 1)
            elif array[y][x] ==  8:
                LMD.set_pixel(y, 18-x, 5)
            else:
                LMD.set_pixel(y, 18-x, 4)
    time.sleep(0.04)

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

def newcar_time(currTime):
    randomTime = random.random()+0.2
    checkTime = currTime + randomTime
    return checkTime

### integer variables: must always be integer!
iScreenDy = 32
iScreenDx = 16
iScreenDw = 3
mytop = 27
myleft = iScreenDw + iScreenDx//2 - 2
newCarNeeded = True

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

car1 = Matrix(obstCar)
car2 = Matrix(obstCar)
car3 = Matrix(obstCar)
car4 = Matrix(obstCar)

ones = zero
tens = zero
hunds = zero
thnds = zero

oScreen.paste(Matrix(thnds),0,2)
oScreen.paste(Matrix(hunds),0,6)
oScreen.paste(Matrix(tens),0,11)
oScreen.paste(Matrix(ones),0,15)

oScreen.paste(tempBlk, mytop, myleft)
LED_init()
draw_matrix(oScreen)
print()

start = timeit.default_timer()
check = 0
while True:
    time.sleep(0.01)
    now = timeit.default_timer()
    score = round(now-start, 1)*10

    thnds = num_matrix(int(score // 1000))
    hunds = num_matrix(int((score - ((score // 1000)*1000)) // 100))
    tens = num_matrix(int((score - ((score // 1000)*1000) - ((score - ((score // 1000)*1000)) // 100*100)) // 10))
    ones = num_matrix(int(score % 10))

    if(car1.state):
        car1Blk = iScreen.clip(car1.top, car1.left, car1.top+car1.get_dy(), car1.left+car1.get_dx()) + car1
        oScreen.paste(car1Blk, car1.top, car1.left)
    if(car2.state):
        car2Blk = iScreen.clip(car2.top, car2.left, car2.top+car2.get_dy(), car2.left+car2.get_dx()) + car2
        oScreen.paste(car2Blk, car2.top, car2.left)
    if(car3.state):
        car3Blk = iScreen.clip(car3.top, car3.left, car3.top+car3.get_dy(), car3.left+car3.get_dx()) + car3
        oScreen.paste(car3Blk, car3.top, car3.left)
    if(car4.state):
        car4Blk = iScreen.clip(car4.top, car4.left, car4.top+car4.get_dy(), car4.left+car4.get_dx()) + car4
        oScreen.paste(car4Blk, car4.top, car4.left)

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, mytop, myleft)
    if now > check:
        newCarNeeded=True
    else:
        newCarNeeded=False

    if newCarNeeded:
        print("newCarNeeded")
        check = newcar_time(now)
        oScreen.paste(Matrix(thnds),0,2)
        oScreen.paste(Matrix(hunds),0,6)
        oScreen.paste(Matrix(tens),0,11)
        oScreen.paste(Matrix(ones),0,15)
        newCarNeeded = False
        jScreen = Matrix(oScreen)
        obstop = 7
        obsleft = random_car()

        currBlk = Matrix(myCar)
        tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

        if(not car1.state):
            car1.set_top(obstop)
            car1.set_left(obsleft)
            car1.set_true()
            car1Blk = iScreen.clip(car1.top, car1.left, car1.top+car1.get_dy(), car1.left+car1.get_dx()) + car1
        
        elif(not car2.state):
            car2.set_top(obstop)
            car2.set_left(obsleft)
            car2.set_true()
            car2Blk = iScreen.clip(car2.top, car2.left, car2.top+car2.get_dy(), car2.left+car2.get_dx()) + car2
        
        elif(not car3.state):
            car3.set_top(obstop)
            car3.set_left(obsleft)
            car3.set_true()
            car3Blk = iScreen.clip(car3.top, car3.left, car3.top+car3.get_dy(), car3.left+car3.get_dx()) + car3

        elif(not car4.state):
            car4.set_top(obstop)
            car4.set_left(obsleft)
            car4.set_true()
            car4Blk = iScreen.clip(car4.top, car4.left, car4.top+car4.get_dy(), car4.left+car4.get_dx()) + car4
        
        oScreen = Matrix(jScreen)
        if(car1.state):
            oScreen.paste(car1Blk, car1.top, car1.left)
        if(car2.state):
            oScreen.paste(car2Blk, car2.top, car2.left)
        if(car3.state):
            oScreen.paste(car3Blk, car3.top, car3.left)
        if(car4.state):
            oScreen.paste(car4Blk, car4.top, car4.left)
    
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

    # TODO: 충돌처리!!

    oScreen = Matrix(iScreen)
    oScreen.paste(Matrix(thnds),0,2)
    oScreen.paste(Matrix(hunds),0,6)
    oScreen.paste(Matrix(tens),0,11)
    oScreen.paste(Matrix(ones),0,15)
    oScreen.paste(tempBlk, mytop, myleft)

    if(car1.state):
        if car1.top<32:
            car1.top+=1
        else:
            car1.set_false()
    if(car2.state):
        if car2.top<32:
            car2.top+=1
        else:
            car2.set_false()
    if(car3.state):
        if car3.top<32:
            car3.top+=1
        else:
            car3.set_false()
    if(car4.state):
        if car4.top<32:
            car4.top+=1
        else:
            car4.set_false()

    if(car1.state):
            oScreen.paste(car1Blk, car1.top, car1.left)
    if(car2.state):
            oScreen.paste(car2Blk, car2.top, car2.left)
    if(car3.state):
            oScreen.paste(car3Blk, car3.top, car3.left)
    if(car4.state):
            oScreen.paste(car4Blk, car4.top, car4.left)
    draw_matrix(oScreen)

    # 호옥시라도 점수가 9999가 된다면....
    if(score == 9999):
        print("!! You WIN !!")
        break

    
    
        
###
### end of the loop
###