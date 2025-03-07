import pygame
import random
frameR = 30
NUM_PECES=5
gameUp=True
ancho=600
alto=400
pygame.init()
screen=pygame.display.set_mode((ancho,alto))
fondo= pygame.image.load("media/fondo.jpg").convert()
fondo_rect= fondo.get_rect()
pygame.display.set_caption("Pecera")
pezder=pygame.image.load('media/sources/pez1.png')
pezizq=pygame.image.load('media/sources/pez1r.png')

marron=(222, 184, 135)

comidax,comiday,cy = -100, -100, 0
vel=1
velx=vely=vel
peces =[]

for i in range(NUM_PECES):
  x=random.randint(60,540)
  y=random.randint(40,360)
  dx=random.randint(60,540)
  dy=random.randint(40,360)
  
  pez=pygame.image.load('media/sources/pez1.png')
  if dx<x:
    pez=pezizq
  else:
    pez=pezder
  pez_rect = pez.get_rect()
  pez_rect.topleft=(x,y)
  peces.append([pez,x,y,dx,dy])

comida=False
buscarComida=False

reloj=pygame.time.Clock()
while gameUp:
  reloj.tick(frameR) # Establece la velocidad del juego al valor de frameR
  screen.blit(fondo, fondo_rect)
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      gameUp=False

  # ------------- Movimiento pez ------------- #
  for pez in peces:
    p,x,y,dx,dy = pez
    rect=p.get_rect()
    if buscarComida:
      if comidax-40<x:
        pez[0]=pezizq
      else:
        pez[0]=pezder
      dx=comidax-40
      dy=comiday-40
    ddx=dx-x
    ddy=dy-y
    if ddx==0 and ddy==0:
      if buscarComida:
        buscarComida=False
        comiday=-10
        cy=-10
      dx=random.randint(60,540)
      dy=random.randint(40,360)
      if dx<x:
        pez[0]=pezizq
      else:
        pez[0]=pezder
      pez[3]=dx
      pez[4]=dy
      rect.x=x
      rect.y=y
      screen.blit(p,rect)
      continue
    if ddx>0:
      pez[0]=pezder
      velx=vel
    elif ddx<0:
      pez[0]=pezizq
      velx=-vel
    else:
      velx=0
    if ddy>0:
      vely=vel
    elif ddy<0:
      vely=-vel
    else:
      vely=0
    x+=velx
    y+=vely
    rect.x=x
    rect.y=y
    pez[1]=x
    pez[2]=y
    screen.blit(p,rect)

  keys=pygame.key.get_pressed()

# ------------- Comida ------------- #

  if keys[pygame.K_SPACE]:
    comiday=-10
    comidax=random.randint(60,540)
    cy=random.randint(60,120)
    print("Comida")
    print(comidax, cy)
    buscarComida=True

  if comiday!=cy:
    if comiday<cy:
      comiday+=1
    else:
      comiday-=1
  pygame.draw.rect(surface=screen,color=marron,rect=(comidax,comiday,6,6))
  pygame.display.flip()

pygame.quit()