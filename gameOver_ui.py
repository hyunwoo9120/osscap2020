from matrix import *
from stringIO_test import *
import pygame as pg
import random
import LED_display as LMD
import threading
import time
import timeit
import keyboard

def num_matrix(number, size):
    if size == "small":
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
            
    elif size == "big":
        if number == 0:
            return bigZero
        elif number == 1:
            return bigOne
        elif number == 2:
            return bigTwo
        elif number == 3:
            return bigThree
        elif number == 4:
            return bigFour
        elif number == 5:
            return bigFive
        elif number == 6:
            return bigSix
        elif number == 7:
            return bigSeven
        elif number == 8:
            return bigEight
        elif number == 9:
            return bigNine

def input_score():
    scoreInput = input("점수를 입력하세요: ")
    return int(scoreInput)

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
                LMD.set_pixel(y, 15-x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, 15-x, 1) # Red
            elif array[y][x] == 2:
                LMD.set_pixel(y, 15-x, 2) # Green
            elif array[y][x] == 3:
                LMD.set_pixel(y, 15-x, 3) # Yellow
            elif array[y][x] == 7:
                LMD.set_pixel(y, 15-x, 7) # White


ones = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tens = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
hunds = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
thnds = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# def draw_score(score):
#     thnds = num_matrix(int(score // 1000), "small")
#     hunds = num_matrix(int((score - ((score // 1000)*1000)) // 100), "small")
#     tens = num_matrix(int((score - ((score // 1000)*1000) - ((score - ((score // 1000)*1000)) // 100*100)) // 10), "small")
#     ones = num_matrix(int(score % 10), "small")

def end(name, score, rank):
    arrayStart=[#0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # print user name
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # blank
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # Rank (font size: 5x7)
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # blank
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # home icon
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0],
                # blank
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                # score
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                #blank
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    iScreen = Matrix(arrayStart)
    LED_init()
    draw_matrix(iScreen)

    lmd_str = trans(name, numary, apb, space)
    userName = change_str(lmd_str)
    userName = reshape_str(userName)

    i=0
    j=0
    n = len(lmd_str)
    while True:
        thnds = num_matrix(int(score // 1000), "small")
        hunds = num_matrix(int((score - ((score // 1000)*1000)) // 100), "small")
        tens = num_matrix(int((score - ((score // 1000)*1000) - ((score - ((score // 1000)*1000)) // 100*100)) // 10), "small")
        ones = num_matrix(int(score % 10), "small")

        rankTens = num_matrix(int(rank // 10), "big")
        rankOnes = num_matrix(int(rank % 10), "big")

        if len(lmd_str)<=4:
            char1 = userName[:,0:4]
            char2 = userName[:,4:8]
            char3 = userName[:,8:12]
            char4 = userName[:,12:]
        else:
            
            sliced = userName[:,i:i+16]
            char1 = sliced[:,0:4]
            char2 = sliced[:,4:8]
            char3 = sliced[:,8:12]
            char4 = sliced[:,12:]

        iScreen.paste(Matrix(list(char1)),1,0)
        iScreen.paste(Matrix(list(char2)),1,4)
        iScreen.paste(Matrix(list(char3)),1,8)
        iScreen.paste(Matrix(list(char4)),1,12)

        j+=1
        if(j%10==0):
            i+=1
        if(i==(n+4)*4):
            i=0

        iScreen.paste(Matrix(thnds),26,0)
        iScreen.paste(Matrix(hunds),26,4)
        iScreen.paste(Matrix(tens),26,8)
        iScreen.paste(Matrix(ones),26,12)

        iScreen.paste(Matrix(rankTens),11,2)
        iScreen.paste(Matrix(rankOnes),11,9)

        draw_matrix(iScreen)
        LMD.refresh()

        if keyboard.is_pressed('\n'):
            return "again"
        if keyboard.is_pressed('q'):
            return "quit"
