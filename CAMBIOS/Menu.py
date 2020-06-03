import pygame,sys
from pygame.locals import *
import numpy as np

class MENU:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico ")
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        bg_image = pygame.image.load("fondo-pared-ladrillos.jpg")
        self.bg_image = bg_image.convert()
        self.screen.blit(self.bg_image,(0,0))
    def otra_pantalla(self):
        self.clock.tick(10)    
        otra_pantalla = True
        while otra_pantalla:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        otra_pantalla = False
            

            pygame.display.update()

