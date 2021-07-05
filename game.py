import pygame
import sys
import random
from time import sleep
from pygame.locals import *
import datetime

# 파이게임 설정 초기화
pygame.init() 
pygame.mixer.init()

# 음악 재생
pygame.mixer.music.load("bgm3.mp3")
volume = 0.5
pygame.mixer.music.play()

# 글자 설정
letter = pygame.font.SysFont("malgungothic", 50, True, False)

# 사진 데이터 및 크기 설정
size_x = 200
size_y = 150
img_kart = pygame.image.load('C:\\Users\\김휘석\\Downloads\\metadata\\kart\\34011fbdc092a2a2d5481c8c038a9f72c355df37dc8e547a1ef612693b81db55.png')
img_kart = pygame.transform.scale(img_kart, (size_x, size_y))
img_character1 = pygame.image.load('C:\\Users\\김휘석\\Downloads\\metadata\\character\\2ecb10f5e23493727a80a91421d6242a18b131f743676e72317bde4bd5d27131.png')
img_character1 = pygame.transform.scale(img_character1, (size_x, size_y))
img_character2 = pygame.image.load('C:\\Users\\김휘석\\Downloads\\metadata\\character\\43dbe2daec2b1995d8b34003f8883463e941d38d2a6201b3ee1dc56d39d5f5ec.png')
img_character2 = pygame.transform.scale(img_character2, (size_x, size_y))
img_character3 = pygame.image.load('C:\\Users\\김휘석\\Downloads\\metadata\\character\\eaf50a8e18f39a9943254098efdb924aac108eb698a34e9a968bc7bebe383a53.png')
img_character3 = pygame.transform.scale(img_character3, (size_x, size_y))

# 파이게임 화면 띄우기
screen = pygame.display.set_mode((1900,1000))

# 변수들 설정
run = True ## 게임 실행 여부
x_car = 400 ## 자동차의 x 위치
y_car = 300 ## 자동차의 y 위치
color = [0, 0, 255] ## 배경색
flipped = False ## 자동차의 좌우 반전
to_dark = False # 화면이 어두워야할지 밝아져야 할지 여부
to_left_character1 = True # 캐릭터의 이동방향이 왼쪽인가?
to_left_character2 = True
to_left_character3 = True
character1 = False # 캐릭터가 보여져야 하는가?
character2 = False
character3 = False
x_character1 = 1400 # 캐릭터의 x 위치
x_character2 = 1400
x_character3 = 1400
y_character1 = round(random.random() * 900) # 캐릭터의 y 위치
y_character2 = round(random.random() * 900)
y_character3 = round(random.random() * 900)
game_over = False # 게임 오버 상황
start = False # 사용자가 시작 버튼을 눌렀는지 아닌지 판단
life = 3 # 라이프의 초기 개수
damage = False # 데미지를 받아야 할 상황인가?
already = False # 이미 데미지를 받은 상황인가?
is_first = True # 시간 측정이 완료되었는가?

# 파이게임 유저 이벤트 설정
BACKGROUND_EVENT = pygame.USEREVENT
CHARACTER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BACKGROUND_EVENT, 1)
pygame.time.set_timer(CHARACTER_EVENT, 5000)
pygame.time.set_timer(CHARACTER_EVENT + 1, 5700, True)
pygame.time.set_timer(CHARACTER_EVENT + 2, 6400, True)

#캐릭터들이 겹쳐있는가? 
def is_hit(x_character, y_character, x_car, y_car, size_x, size_y):
    if x_character < x_car and x_car < x_character + size_x and y_character < y_car and y_car < y_character + size_y:
        return True
    elif x_character < x_car + size_x and x_car + size_x < x_character + size_x and y_character < y_car and y_car < y_character + size_y:
        return True
    elif x_character < x_car and x_car < x_character + size_x and y_character < y_car + size_y and y_car + size_y< y_character + size_y:
        return True
    elif x_character < x_car + size_x and x_car + size_x < x_character + size_x and y_character < y_car + size_y and y_car + size_y < y_character + size_y:
        return True
    return False

