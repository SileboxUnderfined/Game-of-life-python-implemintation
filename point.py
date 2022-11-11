import pygame
from pygame import Rect

class Point(Rect):
    def __init__(self,x,y,width,height):
        super(Point, self).__init__(x,y,width,height)
        self.generation = 0
        self.alive = False
        self.white = pygame.color.Color(255,255,255)

    def draw(self,screen):
        if self.alive: pygame.draw.rect(screen,self.white,self)
        else: pygame.draw.rect(screen,self.white,self,1)

    def clicked(self):
        self.alive = not self.alive