import pygame as pg
import time

pg.mixer.init()

crash = pg.mixer.Sound("./snd/crash.wav")
engine = pg.mixer.Sound("./snd/engine.wav")
race = pg.mixer.Sound("./snd/race.wav")
destruct = pg.mixer.Sound("./snd/destruct.wav")
get_item = pg.mixer.Sound("./snd/item.wav")

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

    def get_item(self, item_type):
        if (item_type == "hp"):
            return 1
        if (item_type == "destruct"):
            return 0
        
player = Car(160, "run")

while(player.hp>0):
    time.sleep(1)
    engine.play()
    
    print("===========================")
    if (player.hp>=160):
        player.hp = 160
    print("HP=%d"%player.hp)
    
    case1=input("State of the car(crash):")
    
    if player.check_crash(case1):
        player.hp -= 60
        crash.play()

    item=input("What type of item?(hp/destruct):")
    
    if (player.get_item(item)==1):
        get_item.play()
        player.hp += 20

    if (player.get_item(item)==0):
        print("All cars are destructed")
        destruct.play()
        
        


