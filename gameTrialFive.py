
import time
import pygame
from pygame.locals import *
import os

windowSize = (1364,748);

class Player:
    x = 484
    y = 220
    
    Ydirections = {'up': -1, 'down': 1, 'none':0}
    Xdirections = {'left': -1, 'right':1, 'none':0}
    XrunningDirection = 'right'
    YrunningDirection = 'none'
    speed = 88

    updateCountMax = 2
    updateCount = 0

 
    def running(self):
        
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
            
            XnextStep = self.x + self.Xdirections[self.XrunningDirection] * self.speed
            YnextStep = self.y + self.Ydirections[self.YrunningDirection] * self.speed
            if (XnextStep >= 0 and XnextStep <= windowSize[0] - 88 and YnextStep >= 0 and YnextStep <= windowSize[1] - 44):
                self.x = XnextStep
                self.y = YnextStep
            else:
                pass
            self.updateCount = 0

            
        '''
        if (self.x >= 0 and self. x <= windowSize[0] - 50 and self.y >= 0 and self.y <= windowSize[1] - 50):
            if(self.runningDirection == 'right' or self.runningDirection == 'left'):
                self.x = self.x + self.directions[self.runningDirection] * self.speed
            else:
                self.y = self.y + self.directions[self.runningDirection] * self.speed
        else:
            if (self.x < 0 or self.x > windowSize[0] - 50):
                self.x = self.x - self.directions[self.runningDirection] * self.speed
            if (self.y < 0 or self.y > windowSize[1] - 50):
                self.y - self.directions[self.runningDirection] * self.speed
            '''

        
           
    def changeDirection(self,code):
        if (code == 1):
            self.YrunningDirection = 'up'
            self.XrunningDirection = 'none'
        elif (code == 2):
            self.YrunningDirection = 'down'
            self.XrunningDirection = 'none'
        elif (code == 3):
            self.XrunningDirection = 'left'
            self.YrunningDirection = 'none'
        elif (code == 4):
            self.XrunningDirection = 'right'
            self.YrunningDirection = 'none'
    
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed
            
