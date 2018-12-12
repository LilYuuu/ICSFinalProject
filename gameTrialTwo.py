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
    speed = 5

    
##    rec = pygame.Surface((50,50))
##    rec.fill((255,255,255))
##    rect = rec.get_rect()
 
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

    x = [0]
    y = [0]
    step = 50
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
    
##    x = 200
##    y = 300
##    Ydirections = {'up': -1, 'down': 1, 'none':0}
##    Xdirections = {'left': -1, 'right':1, 'none':0}
##    XrunningDirection = 'right'
##    YrunningDirection = 'none'
##    speed = 5
##
##    length = 3
    
##    rec = pygame.Surface((50,length))    
##    rec.fill((255,0,0))
##    rect = rec.get_rect()
    
    t = time.time()

    def __init__(self,length):
        self.length = length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)

        self.x[1] = 1 * self.step
        self.x[2] = 2 * self.step

 
    def running(self):
##        XnextStep = self.x + self.Xdirections[self.XrunningDirection] * self.speed
##        YnextStep = self.y + self.Ydirections[self.YrunningDirection] * self.speed
##        if (XnextStep >= 0 and XnextStep <= windowSize[0] - 50 and YnextStep >= 0 and YnextStep <= windowSize[1] -50):
##            self.x = XnextStep
##            self.y = YnextStep
##        else:
##            pass


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

            
##        if (self.speed >= 0.5):
##            self.speed -= (time.time()-self.t)/10000

##        if self.length >= 50:           
##            self.length += (time.time()-self.t)/100
##            rec = pygame.Surface((50,self.length))
##            rec.fill((255,0,0))
##            rect = rec.get_rect()

        
    
##    def changeDirection(self,code):
##        if (code == 1):
##            self.YrunningDirection = 'up'
##            self.XrunningDirection = 'none'
##        elif (code == 2):
##            self.YrunningDirection = 'down'
##            self.XrunningDirection = 'none'
##        elif (code == 3):
##            self.XrunningDirection = 'left'
##            self.YrunningDirection = 'none'
##        elif (code == 4):
##            self.XrunningDirection = 'right'
##            self.YrunningDirection = 'none'
    
    def moveRight(self):
#        self.x = self.x + self.speed
        self.direction = 0
 
    def moveLeft(self):
##        self.x = self.x - self.speed
        self.direction = 1
 
    def moveUp(self):
##        self.y = self.y - self.speed
        self.direction = 2
 
    def moveDown(self):
##        self.y = self.y + self.speed
        self.direction = 3
#lxn
    def draw(self,surface,image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))

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
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(windowSize, pygame.HWSURFACE)
 
        pygame.display.set_caption('Snake game test')
        self._running = True
   #     self._image_surf = pygame.image.load("pygame.png").convert()

#lxn
        self.player_surf = pygame.image.load("douzi.jpg").convert()
        self.snake_surf = pygame.image.load("she.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
#lxn
        
        self._display_surf.blit(self.player_surf,(self.player.x,self.player.y))
#        self._display_surf.blit(self.snake_surf,(self.snake.x,self.snake.y))
        self.snake.draw(self._display_surf, self.snake_surf)
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
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
