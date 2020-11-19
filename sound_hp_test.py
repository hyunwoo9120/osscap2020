import pygame as pg
import time

pg.mixer.init()

crash = pg.mixer.Sound("crash.wav")
engine = pg.mixer.Sound("engine.wav")
race = pg.mixer.Sound("race.wav")

race.play()


HP = 160

class Car:
    def __init__(self, hp, state):
        self.hp = hp
        self.state = state
                                    
    def check_crash(self, state):
        self.state = state
        if (self.state == "crash"):
            return True
        else: return False

player = Car(160, "run")

while(player.hp>=0):
    time.sleep(1)
    engine.play()
    print("===========================")
    print("HP=%d"%player.hp)
    case1=input("State of the car:")
                                                                                                                        
    if player.check_crash(case1):
        player.hp -= 60
        crash.play()
