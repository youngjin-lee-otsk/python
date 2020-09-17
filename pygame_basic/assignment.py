import pygame
import random
from datetime import datetime
from datetime import timedelta
from tkinter import *
from tkinter import messagebox

#팝업창
# pop_up = Tk()
# pop_up.title('TEST')
# pop_up.geometry("200x100")
# pop_up.resizable(0, 0)

#게임 타임 인터벌
TURN_INTERVAL = timedelta(seconds=0.3)

pygame.init() # 초기화 (반드시 필요)
pygame.mixer.init()

# 화면 크기 설정   
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 함수가 시작된 시간
last_moved_time = datetime.now()

#character 이미지 생성.
#character파일로 저장. (width, height) = (70, 70)

# 화면 타이틀 설정
pygame.display.set_caption("Avoding Timo") # 게임 이름

# 배경 음악
pygame.mixer.music.load("C:/py/python/pygame_basic/timo_song.mp3")
pygame.mixer.music.set_volume(0.4) # 1 ~ 0.1
pygame.mixer.music.play(-1)
 
# 레벨업 음성
voice = pygame.mixer.Sound("C:/py/python/pygame_basic/hasegi.wav")

#FPS 지정
clock = pygame.time.Clock()

#점수
total_score = 0 #전체점수
score = 100 #증가변수

background = pygame.image.load("C:/py/python/pygame_basic/kal_background.jpg")

