from matrix import *
from stringIO import *
import pygame as pg
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
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                # print("□ ", end='')
                LMD.set_pixel(y, 15-x, 0)
            elif array[y][x] == 1:
                # print("■ ", end='')
                LMD.set_pixel(y, 15-x, 1)
            elif array[y][x] == 2:
                # print("■ ", end='')
                LMD.set_pixel(y, 15-x, 2)
            elif array[y][x] == 5:
                # print("■ ", end='')
                LMD.set_pixel(y, 15-x, 5)
            elif array[y][x] == 3:
                # print("■ ", end='')
                LMD.set_pixel(y, 15-x, 3)
            elif array[y][x] == 6:
                # print("■ ", end='')
                LMD.set_pixel(y, 15-x, 6)
            else:
                LMD.set_pixel(y, 15-x, 7)
def start(rank1, rank2, rank3):
    arrayStart=[#0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

                # Rank1 (2,0)
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

                # Rank2 (9,0)
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                
                # Rank3 (16,0)
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    play = [[0, 7, 7, 0, 0, 7, 0, 0, 0, 7, 0, 0, 7, 0, 7, 0],
            [0, 7, 0, 7, 0, 7, 0, 0, 7, 0, 7, 0, 7, 0, 7, 0],
            [0, 7, 7, 0, 0, 7, 0, 0, 7, 7, 7, 0, 0, 7, 0, 0],
            [0, 7, 0, 0, 0, 7, 7, 0, 7, 0, 7, 0, 0, 7, 0, 0]]
    sound_on = [[0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
                [0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 2, 0, 0, 7, 7, 0],
                [0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 7, 7, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 7, 7, 0, 0]]
    sound_off =[[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]

    iScreen = Matrix(arrayStart)
    iScreen.paste(Matrix(play),20,0)
    iScreen.paste(Matrix(sound_on),26,0)
    LED_init()
    draw_matrix(iScreen)

    lmd_str = trans(rank1, numary, apb, space)
    userName = change_str(lmd_str)
    rOne = reshape_str(userName)
    for x in range(len(rOne)):
        for y in range(len(rOne[x])):
            if rOne[x][y] != 0:
                rOne[x][y] = 5

    n = len(lmd_str)

    lmd_str = trans(rank2, numary, apb, space)
    userName = change_str(lmd_str)
    rTwo = reshape_str(userName)
    for x in range(len(rTwo)):
        for y in range(len(rTwo[x])):
            if rTwo[x][y] != 0:
                rTwo[x][y] = 3

    if n<len(lmd_str):
        n = len(lmd_str)

    lmd_str = trans(rank3, numary, apb, space)
    userName = change_str(lmd_str)
    rThree = reshape_str(userName)
    for x in range(len(rThree)):
        for y in range(len(rThree[x])):
            if rThree[x][y] != 0:
                rThree[x][y] = 6

    if n<len(lmd_str):
        n = len(lmd_str)

    on = True
    print(on)

    pg.mixer.init()
    race = pg.mixer.Sound("./snd/race.wav")
    
    race.play()

    i=0
    j=0
    while True:
        if len(rank1)<=4:
            char11 = rOne[:,0:4]
            char12 = rOne[:,4:8]
            char13 = rOne[:,8:12]
            char14 = rOne[:,12:]
        else:
            sliced = rOne[:,i:i+16]
            char11 = sliced[:,0:4]
            char12 = sliced[:,4:8]
            char13 = sliced[:,8:12]
            char14 = sliced[:,12:]

        if len(rank2)<=4:        
            char21 = rTwo[:,0:4]
            char22 = rTwo[:,4:8]
            char23 = rTwo[:,8:12]
            char24 = rTwo[:,12:]
        else:    
            sliced = rTwo[:,i:i+16]
            char21 = sliced[:,0:4]
            char22 = sliced[:,4:8]
            char23 = sliced[:,8:12]
            char24 = sliced[:,12:]

        if len(rank3)<=4:        
            char31 = rThree[:,0:4]
            char32 = rThree[:,4:8]
            char33 = rThree[:,8:12]
            char34 = rThree[:,12:]
        else:
            sliced = rThree[:,i:i+16]
            char31 = sliced[:,0:4]
            char32 = sliced[:,4:8]
            char33 = sliced[:,8:12]
            char34 = sliced[:,12:]


        iScreen.paste(Matrix(list(char11)),1,0)
        iScreen.paste(Matrix(list(char12)),1,4)
        iScreen.paste(Matrix(list(char13)),1,8)
        iScreen.paste(Matrix(list(char14)),1,12)
        iScreen.paste(Matrix(list(char21)),7,0)
        iScreen.paste(Matrix(list(char22)),7,4)
        iScreen.paste(Matrix(list(char23)),7,8)
        iScreen.paste(Matrix(list(char24)),7,12)
        iScreen.paste(Matrix(list(char31)),13,0)
        iScreen.paste(Matrix(list(char32)),13,4)
        iScreen.paste(Matrix(list(char33)),13,8)
        iScreen.paste(Matrix(list(char34)),13,12)

        j+=1
        if(j%10==0):
            i+=1
        if(i==(n+4)*4):
            i=0

        if keyboard.is_pressed('o'):
            on = not on
            print(on)
            print("key 'o' is pressed!")
            time.sleep(0.2)
            if on:
                print("on: ", on)
                iScreen.paste(Matrix(sound_on),26,0)
                pg.mixer.unpause()
            else:
                print("off: ", on)
                iScreen.paste(Matrix(sound_off),26,0)
                pg.mixer.pause()

        if keyboard.is_pressed('\n'):
            clear = input()
            time.sleep(0.3)
            break

        draw_matrix(iScreen)
        LMD.refresh()
    clear = input()
    username = input("사용자의 이름을 입력하세요: ")
    if on:
        race.stop()
    return username, on
