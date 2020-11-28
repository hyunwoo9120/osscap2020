from matrix import *
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
            elif array[y][x] == 7:
                # print("■ ", end='')
                LMD.set_pixel(y, 15-x, 7)
def start():
    arrayStart=[#0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
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
    on = True
    print(on)

    pg.mixer.init()
    race = pg.mixer.Sound("./snd/race.wav")
    
    race.play()

    while True:
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

    if on:
        race.stop()
    return on
