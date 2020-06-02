import pygame,sys
from pygame.locals import *
import numpy as np
class carga(pygame.sprite.Sprite):
    def __init__(self,pos,magnitud):
        if magnitud<0:
            self.image=pygame.image.load("electron.png")
        if magnitud>0:
            self.image=pygame.image.load("proton.png") 
        if magnitud==0:
            self.image=pygame.image.load("Neutro.png")
        px,py=pos
        self.pos=self.image.get_rect().move(px,py)
        self.magnitud=magnitud
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=self.pos
    def campo(self, punto):
        k=8.9
        campo=[0,0]
        
        dist=((punto[0]-self.pos[0])**(2)+(punto[1]-self.pos[1])**(2))**(3/2)
        if dist!=0:
            campo[0]=(self.magnitud*k*(punto[0]-self.pos[0]))/dist
            campo[1]=(self.magnitud*k*(punto[1]-self.pos[1]))/dist
            return (campo[0],campo[1])
        else:
            return(0,0)
class ball(pygame.sprite.Sprite):
    
    def __init__(self,pos, vel,magnitud,acel=(4,5)):
        if magnitud<0:
            self.image=pygame.image.load("electronchikito.png")
        if magnitud>0:
            self.image=pygame.image.load("protonchikito.png") 
        if magnitud==0:
            self.image=pygame.image.load("Neutrochikito.png")
        px,py=pos
        self.pos=self.image.get_rect().move(px,py)
        self.vel=np.array(vel)
        self.acel=np.array(acel)
        self.magnitud=magnitud
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=self.pos
    def fuerza(self,CARGA):
        fuerza=[0,0]
        if carga.campo(CARGA,self.pos)==False:
            return (0,0)
        fuerza[0]=self.magnitud*carga.campo(CARGA,self.pos)[0]
        fuerza[1]=self.magnitud*carga.campo(CARGA,self.pos)[1]
        return (fuerza[0],fuerza[1])

    def move(self,CARGA):
        if CARGA.pos[0]==self.pos[0] and CARGA.pos[1]==self.pos[1]:
            self.vel=self.vel-self.vel
        vx,vy=self.vel
        ax,ay=self.acel
        self.vel=self.vel+self.acel
        self.pos = self.pos.move(vx,vy)
        


        self.rect=self.pos
    
class intro:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        bg_image = pygame.image.load("fondo-pared-ladrillos.jpg")
        self.bg_image = bg_image.convert()
        self.screen.blit(self.bg_image,(0,0))
    def update(self):
        self.clock.tick(10)
        pygame.display.flip()
class world:
    def __init__(self,balls,cargas):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico")
        self.clock=pygame.time.Clock()
        self.balls=balls
        self.cargas=cargas
        self.screen = pygame.display.set_mode((800, 600))
        bg_image = pygame.image.load("fondo-pared-ladrillos.jpg")
        self.bg_image = bg_image.convert()
        self.screen.blit(self.bg_image,(0,0))
        
    def update(self):
        self.clock.tick(10)
        
        for o in self.balls:
            self.screen.blit(self.bg_image,o.pos, o.pos)
        for l in self.cargas:
            self.screen.blit(self.bg_image,l.pos, l.pos)
        

        for k in self.cargas:
            self.screen.blit(k.image,k.pos)
            for o in self.balls:
                
                o.acel=o.fuerza(k)
                o.move(k)
                self.screen.blit(o.image,o.pos)
        
        pygame.display.flip()

            
    

def main():
    c=ball((500,100),(1,0),20)
    g=ball((0,200),(10,2),-20)
    v=ball((0,300),(2,0),5)
    k=ball((300,400),(0,0),10)
    e=carga((350,250),-20)
    f=carga((600,250),-20)
    l=carga((550,400),20)
    p=[]
    for i in range(-200,1000,35):
        p=p+[carga((i,500),15)]
        p=p+[carga((i,0),-15)]
    w=world([v],p)
    w=world([g,k,c],[e])
    
    while True:
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        
        w.update()
            
            
            
        

         
if __name__ =="__main__":
    main()
