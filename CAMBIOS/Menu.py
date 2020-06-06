import pygame,sys
from pygame.locals import *
import numpy as np



class MENU:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico ")
        self.imagen_boton = pygame.image.load("proton.png")
        self.imagen_boton_pressed = pygame.image.load("protonchikito.png")
        self.imagen_panel = pygame.image.load('MENU.jpg')
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        bg_image = pygame.image.load("MENU.jpg")
        self.bg_image = bg_image.convert()
        self.screen.blit(self.bg_image,(0,0))
        
        self.screen.blit(self.imagen_panel,(0,0))
        
    def dibujar_botones_iniciales(lista_botones):
        panel = pygame.transform.scale(self.imagen_panel, [560, 420])
        pantalla.blit(panel, [20, 20])
        for boton in lista_botones:
            if boton['on_click']:
                pantalla.blit(boton['imagen_pressed'], boton['rect'])
            else:
                pantalla.blit(boton['imagen'], boton['rect'])
            dibujar_texto(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)
    def otra_pantalla(self):
        self.clock.tick(10)    
        otra_pantalla = True
        r_boton_1_1 = self.imagen_boton.get_rect()
        botones = []
        r_boton_1_1.topleft = [80, 80]
        botones.append({ 'imagen': self.imagen_boton, 'imagen_pressed': self.imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
        while otra_pantalla:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse = event.pos
                    for boton in botones:
                        boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                    click = True
                if event.type == MOUSEBUTTONUP:
                    for boton in botones:
                        boton['on_click'] = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        otra_pantalla = False
            

            pygame.display.update()