import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

# 4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        ############################
        # 여기에 도형을 그리세요
        ############################
        sky = pygame.image.load('Background.png')
        #sky_rect = sky.get_rect()
        #print(sky_rect)
        sky = pygame.transform.scale(sky, (400, 300))
        screen.blit(sky, (0, 0))

        ground = pygame.image.load('Ground.png')
        ground = pygame.transform.scale(ground, (400, 150))
        screen.blit(ground, (0, 300))

        castle = pygame.image.load('castle.png')
        castle = pygame.transform.scale(castle, (200, 150))
        screen.blit(castle, (200, 150))

        heart = pygame.image.load('heart.png')
        heart = pygame.transform.scale(heart, (50, 50))
        screen.blit(heart, (0, 0))

        player = pygame.image.load('Player_Attack_R.png')
        player = pygame.transform.scale(player, (50, 50))
        screen.blit(player, (100, 250))
        
        pygame.display.update()

runGame()
pygame.quit()
