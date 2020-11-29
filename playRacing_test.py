from matrix import *
from stringIO_test import *
import random
import pygame as pg
import LED_display as LMD
import threading
import time
import timeit
import keyboard
pg.mixer.init()
race = pg.mixer.Sound("./snd/race.wav")
crash = pg.mixer.Sound("./snd/crash.wav")
heal = pg.mixer.Sound("./snd/item.wav")

def play_sound(sound, on):
    if on:
        if sound == 'race':
            race.play(-1)
        elif sound == 'crash':
            crash.play()
        elif sound == 'heal':
            heal.play()
        elif sound == 'stop':
            print("called stop")
            race.stop()

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
                LMD.set_pixel(y, 18-x, 0) # black
            elif array[y][x] == 1:
                LMD.set_pixel(y, 18-x, 3) # yellow
            elif array[y][x] == 10:
                LMD.set_pixel(y, 18-x, 3) # yellow
            elif array[y][x] == 3:
                LMD.set_pixel(y, 18-x, 4) # blue
            elif array[y][x] ==  7:
                LMD.set_pixel(y, 18-x, 7) # white
            elif array[y][x] ==  8:
                LMD.set_pixel(y, 18-x, 5)
            elif array[y][x] == 11:
                LMD.set_pixel(y, 18-x, 1) # Red
            elif array[y][x] == 12:
                LMD.set_pixel(y, 18-x, 1) # Red
            elif array[y][x] == 13:
                LMD.set_pixel(y, 18-x, 2) # green
            elif array[y][x] == 14:
                LMD.set_pixel(y, 18-x, 2) # green
            elif array[y][x] == 15:
                LMD.set_pixel(y, 18-x, 4) # blue
            elif array[y][x] == 16:
                LMD.set_pixel(y, 18-x, 4) # blue
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

def item_time(currTime):
    randomTime = random.randrange(5,15)
    itemTime = currTime + randomTime
    return itemTime


