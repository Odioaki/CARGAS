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
        if self.col(CARGA)==True:
            return (0,0)
        return (fuerza[0],fuerza[1])
        
            

    def move(self,CARGA):
        if CARGA.pos[0]==self.pos[0] and CARGA.pos[1]==self.pos[1]:
            self.vel=self.vel-self.vel
        vx,vy=self.vel
        ax,ay=self.acel
        self.vel=self.vel+self.acel
        self.pos = self.pos.move(vx,vy)
        


        self.rect=self.pos
    def col(self, o):
            if pygame.sprite.collide_mask(self,o) is None:
                return
            
            npspos=np.array((self.pos.x,self.pos.y))
            npopos=np.array((o.pos.x,o.pos.y))
            
            colision = (npspos-npopos)
            dist=np.sqrt(np.dot(colision, colision))
            colision=colision/dist

            self.vel = self.vel - self.vel
            return True
            
            
            



class world:
    def __init__(self,ball,cargas):
        
        pygame.init()
        pygame.display.set_caption("Simulador Campo Electrico")
        self.clock=pygame.time.Clock()
        self.ball=ball
        self.cargas=cargas
        self.screen = pygame.display.set_mode((800, 600))
        bg_image = pygame.image.load("fondo-pared-ladrillos.jpg")
        self.bg_image = bg_image.convert()
        self.screen.blit(self.bg_image,(0,0))
        
    def update(self):
        self.clock.tick(10)    
        
        
        for o in self.ball :
            self.screen.blit(self.bg_image,o.pos,o.pos)
        for i in range(len(self.ball)):
            for j in range(len(self.cargas)):
                self.ball[i].col(self.cargas[j])
        for k in self.cargas:
            self.screen.blit(k.image,k.pos)
            for o in self.ball:
                
                o.acel=o.fuerza(k)
                o.move(k)
                self.screen.blit(o.image,o.pos)
        
        pygame.display.flip()
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

class INTRO:
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
                    if event.key == pygame.K_p:
                        otra_pantalla = False
            

            pygame.display.update()          

   

def main():
    c=ball((500,100),(1,0),20)
    g=ball((0,200),(10,2),-20)
    v=ball((0,250),(1.5,0),-5)
    k=ball((300,400),(0,0),10)
    e=carga((350,250),-20)
    f=carga((600,250),-20)
    l=carga((550,500),50)
    n=carga((550,100),20)
    p=[]
    b=[]
    for i in range(-200,1000,20):
        p=p+[carga((i,500),10)]
        p=p+[carga((i,0),-10)]
        b=b+[ball((i,400),(0,0),15)]
        b=b+[ball((i,200),(0,0),-15)]
    #w=world([v],p)
    #w=world([g,k,c,v],[e])
    #w=world(b,[e])
    w=world(b,[e,f,l,n])




    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    MENU().otra_pantalla()

                    

            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        

        w.update()

            
            
            
        

         
if __name__ =="__main__":
    main()
