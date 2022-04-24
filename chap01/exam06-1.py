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
        num_of_lines=3
        gap = 20
        # 가로선
        for y_idx in range(num_of_lines+1):
            y_pos = y_idx * gap
            pygame.draw.line(screen, (255, 0, 0), (0, y_pos), (gap*num_of_lines, y_pos), 3)

        # 세로선
        for x_idx in range(num_of_lines+1):
            x_pos =(x_idx) * gap
            pygame.draw.line(screen, (255, 0, 0), (x_pos, 0), (x_pos, gap*num_of_lines), 3)
        
        pygame.display.update()

runGame()
pygame.quit()