def play(on):
### integer variables: must always be integer!
    iScreenDy = 32
    iScreenDx = 16
    iScreenDw = 3
    mytop = 27
    myleft = iScreenDw + iScreenDx//2 - 2
    newCarNeeded = True
    newItemNeeded = True

    arrayMap = [
                #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21

                # timer
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                # gauge
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                # map
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10],
                [10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                [10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10], 
                
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    gauge = [[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
             [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]]  # 160

    ones = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    tens = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    hunds = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    thnds = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    myCar = [[15, 15, 15],
             [15, 15, 15],
             [15, 15, 15],
             [15, 15, 15]]

    obstCar = [[8, 8, 8],
            [8, 8, 8],
            [8, 8, 8],
            [8, 8, 8]]

    oitem = [[7, 7],
    [7, 7]]

    iScreen = Matrix(arrayMap)
    oScreen = Matrix(iScreen)

    currBlk = Matrix(myCar)
    tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
    tempBlk = tempBlk + currBlk

    car1 = Matrix(obstCar)
    car2 = Matrix(obstCar)
    car3 = Matrix(obstCar)
    car4 = Matrix(obstCar)
    item = Matrix(oitem)

    ones = zero
    tens = zero
    hunds = zero
    thnds = zero

    oScreen.paste(Matrix(thnds),0,3)
    oScreen.paste(Matrix(hunds),0,7)
    oScreen.paste(Matrix(tens),0,11)
    oScreen.paste(Matrix(ones),0,15)
    oScreen.paste(Matrix(gauge),5,3)

    oScreen.paste(tempBlk, mytop, myleft)
    play_sound('race', on)
    LED_init()
    draw_matrix(oScreen)
    print()

    e=0
    f=0
    hp = 160
    hp_time = 0
    start = timeit.default_timer()
    check = 0
    itemCheck = 0

    while True:

        if(hp<50):
            for i in range(len(myCar)):
                for j in range(len(myCar[i])):
                    myCar[i][j]=11

        elif(hp<110):
            for i in range(len(myCar)):
                for j in range(len(myCar[i])):
                    myCar[i][j]=13

        elif(hp<=160):
            for i in range(len(myCar)):
                for j in range(len(myCar[i])):
                    myCar[i][j]=15



        currBlk = Matrix(myCar)
        tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

        e+=1
        if(e%3==0):
            if(f%6<2):
                arrayMap.insert(7,[10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10])
                del arrayMap[31]
            else:
                arrayMap.insert(7,[10, 10, 10, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 10, 10, 10, 10])
                del arrayMap[31]
            f+=1

        iScreen = Matrix(arrayMap)
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, mytop, myleft)

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
        if(item.state):
            itemBlk = iScreen.clip(item.top, item.left, item.top+item.get_dy(), item.left+item.get_dx()) + item
            oScreen.paste(itemBlk, item.top, item.left)

        if now > check:
            newCarNeeded=True
        else:
            newCarNeeded=False

        if newCarNeeded:
            print("newCarNeeded")
            check = newcar_time(now)
            oScreen.paste(Matrix(thnds),0,3)
            oScreen.paste(Matrix(hunds),0,7)
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

        if now > itemCheck:
            newItemNeeded=True
        else:
            newItemNeeded=False

        if newItemNeeded:
            newItemNeeded = False
            item.set_true()
            itemCheck = item_time(now)
            itemtop = 7
            itemleft = random_car()
            item.set_top(itemtop)
            item.set_left(itemleft)

            itemBlk = iScreen.clip(item.top, item.left, item.top+item.get_dy(), item.left+item.get_dx()) + item
            if(item.state):
                oScreen.paste(itemBlk, item.top, item.left)
        


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

        if tempBlk.anyGreaterThan(20): # 양쪽 차선과 내 자동차가 부딪힌 경우
            if key == 'a': # undo: move right
                myleft += 1
            elif key == 'd': # undo: move left
                myleft -= 1
        
            tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
            oScreen.paste(tempBlk, mytop, myleft)
        
        tempBlk = iScreen.clip(mytop, myleft, mytop+currBlk.get_dy(), myleft+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

        # TODO: 충돌처리!!
        if(car1.state):
            if currBlk.check_crash(mytop,myleft,car1Blk,car1.top,car1.left) and now>hp_time+1:
                hp_time = timeit.default_timer()
                play_sound('crash', on)
                hp -= 60
                print("hp: ",hp)
                for i in range((160-hp)//10):
                    if hp <0:
                        for i in range(len(gauge)):
                            for j in range(len(gauge[i])):
                                gauge[i][j]=0
                    else:
                        gauge[0][i]=0
                        gauge[1][i]=0
            if(hp<=0):
                break
        if(car2.state):
            if currBlk.check_crash(mytop,myleft,car2Blk,car2.top,car2.left) and now>hp_time+1:
                hp_time = timeit.default_timer()
                play_sound('crash', on)
                hp -= 60
                print("hp: ",hp)
                for i in range((160-hp)//10):
                    if hp <0:
                        for i in range(len(gauge)):
                            for j in range(len(gauge[i])):
                                gauge[i][j]=0
                    else:
                        gauge[0][i]=0
                        gauge[1][i]=0
            if(hp<=0):
                break
        if(car3.state):
            if currBlk.check_crash(mytop,myleft,car3Blk,car3.top,car3.left) and now>hp_time+1:
                hp_time = timeit.default_timer()
                play_sound('crash', on)
                hp -= 60
                print("hp: ",hp)
                for i in range((160-hp)//10):
                    if hp <0:
                        for i in range(len(gauge)):
                            for j in range(len(gauge[i])):
                                gauge[i][j]=0
                    else:
                        gauge[0][i]=0
                        gauge[1][i]=0
            if(hp<=0):
                break
        if(car4.state):
            if currBlk.check_crash(mytop,myleft,car4Blk,car4.top,car4.left) and now>hp_time+1:
                hp_time = timeit.default_timer()
                play_sound('crash', on)
                hp -= 60
                print("hp: ",hp)
                for i in range((160-hp)//10):
                    if hp <0:
                        for i in range(len(gauge)):
                            for j in range(len(gauge[i])):
                                gauge[i][j]=0
                    else:
                        gauge[0][i]=0
                        gauge[1][i]=0
            if(hp<=0):
                break

        if(item.state):
            if currBlk.check_crash(mytop,myleft,itemBlk,item.top,item.left) and now>hp_time+1:
                hp_time = timeit.default_timer()
                play_sound('heal', on)
                hp += 40
                if hp >160:
                    hp = 160
                print("hp: ",hp)
                for i in range(hp//10):
                    gauge[0][15-i]=1
                    gauge[1][15-i]=1

        if(hp<50):
            for i in range(len(gauge)):
                for j in range(len(gauge[i])):
                    if (gauge[i][j]!=0):
                        gauge[i][j]=11

        elif(hp<110):
            for i in range(len(gauge)):
                for j in range(len(gauge[i])):
                    if (gauge[i][j]!=0):
                        gauge[i][j]=13

        elif(hp<=160):
            for i in range(len(gauge)):
                for j in range(len(gauge[i])):
                    if (gauge[i][j]!=0):
                        gauge[i][j]=15

        oScreen = Matrix(iScreen)
        oScreen.paste(Matrix(thnds),0,3)
        oScreen.paste(Matrix(hunds),0,7)
        oScreen.paste(Matrix(tens),0,11)
        oScreen.paste(Matrix(ones),0,15)
        oScreen.paste(tempBlk, mytop, myleft)
        oScreen.paste(Matrix(gauge),5,3)

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
        if(item.state):
            if item.top<32:
                item.top+=1
            else:
                item.set_false()
        

        if(car1.state):
                oScreen.paste(car1Blk, car1.top, car1.left)
        if(car2.state):
                oScreen.paste(car2Blk, car2.top, car2.left)
        if(car3.state):
                oScreen.paste(car3Blk, car3.top, car3.left)
        if(car4.state):
                oScreen.paste(car4Blk, car4.top, car4.left)
        if(item.state):
                oScreen.paste(itemBlk, item.top, item.left)
        draw_matrix(oScreen)

        # 호옥시라도 점수가 9999가 된다면....
        if(score == 9999):
            print("!! You WIN !!")
            break
    time.sleep(0.7)
    play_sound('stop',on)
    return score
    
    
        
###
### end of the loop
###
