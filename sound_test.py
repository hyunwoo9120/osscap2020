import pygame

import time

 

pygame.mixer.init()

  

crash = pygame.mixer.Sound("./snd/crash.wav")

engine = pygame.mixer.Sound("./snd/engine.wav")

race = pygame.mixer.Sound("./snd/race.wav")

   

race.play()

    

while(1):
    answer=input("State of the car : ")
    if(answer=="crash"):
        crash.play()

    elif(answer=="start"):
        engine.play()
