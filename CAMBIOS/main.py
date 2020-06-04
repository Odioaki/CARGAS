import pygame,sys
from pygame.locals import *
import numpy as np
from Funciones import *
from Pantalla import *
from Menu import *
from Intro import *



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
    #PRUEBA VELOCIDAD ORBITAL
    PO=ball((0,500),(1.5,0),-5)
    CO=carga((400,300),40)
    #w=world([PO],[CO])
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    MENU().otra_pantalla()
                    #w.update()
        
              
                    

            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        w.update()
        #MENU().otra_pantalla()

        
   
main()

