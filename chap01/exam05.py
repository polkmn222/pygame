# pip install pygame
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
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (200, 0))
        pygame.draw.line(screen, (255, 0, 0), (0, 20), (200, 20), 3)
        pygame.draw.line(screen, (255, 0, 0), (0, 40), (200, 40), 6)
        
        pygame.display.update()

runGame()
pygame.quit()