class Snake:

    x = [44*6]
    y = [44*7]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0


    def __init__(self,length):
        self.length = length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)

        self.x[1] = 1 * self.step
        self.x[2] = 2 * self.step

        self.t = time.time()

 
    def running(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:                
                self.x[0] = self.x[0] + self.step
    
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step

            if self.direction == 2:
                self.y[0] = self.y[0] - self.step

            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 

            
    
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3

    def draw(self,surface,image):
        for i in range(1,self.length):
            surface.blit(image,(self.x[i],self.y[i]))
    def drawhead(self,surface,image):
        surface.blit(image,(self.x[0],self.y[0]))

class Game:
    def isCollision(self,x1,y1,x2,y2,b):
        #print(x1,y1)
        if x2 >= x1 and x2 <= x1 + b:
            if y2 >= y1 and y2 <= y1 + b:
##                print("we hit it!")
                return True
        return False
            
    def isEaten(self,x1,y1,x2,y2):
        if (x2 < x1 + 44 and x2 > x1 - 44) or (x2 > x1 and x2 < x1 + 44):
            if y2 > y1-44 and y2 < y1 + 44:
                return True
        if (y2 < y1 + 44 and y2 > y1 - 44) or (y2 < y1 and y2 + 44 > y1):
            if x2 + 44 > x1 and x2 < x1 + 44:
                return True
        return False
    
    def isHitWall(self,x,y):
        if x == 1320 or y == 704 or x == 0 or y == 0:
            return True
        return False



class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
#lxn
        self.player_surf = None
        self.snake_surf = None
        self.player = Player() 
        self.snake = Snake(3)

        self.game = Game()
        self.interfaceSwitch = True
        


 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(windowSize, pygame.HWSURFACE)
 
        pygame.display.set_caption('Snake game test')
        self._running = True
   #     self._image_surf = pygame.image.load("pygame.png").convert()

#lxn
        self.player_surf = pygame.image.load("douzi.jpg").convert()
        self.snake_surf = pygame.image.load("snake.png").convert()
        self.snakehead_surf = pygame.image.load("head.png").convert()
        
        self.interfaceSwitch = True


 
    def on_event(self, event):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._running = False
 
    def on_loop(self):
        self.snake.running()
        #print(self.player.x, self.player.y)
##        for i in range(0,self.snake.length):
        if self.game.isEaten(self.player.x,self.player.y,self.snake.x[0], self.snake.y[0]):
            print("The egg loses!")
            theScreen.end2()

        if (time.time() - self.snake.t) / 10 <= 1.1 and (time.time() - self.snake.t) /10 >= 0.9:
            self.snake.length = self.snake.length + 5
            self.snake.t += 10
            

        for i in range(2,self.snake.length):
            if self.game.isCollision(self.snake.x[0],self.snake.y[0],self.snake.x[i], self.snake.y[i],40):
                print("The snake loses!")
                theScreen.end3()
                
        if self.game.isHitWall(self.snake.x[0],self.snake.y[0]):
            print("The snake loses!")
            theScreen.end1()
        
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
#lxn
        
        self._display_surf.blit(self.player_surf,(self.player.x,self.player.y))
#        self._display_surf.blit(self.snake_surf,(self.snake.x,self.snake.y))
        self._display_surf.blit(self.player_surf,(self.player.x,self.player.y))
        self.snake.drawhead(self._display_surf, self.snakehead_surf)
        self.snake.draw(self._display_surf, self.snake_surf)
        for i in range(0,1364,44):
            pygame.draw.rect(self._display_surf,(60,60,100),(i,0,43,43))
            pygame.draw.rect(self._display_surf,(60,60,100),(i,704,43,43))
        for i in range(44,704,44):
            pygame.draw.rect(self._display_surf,(60,60,100),(0,i,43,43))
            pygame.draw.rect(self._display_surf,(60,60,100),(1320,i,43,43))

        
        
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
            self.player.running()
            self.snake.running()
 
            if (keys[K_RIGHT]):
                #self.player.moveRight()
                self.player.changeDirection(4)
 
            if (keys[K_LEFT]):
              #  self.player.moveLeft()
                self.player.changeDirection(3)
 
            if (keys[K_UP]):
              #  self.player.moveUp()
                self.player.changeDirection(1)
 
            if (keys[K_DOWN]):
               # self.player.moveDown()
                self.player.changeDirection(2)
            
            if (keys[K_d]):
#                self.snake.changeDirection(4)
                self.snake.moveRight()
                
            if (keys[K_a]):
                self.snake.moveLeft()
#               self.snake.changeDirection(3)
            if (keys[K_w]):
                self.snake.moveUp()
#                self.snake.changeDirection(1)
 
            if (keys[K_s]):
                self.snake.moveDown()
#                self.snake.changeDirection(2)
 
            if (keys[K_ESCAPE]):
                self._running = False

 
            self.on_loop()
            self.on_render()
            time.sleep (50.0 / 1000.0);
##        self.on_cleanup()

class Screen():
    def __init__(self):
        
        self._display_surf = None
        self.interfaceSwitch = True
        self.timer = None
        
    def begin(self):

        pygame.init()

        self._display_surf = pygame.display.set_mode(windowSize, pygame.HWSURFACE)
 
        pygame.display.set_caption('Snake game test')
        
        myfont1 = pygame.font.SysFont('Comic Sans MS', 60)

        textsurface = myfont1.render('Snake Game', True, (255, 255, 255))


        myfont2 = pygame.font.SysFont('Comic Sans MS', 30)

        textInstruction = myfont2.render('Press the space to start!', True, (255, 255, 255))

        textplayer1 = myfont2.render('Snake:', True, (255, 255, 255))

        instructionImg1 = pygame.image.load('instruction1.jpg')
        instructionImg1 = pygame.transform.scale(instructionImg1, (180, 120))

        textplayer2 = myfont2.render('Egg:', True, (255, 255, 255))

        instructionImg2 = pygame.image.load('instruction2.jpg')
        instructionImg2 = pygame.transform.scale(instructionImg2, (180, 120))

        while True:
            if self.interfaceSwitch == True:
                self._display_surf.blit(textsurface, (500, 150))
                self._display_surf.blit(textInstruction, (500, 600))
                self._display_surf.blit(textplayer1, (400, 300))
                self._display_surf.blit(instructionImg1, (600, 260))
                self._display_surf.blit(textplayer2, (400, 450))
                self._display_surf.blit(instructionImg2, (600, 410))
                #print("true")

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.interfaceSwitch = False
                            #print(self.interfaceSwitch)
                            theApp.on_execute()
                            break
            pygame.display.flip()
            
    def end1(self):
        while True:
            self.myfont3 = pygame.font.SysFont('Comic Sans MS',60)
            textsurface = self.myfont3.render('Snake Hits the Wall!',True,(255,255,255))
            self._display_surf.blit(textsurface, (500, 150))
            textsurface2 = self.myfont3.render('Press the space to leave!',True,(255,255,255))
            self._display_surf.blit(textsurface2, (500, 350))
            pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
##                            isFirstTime = False
##                            theApp.on_execute()
                            pygame.quit()
                            break
        

    def end2(self):
        while True:
            self.myfont3 = pygame.font.SysFont('Comic Sans MS',60)
            textsurface = self.myfont3.render('The egg has been Eaten!',True,(255,255,255))
            self._display_surf.blit(textsurface, (500, 150))
            textsurface2 = self.myfont3.render('Press the space to leave!',True,(255,255,255))
            self._display_surf.blit(textsurface2, (500, 350))
            pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
##                            isFirstTime = False
##                            theApp.on_execute()
                            pygame.quit()
                            break

    def end3(self):
        while True:
            self.myfont3 = pygame.font.SysFont('Comic Sans MS',60)
            textsurface = self.myfont3.render('Snake eats himeself!',True,(255,255,255))
            self._display_surf.blit(textsurface, (500, 150))
            textsurface2 = self.myfont3.render('Press the space to leave!',True,(255,255,255))
            self._display_surf.blit(textsurface2, (500,350))
            pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
##                            isFirstTime = False
##                            theApp.on_execute()
                            pygame.quit()
                            break
    

        
        
 
if __name__ == "__main__" :
    theApp = App()
    theScreen = Screen()
    theScreen.begin()

