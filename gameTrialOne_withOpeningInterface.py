# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:04:25 2018

@author: chenq
"""
import time
import pygame
from pygame.locals import *

windowSize = (1280,720);
 
class Player:
    x = 500
    y = 300
    Ydirections = {'up': -1, 'down': 1, 'none':0}
    Xdirections = {'left': -1, 'right':1, 'none':0}
    XrunningDirection = 'right'
    YrunningDirection = 'none'
    speed = 20
    rec = pygame.Surface((50,50))
    rec.fill((255,255,255))
    rect = rec.get_rect()
 
    def running(self):
        XnextStep = self.x + self.Xdirections[self.XrunningDirection] * self.speed
        YnextStep = self.y + self.Ydirections[self.YrunningDirection] * self.speed
        if (XnextStep >= 0 and XnextStep <= windowSize[0] - 50 and YnextStep >= 0 and YnextStep <= windowSize[1] -50):
            self.x = XnextStep
            self.y = YnextStep
        else:
            pass
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
    x = 200
    y = 300
    Ydirections = {'up': -1, 'down': 1, 'none':0}
    Xdirections = {'left': -1, 'right':1, 'none':0}
    XrunningDirection = 'right'
    YrunningDirection = 'none'
    speed = 20
    rec = pygame.Surface((50,50))
    rec.fill((255,0,0))
    rect = rec.get_rect()
    t = time.time()
 
    def running(self):
        XnextStep = self.x + self.Xdirections[self.XrunningDirection] * self.speed
        YnextStep = self.y + self.Ydirections[self.YrunningDirection] * self.speed
        if (XnextStep >= 0 and XnextStep <= windowSize[0] - 50 and YnextStep >= 0 and YnextStep <= windowSize[1] -50):
            self.x = XnextStep
            self.y = YnextStep
        else:
            pass
        if (self.speed >= 0.5):
            self.speed -= (time.time()-self.t)/10000;
    
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

class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.player_surf = None
        self.snake_surf = None
        self.player = Player() 
        self.snake = Snake()
 
    def on_init(self):
        pygame.init()
        pygame.font.init()
        self._display_surf = pygame.display.set_mode(windowSize, pygame.HWSURFACE)

        pygame.display.set_caption('Snake game test')
        self._running = True
   #     self._image_surf = pygame.image.load("pygame.png").convert()
        self.player_surf = self.player.rec
        self.snake_surf = self.snake.rec

        self.interfaceSwitch = True
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        # self._display_surf.fill((0,0,0))
        # self._display_surf.blit(self.player_surf,(self.player.x,self.player.y))
        # self._display_surf.blit(self.snake_surf,(self.snake.x,self.snake.y))
        

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

        if self.interfaceSwitch == True:
            self._display_surf.blit(textsurface, (500, 150))
            self._display_surf.blit(textInstruction, (500, 600))
            self._display_surf.blit(textplayer1, (400, 300))
            self._display_surf.blit(instructionImg1, (600, 260))
            self._display_surf.blit(textplayer2, (400, 450))
            self._display_surf.blit(instructionImg2, (600, 410))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.interfaceSwitch = False
                        print(self.interfaceSwitch)
        else:
            self._display_surf.fill((0,0,0))
            self._display_surf.blit(self.player_surf,(self.player.x,self.player.y))
            self._display_surf.blit(self.snake_surf,(self.snake.x,self.snake.y))
        
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
                self.snake.changeDirection(4)
                
            if (keys[K_a]):
              #  self.player.moveLeft()
                self.snake.changeDirection(3)
 
            if (keys[K_w]):
              #  self.player.moveUp()
                self.snake.changeDirection(1)
 
            if (keys[K_s]):
               # self.player.moveDown()
                self.snake.changeDirection(2)
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