while run:
    if start == False: #게임이 시작했는가?
        text = letter.render("쉬운 난이도 : E(Easy) 보통 난이도: H(Hard) 어려운 난이도: I(Insane)", True, (0,0,0))
        screen.fill(color) #배경을 색깔로 채우기
        screen.blit(text, (200, 400)) # 글자를 지정한 위치에 띄우기
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # 키를 누르면 난이도에 맞는 게임 실행
                if event.key == K_e:
                    speed = 3
                    start = True
                if event.key == K_h:
                    speed = 5
                    start = True
                if event.key == K_i:
                    speed = 7
                    start = True
                if start == True:
                    start_time = datetime.datetime.now()
            if event.type == pygame.QUIT: # 종료 버튼을 누르면 게임 종료
                pygame.quit()
                run = False
        pygame.display.flip()
    elif start == True:
        if game_over == False:
            # 캐릭터가 나오는 시간을 무작위로 설정
            time_character1 = round(random.random() * 7000) + 1000
            time_character2 = round(random.random() * 7000) + 1000
            time_character3 = round(random.random() * 7000) + 1000
            screen.fill(color) # 화면 채우기
            clicked = pygame.mouse.get_pressed() # 장치가 눌려있는지 확인하는 함수
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RIGHT] == 1: # 눌려있으면 자동차 이동
                x_car += 8
            if pressed[pygame.K_LEFT] == 1:
                x_car -= 8
            if pressed[pygame.K_UP] == 1:
                y_car -= 8
            if pressed[pygame.K_DOWN] == 1:
                y_car += 8
            for event in pygame.event.get():
                if event.type == CHARACTER_EVENT: # 캐릭터 나타나기
                    pygame.time.set_timer(CHARACTER_EVENT, time_character1)
                    character1 = not character1
                if event.type == CHARACTER_EVENT + 1:
                    pygame.time.set_timer(CHARACTER_EVENT + 1, time_character2)
                    character2 = not character2
                if event.type == CHARACTER_EVENT + 2:
                    character3 = not character3
                    pygame.time.set_timer(CHARACTER_EVENT + 2, time_character3)
                    character3_first = False
                if event.type == BACKGROUND_EVENT: #배경화면 바꾸기
                    if not to_dark:
                        color[1] += 0.3
                        if color[1] > 255:
                            color[1] = 255
                            to_dark = True
                    else:
                        color[1] -= 0.3
                        if color[1] < 0:
                            color[1] = 0
                            to_dark = False 
                if event.type == pygame.KEYDOWN: # 키보드로 자동차 움직이기
                    if event.key == pygame.K_RIGHT:
                        if flipped == True:
                            flipped = False
                            img_kart = pygame.transform.flip(img_kart, True, False)
                            x_car += 100
                    if event.key == pygame.K_LEFT:
                        if flipped == False:
                            flipped = True
                            img_kart = pygame.transform.flip(img_kart, True, False)
                            x_car -= 100
                    if event.key == pygame.K_UP:
                        y_car -= 100
                    if event.key == pygame.K_DOWN:
                        y_car += 100
                    if event.key == pygame.K_2: # 1번과 2번을 누르면서 음량 조절
                        volume += 0.2
                        if volume > 1:
                            volume = 1
                    if event.key == pygame.K_1:
                        volume -= 0.2
                        if volume < 0:
                            volume = 0
                if event.type == pygame.QUIT: # 종료 버튼을 누르면 게임 종료
                    pygame.quit()
                    run = False
            # 자동차가 화면을 벗어나지 않게 하기
            if y_car < 0:
                y_car = 0
            if x_car < 0:
                x_car = 0
            if y_car > 1000 - size_y:
                y_car = 1000 - size_y
            if x_car > 1900 - size_x:
                x_car = 1900 - size_x
            #사진들 띄우기
            screen.blit(img_kart, (x_car, y_car))
            ## 캐릭터 1
            if character1 == True:
                screen.blit(img_character1, [x_character1, y_character1])
                if to_left_character1 == True:
                    x_character1 -= speed
                else:
                    x_character1 += speed
                if x_character1 <= 0:
                    character1 = False
                    y_character1 = round(random.random() * 900)
                if x_character1 >= 1400:
                    character1 = False
                    y_character1 = round(random.random() * 900)
            if x_character1 < 1:
                to_left_character1 = False
                x_character1 = 0
            if x_character1 > 1400:
                to_left_character1 = True
                x_character1 = 1400


            ## 캐릭터 2
            if character2 == True:
                screen.blit(img_character2, [x_character2, y_character2])
                if to_left_character2 == True:
                    x_character2 -= speed
                else:
                    x_character2 += speed
                if x_character2 <= 0:
                    character2 = False
                    y_character2 = round(random.random() * 900)
                if x_character2 >= 1400:
                    character2 = False
                    y_character2 = round(random.random() * 900)
            if x_character2 < 1:
                to_left_character2 = False
                x_character2 = 0
            if x_character2 > 1400:
                to_left_character2 = True
                x_character2 = 1400
            
            ## 캐릭터 3
            if character3 == True:
                screen.blit(img_character3, [x_character3, y_character3])
                if to_left_character3 == True:
                    x_character3 -= speed
                else:
                    x_character3 += speed
                if x_character3 <= 0:
                    character3 = False
                    y_character3 = round(random.random() * 900)
                if x_character3 >= 1400:
                    character3 = False
                    y_character3 = round(random.random() * 900)
            if x_character3 < 1:
                to_left_character3 = False
                x_character3 = 0
            if x_character3 > 1400:
                to_left_character3 = True
                x_character3 = 1400

            ## 자동차와 캐릭터 충돌
            if is_hit(x_character1, y_character1, x_car, y_car, size_x, size_y) and character1:
                damage = True
            elif is_hit(x_character2, y_character2, x_car, y_car, size_x, size_y) and character2:
                damage = True
            elif is_hit(x_character3, y_character3, x_car, y_car, size_x, size_y) and character3:
                damage = True
            if damage == True and already == False:
                life -= 1
                already = True
            elif not (is_hit(x_character1, y_character1, x_car, y_car, size_x, size_y) or is_hit(x_character2, y_character2, x_car, y_car, size_x, size_y) or is_hit(x_character3, y_character3, x_car, y_car, size_x, size_y)):
                already = False
                damage = False
            if life <= 0:
                game_over = True
            game_end = letter.render("남은 라이프 개수: " + str(life), True, (0,0,0))
            # 게임 종료
            screen.blit(game_end, (100, 100))
            pygame.mixer.music.set_volume(volume)
            pygame.display.flip()
        if game_over == True:
            # 시간 측정 후 화면에 노출
            if is_first == True:
                time_record = str(datetime.datetime.now() - start_time)[:-6]
                is_first = False
            # 게임 종료 글자 생성
            game_end = letter.render("게임 종료", True, (0,0,0))
            record = letter.render(time_record, True, (0,0,0))
            game_continue = letter.render("CONTINUE? Press (Y)es/(N)o", True, (0,0,0))
            # Y 버튼과 N 버튼 감지
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_y:
                        start = False
                        game_over = False
                        life = 3
                        is_first = True               
                    elif event.key == K_n:
                        run = False
            # 화면 조정
            screen.fill(color)
            screen.blit(record, (700, 400))
            screen.blit(game_continue, (800,500))
            screen.blit(game_end, (100,100))
            pygame.display.flip()
sys.exit()