# 야스오 불러오기
character = pygame.image.load("C:/py/python/pygame_basic/yasuo.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 케릭터의 가로
character_height = character_size[1] # 케릭터의 세로
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height / 2 - (character_height / 2) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.3
Enermy_speed = 3

# 티모1
enemy = pygame.image.load("C:/py/python/pygame_basic/timo.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 적의 가로
enemy_height = enemy_size[1] # 적의 세로
enemy_x_pos = random.sample(range(enemy_width, screen_width - enemy_width), 1)[0]
enemy_y_pos = 0 # 화면 세로 가운데 위치 (세로)

# 티모2
enemy2 = pygame.image.load("C:/py/python/pygame_basic/timo.png")
enemy_size2 = enemy2.get_rect().size # 이미지의 크기를 구해옴
enemy_width2 = enemy_size2[0] # 적의 가로
enemy_height2 = enemy_size2[1] # 적의 세로
enemy_x_pos2 = random.sample(range(enemy_width2, screen_width - enemy_width2), 1)[0]
enemy_y_pos2 = 640 - enemy_height2 # 화면 세로 가운데 위치 (세로)

# 티모3
enemy3 = pygame.image.load("C:/py/python/pygame_basic/timo.png")
enemy_size3 = enemy3.get_rect().size # 이미지의 크기를 구해옴
enemy_width3 = enemy_size3[0] # 적의 가로
enemy_height3 = enemy_size3[1] # 적의 세로
enemy_x_pos3 = 0
enemy_y_pos3 = random.sample(range(enemy_height3, screen_height - enemy_height3), 1)[0] # 화면 세로 가운데 위치 (세로)

# 티모4
enemy4 = pygame.image.load("C:/py/python/pygame_basic/timo.png")
enemy_size4 = enemy4.get_rect().size # 이미지의 크기를 구해옴
enemy_width4 = enemy_size4[0] # 적의 가로
enemy_height4 = enemy_size4[1] # 적의 세로
enemy_x_pos4 = 480 - enemy_width4
enemy_y_pos4 = random.sample(range(enemy_height4, screen_height - enemy_height4), 1)[0] # 화면 세로 가운데 위치 (세로)

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성. (폰트, 크기)

# 총 시간
total_time = 60

# 시작 시간 정보.
ticks = pygame.time.get_ticks() #시작 tick을 받아옴.

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초방 프레임 수 설정. 30프레임.
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
    enemy_y_pos2 -= Enermy_speed
    enemy_x_pos3 += Enermy_speed
    enemy_x_pos4 -= Enermy_speed

    character_x_pos += to_x * dt #프레임에 따라 캐릭터가 이동하는 속도를 고정하도록 지정하기 위함.
    character_y_pos += to_y * dt #프레임에 따라 캐릭터가 이동하는 속도를 고정하도록 지정하기 위함.

    #캐릭터가 화면 밖으면 벗어나지 않도록 하기 위해 위치를 지정한다.
    #가로 경계값 처리

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.sample(range(enemy_width, screen_width - enemy_width), 1)[0]
        total_score += score

    if enemy_y_pos2 < 0:
        enemy_y_pos2 = 640
        enemy_x_pos2 = random.sample(range(enemy_width2, screen_width - enemy_width2), 1)[0]
        total_score += score

    if enemy_x_pos3 > screen_width:
        enemy_y_pos3 = random.sample(range(enemy_height3, screen_width - enemy_height3), 1)[0]
        enemy_x_pos3 = 0
        total_score += score
    
    if enemy_x_pos4 < 0:
        enemy_y_pos4 = random.sample(range(enemy_height4, screen_width - enemy_height4), 1)[0]
        enemy_x_pos4 = 480
        total_score += score

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

    enemy_rect2 = enemy.get_rect()
    enemy_rect2.left = enemy_x_pos2
    enemy_rect2.top = enemy_y_pos2

    enemy_rect3 = enemy.get_rect()
    enemy_rect3.left = enemy_x_pos3
    enemy_rect3.top = enemy_y_pos3

    enemy_rect4 = enemy.get_rect()
    enemy_rect4.left = enemy_x_pos4
    enemy_rect4.top = enemy_y_pos4

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    elif character_rect.colliderect(enemy_rect2):
        print("충돌했어요")
        running = False
    elif character_rect.colliderect(enemy_rect3):
        print("충돌했어요")
        running = False
    elif character_rect.colliderect(enemy_rect4):
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 케릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 티모1 그리기
    screen.blit(enemy2, (enemy_x_pos2, enemy_y_pos2)) # 티모2 그리기
    screen.blit(enemy3, (enemy_x_pos3, enemy_y_pos3)) # 티모3 그리기
    screen.blit(enemy4, (enemy_x_pos4, enemy_y_pos4)) # 티모4 그리기

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - ticks) / 1000 #밀리세컨드 초로 환산.
    #결과 시간을 1000으로 나누어서 초 단위로 표시

    # 출력할 글자, True, 글자 색상
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) #실제 글자를 그리는 것.
    #int로 변경해서 초단위 표시하도록 하기 위해 int로 변경하고 다시 string으로 변환하여 출력.
    screen.blit(timer, (10, 10))

    # Score
    score_letter = game_font.render("SCORE: " + str(total_score), True, (255, 255, 255))
    screen.blit(score_letter, (290, 10))
    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <=0:
        print("타임아웃!")
        running = False

    #10초마다 티모 속도증가 & 점수 증가치 증가

    if timedelta(seconds=10) <= datetime.now() - last_moved_time: #시작시간에서 현재시간 인터벌체크
        Enermy_speed += 0.8 #티모속도 증가
        score += 50 #획득 점수 가중치
        pygame.mixer.Sound.play(voice) #야스오 음성
        last_moved_time = datetime.now() #시작시간을 다시 현재로 수정

    pygame.display.update() # 게임 화면을 다시 그리기!

# 잠시대기 && 점수팝업 기타...
evaluation = "쓰레기"
comment = "사람인가?"

if total_score > 2000 and total_score < 8000:
    evaluation = "일반인"
    comment = "분발하세요"
elif total_score > 8000 and total_score < 15000:
    evaluation = "상위1%"
    comment = "충분합니다"
elif total_score > 15000 and total_score < 20000:
    evaluation = "운동선수"
    comment = "실화임?"
elif total_score > 20000:
    evaluation = "신"
    comment = "여기는 당신이 있을 곳이 아닙니다."

score_set = "Score: " + str(total_score)

total_print = """ {}
"level: " {}
{}""".format(score_set, evaluation, comment)

messagebox.showinfo('당신의 점수는?', total_print)

pygame.time.delay(2000) #2초 정도 대기

# pygame 종료
pygame.quit()