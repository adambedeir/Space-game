import pygame
from spaceship import *
pygame.init()
screen_info=pygame.display.Info()
print(screen_info)
size=(width,height)=(screen_info.current_w,screen_info.current_h)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
color= (10,0,10)

numlevel=4
level=1
player=Ship()
def main():
  
  while level<=numlevel:
    clock.tick(60)
    player.update()
    for event in pygame.event.get():
      if event==pygame.KEYDOWN
        if event.key==pygame.K_D
        player.speed[0]=10
    screen.fill(color)
    screen.blit (player.image,player.rect)
    pygame.display.flip()
if __name__=='__main__':
  main()

