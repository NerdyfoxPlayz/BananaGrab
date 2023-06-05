import pygame
import os
import random
pygame.init()
pygame.mixer.init()

#importing files stuff
monke_image_import = pygame.image.load('monke.png')
monke_img = pygame.transform.scale(monke_image_import, (300, 300))

banana_image_import = pygame.image.load('banana.png')
banana_img = pygame.transform.scale(banana_image_import, (250, 250))
munch = pygame.mixer.Sound('munch.wav')

                           

#Pygame stuff
WIDTH, HEIGHT = 1080, 2400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()

#don't ask, its for bananas, trust me
banana1_x, banana1_y = random.randrange(250, WIDTH), 0 - random.randrange(100, 300)
banana2_x, banana2_y = random.randrange(250, WIDTH), 0 - random.randrange(500, 800)
banana3_x, banana3_y = random.randrange(250, WIDTH), 0 - random.randrange(900, 1400)
banana4_x, banana4_y = random.randrange(250, WIDTH), 0 - random.randrange(1300, 2000)
banana5_x, banana5_y = random.randrange(250, WIDTH), 0 - random.randrange(1700, 2600)

def draw_window(monke):
    screen.fill('white')
    screen.blit(monke_img, (monke.x, monke.y))
    screen.blit(banana_img, (banana1.x, banana1.y))
    screen.blit(banana_img, (banana2.x, banana2.y))
    screen.blit(banana_img, (banana3.x, banana3.y))
    screen.blit(banana_img, (banana4.x, banana4.y))
    screen.blit(banana_img, (banana5.x, banana5.y))
    
    
    pygame.display.update()
    

run = True
while run:
    clock.tick(FPS)
    
    mouse_pos = pygame.mouse.get_pos()
    monke = pygame.Rect(mouse_pos[0], HEIGHT - 550, 300, 300)    
    
    if banana1_y > HEIGHT:
        banana1_x, banana1_y = random.randrange(0, WIDTH - 250), -250
        
    if banana2_y > HEIGHT:
        banana2_x, banana2_y = random.randrange(0, WIDTH - 250), -250
        
    if banana3_y > HEIGHT:
        banana3_x, banana3_y = random.randrange(0, WIDTH - 250), -250
        
    if banana4_y > HEIGHT:
        banana4_x, banana4_y = random.randrange(0, WIDTH - 250), -250
        
    if banana5_y > HEIGHT:
        banana5_x, banana5_y = random.randrange(0, WIDTH - 250), -250
       
    banana1 = pygame.Rect(banana1_x, banana1_y, 250, 250)
    banana1_y += 10
    if banana1.colliderect(monke):
       banana1_y = HEIGHT + 100
       munch.play()
       
    banana2 = pygame.Rect(banana2_x, banana2_y, 250, 250)
    banana2_y += 10
    if banana2.colliderect(monke):
        banana2_y = HEIGHT
        munch.play()
    
    banana3 = pygame.Rect(banana3_x, banana3_y, 250, 250)
    banana3_y += 10
    if banana3.colliderect(monke):
        banana3_y = HEIGHT
        munch.play()
        
    banana4 = pygame.Rect(banana4_x, banana4_y, 250, 250)
    banana4_y += 10
    if banana4.colliderect(monke):
        banana4_y = HEIGHT
        munch.play()
        
    banana5 = pygame.Rect(banana5_x, banana5_y, 250, 250)
    banana5_y += 10
    if banana5.colliderect(monke):
        banana5_y = HEIGHT
        munch.play()
    
    draw_window(monke)
