import pygame as pg
import random
from time import sleep

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)


#자동차 객체 생성
class Car:
    image_car = ['RacingCar01.png','RacingCar02.png','RacingCar03.png','RacingCar04.png','RacingCar05.png','RacingCar06.png','RacingCar07.png','RacingCar08.png','RacingCar09.png','RacingCar10.png','RacingCar11.png','RacingCar12.png','RacingCar13.png','RacingCar14.png','RacingCar15.png','RacingCar16.png','RacingCar17.png','RacingCar18.png','RacingCar19.png','RacingCar20.png']

    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image = ""
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy

    def load_image(self):
        self.image = pg.image.load(random.choice(self.image_car))
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rext().size[1]

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx
    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self):
        if self.x+self.width > WINDOW_WIDTH or self.x < 0:
            self.x -= self.dx
                                                          
    def check_crash(self, car):
        if (self.x + self.width > car.x) and (self.x < car.x) and (self.y < car.y+car.height) and (self.y + self.height > car.y):
            return True
        else:
            return False

#메인 메뉴 설계
def draw_main_menu():
    draw_x = (WINDWO_WIDTH / 2) - 200
    draw_y = WINDOW_HEIGHT / 2
    image_intro = pg.image.load('PyCar.png')
    screen.blit(image_intro, [draw_x, draw_y])
    font_40 = pg.font.SysFont("FixedSys", 40, True, False)
    font_30 = pg.font.SysFont("FixedSys", 30, True, False)
    text_title = font_40.render("--Pyracing--", True, BLACK)
    screen.blit(text_title, [draw_x, draw_y])
    text_score = font_40.render("Score: "+ str(score), True, WHITE)
    screen.blit(text_score, [draw_x, draw_y + 70])
    text_start = font_30.render("Press Space key to start!!", True, RED)
    screen.blit(text_start, [draw_x, draw_y+140])
    pg.display.flip()
    
    #점수 처리
def draw_score():
    font_30 = pg.font.SysFont("FixedSys", 30, True, False)
    text_score = font_30.render("Score: "+ str(score), True, BLACK)
    screen.blit(text_score, [15, 15])


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption("PyRacing")
    clock = pg.time.Clock()

    pg.mixer.music.load('race.wav')
    sound_crach = pg.mixer.Sound('carsh.wav')
    sound_engine = pg.mixer.Sound('engine.wav')

    player = Car(WINDOW_WIDTH/2, (WINDOW_HEIGHT - 150), 0, 0)
    player.load_image()

    cars = []
    car_count = 3
    
    for i in range(car_count):                #자동차를 3개만 나올 수 있도록 설정.
        x = random.randrange(0, WINDOW_WIDTH)
        y = random.randrange(-150, -50)
        car = Car(x, y, 0, random.randint(5, 10))
        car.load_image()
        cars.append(car)
        
    lanes = []                                   #속도감을 보여주기 위한 차선의 움직임 표현
    lane_width = 10
    lane_height = 80
    lane_margin = 20
    lane_count = 20
    lane_x = (WINDOW_WIDTH - lane_width)/2
    lane_y = -10
    for i in range(lane_count):
        lanes.append([lane_x, lane_y])
        lane_y += lane_height + lane_margin
 
score = 0
crash = True
game_on = True

while game_on:                                              #메인 게임, 충돌 구현
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_on = False

        if crash:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                crash = False
                for i in range(car_count):
                    cars[i].x = random.randrange(0, WINDOW_WIDTH-cars[i].width)
                    car[i].y = random.randrange(-150, -50)
                    cars[i].load_image()

                player.load_image()
                player.x = WINDOW_WIDTH / 2
                player.dx = 0
                score = 0
                pg.mouse.set_visible(False)
                sound_engine.play()
                sleep(5)
                pg.mixer.music.play(-1)

        if not crash:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    player.dx = 4
                elif event.key == pygame.K_LEFT:
                    player.dx = -4

            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    player.dx = 0
                elif event.key == pg.K_LEFT:
                    player.cd = 0
 
        screen.fill(GRAY)
        if not crash:
        
            for i in range(lane_count):
            
                pg.draw.rect(screen, WHITE, [lanes[i][0], lanes[i][1], lane_width, lane_height])
                lanes[i][1] += 10
                if lanes[i][1] > WINDOW_HEIGHT:                              
                    lanes[i][1] = -40 - lane_height
                    
            player.draw_image()
            player.move_x()                   
            player.check_out_of_screen()
               
            for i in range(car_count):
                cars[i].draw_image()
                cars[i].y += cars[i].dy

                if cars[i].y > WINDOW_HEIGHT:
                    score += 10
                    cars[i].x = random.randrange(0, WINDOW_WIDTH-cars[i].width)
                    car[i].y = random.randrange(-150, -50)  
                    cars[i].dy = random.randrange(5, 10)                                        
                    cars[i].load_image()
                                                        

                    
            for i in range(car_counnt):
                if player.check_crash(cars[i]):    
                    crash = True
                    pg.mixer.music.stop()
                    sound_crash.play()
                    sleep(2)
                    pg.mouse.set_visible(True)
                    break


                    
            draw_score()
                    
            pg.display.flip()
        else:
            draw_main_menu()

        clock.tick(60)
    pg.quit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
