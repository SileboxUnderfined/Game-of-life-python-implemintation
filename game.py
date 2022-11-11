import pygame
from grid import Grid

class Game:
    def __init__(self, fps, width, height):
        self.fps = fps
        self.width = width
        self.height = height
        self.grid = Grid(width, height)
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.initColors()

        pygame.display.set_caption("game of life")
        self.running = True

    def initColors(self):
        self.black = pygame.color.Color(0,0,0)
        self.white = pygame.color.Color(255,255,255)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                [i.clicked() for i in self.grid.grid if i.collidepoint(pos)]

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.grid.start()

    def draw(self):
        self.screen.fill(self.black)

        self.grid.draw(self.screen)

    def loop(self):
        while self.running:
            self.draw()

            pygame.display.flip()

            self.events()

            self.clock.tick(self.fps)