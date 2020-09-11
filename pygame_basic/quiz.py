import pygame
import random

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정   
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#character 이미지 생성.
#character파일로 저장. (width, height) = (70, 70)

# 화면 타이틀 설정
pygame.display.set_caption("Avoiding Ddong Game") # 게임 이름

#FPS 지정
clock = pygame.time.Clock()

background = pygame.image.load("C:/py/python/pygame_basic/background.png")

# 케릭터(스프라이트) 불러오기
character = pygame.image.load("C:/py/python/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 케릭터의 가로
character_height = character_size[1] # 케릭터의 세로
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 1
Enermy_speed = 25

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/py/python/pygame_basic/enermy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 적의 가로
enemy_height = enemy_size[1] # 적의 세로
enemy_x_pos = random.sample(range(enemy_width, screen_width - enemy_width), 1)[0]
#(screen_width) / 2 - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = 0 # 화면 세로 가운데 위치 (세로)

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성. (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보.
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴.

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초방 프레임 수 설정. 30프레임.
    ddongDt = clock.tick(60)
    #print("fps : "  str(clock.get_fps()))
    #캐릭터가 100만큼 이동을 해야함.
    #10 fps : 1초 동안에 10번 동작. -> 1번에 몇 만큼 이동? 10만큼! 10*10 = 100
    #20 fps : 1초 동안에 20번 동작. -> 1번에 몇 만큼 이동? 5만큼! 5*20 = 100

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed #character_speed 만큼 왼쪽
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed #character_speed 만큼 오른쪽
            elif event.key == pygame.K_UP:
                to_y -= character_speed #character_speed 만큼 위로
            elif event.key == pygame.K_DOWN:
                to_y += character_speed #character_speed 만큼 아래로
        if event.type == pygame.KEYUP: # 방향키를 때면 멈춤.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
    enemy_y_pos += Enermy_speed
    enemy_y_pos += to_y * ddongDt
    character_x_pos += to_x * dt #프레임에 따라 캐릭터가 이동하는 속도를 고정하도록 지정하기 위함.
    character_y_pos += to_y * dt #프레임에 따라 캐릭터가 이동하는 속도를 고정하도록 지정하기 위함.

    #캐릭터가 화면 밖으면 벗어나지 않도록 하기 위해 위치를 지정한다.
    #가로 경계값 처리

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.sample(range(enemy_width, screen_width - enemy_width), 1)[0]

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        #실제 스크린 크기에서 캐릭터 크기만큼 빼서 마치 오른쪽 끝으로 못나가는 것 처럼 표현하기.
        character_x_pos = screen_width - character_width
    
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        #실제 스크린 크기에서 캐릭터 크기만큼 빼서 마치 오른쪽 끝으로 못나가는 것 처럼 표현하기.
        character_y_pos = screen_height - character_height

    #충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 케릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 케릭터 그리기

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드 초로 환산.
    #결과 시간을 1000으로 나누어서 초 단위로 표시

    # 출력할 글자, True, 글자 색상
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) #실제 글자를 그리는 것.
    #int로 변경해서 초단위 표시하도록 하기 위해 int로 변경하고 다시 string으로 변환하여 출력.
    screen.blit(timer, (10, 10))

    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <=0:
        print("타임아웃!")
        running = False

    pygame.display.update() # 게임 화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000) #2초 정도 대기

# pygame 종료
pygame.quit()