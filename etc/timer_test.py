from matrix import *
import random
import LED_display as LMD
import threading
import time
import timeit


def LED_init():
    thread = threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return


def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(3, m.get_dx()-3):
            if array[y][x] == 0:
                LMD.set_pixel(y, 18-x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, 18-x, 3)
            elif array[y][x] == 2:
                LMD.set_pixel(y, 18-x, 3)
            elif array[y][x] == 3:
                LMD.set_pixel(y, 18-x, 4)
            elif array[y][x] == 7:
                LMD.set_pixel(y, 18-x, 1)
            else:
                LMD.set_pixel(y, 18-x, 4)
        print()

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

arrayTime = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]

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


iScreen = Matrix(arrayTime)
oScreen = Matrix(iScreen)
oScreen.paste(Matrix(thnds),0,3)
oScreen.paste(Matrix(hunds),0,7)
oScreen.paste(Matrix(tens),0,11)
oScreen.paste(Matrix(ones),0,15)
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
    oScreen.paste(Matrix(thnds),0,3)
    oScreen.paste(Matrix(hunds),0,7)
    oScreen.paste(Matrix(tens),0,11)
    oScreen.paste(Matrix(ones),0,15)
    draw_matrix(oScreen)

    print(score)
    # ~999.9 secs ( about 16 mins )
    if(score == 9999):
        print("!! You WIN !!")
        break

print(score)
