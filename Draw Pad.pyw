import pygame
from pygame.locals import *
import sys
import os
import inputbox

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)


class Draw(object):
    
    def import_picture(self, screen):
        image_name = (inputbox.ask(screen, 'Image Name'))
        imp_img = pygame.image.load(image_name)
        screen.blit(imp_img, (0, 0))
        
    
    def update(self, screen):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            self.color = RED
        if key[pygame.K_b]:
            self.color = BLUE
        if key[pygame.K_g]:
            self.color = GREEN
        if key[pygame.K_w]:
            self.color = WHITE
        if key[pygame.K_e]:
            self.color = BLACK
        if key[pygame.K_1]:
            self.size = 5
        if key[pygame.K_2]:
            self.size = 10
        if key[pygame.K_3]:
            self.size = 20
        if key[pygame.K_4]:
            self.size = 30
        if key[pygame.K_5]:
            self.size = 40
        if key[pygame.K_c]:
            r = int(inputbox.ask(screen, 'Red Value'))
            g = int(inputbox.ask(screen, 'Green Value'))
            b = int(inputbox.ask(screen, 'Blue Value'))
            self.color = (r,g,b)
        if key[pygame.K_s]:
            pygame.image.save(screen,"screenshot.jpg")
        if key[pygame.K_i]:
            self.import_picture(screen)
        mouse_pos = pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, self.color, (mouse_pos), self.size)


    def main(self):

        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(45)
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Draw Pad')
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        self.color = (255,255,255)
        self.size = 10
        
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            self.update(screen)
            pygame.display.flip()
            
        
if __name__ == '__main__':
    draw = Draw()
    draw.main()
