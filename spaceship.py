import pygame

class Ship(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image=pygame.image.load('ship.png')
    self.image=pygame.transform.smoothscale(self.image, (500,500))
    self.rect=self.image.get_rect()
    self.image=pygame.transform.rotate(self.image,(270))
    screen_info=pygame.display.Info()
    (width,height)=(screen_info.current_w, screen_info.current_h)
    
    self.rect.center=(30, height/2)
    self.speed=pygame.math.Vector2(10,0)
  def update(self):
    self.rect.move_ip(self.speed)