import pygame
pygame.init() #초기화 (반드시 필요)

screen_width = 480 # (가로크기)
screen_height = 640 # (세로크기)
pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nado Game") #게임이름

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아니다
#pygame 종료
pygame.quit()