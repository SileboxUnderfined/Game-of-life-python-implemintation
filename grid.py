import pygame
from point import Point #TODO: переименовать Point в Cell

class Grid:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.block_size = 20

        self.initGrid()

    def initGrid(self):
        self.grid = []
        for x in range(0,self.width,self.block_size):
            for y in range(0,self.height,self.block_size):
                point = Point(x,y,self.block_size,self.block_size)
                self.grid.append(point)

    def draw(self,screen):
        for point in self.grid:
            point.draw(screen)

    def start(self): pass #TODO: реализовать старт клеточного автомата