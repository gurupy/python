# TODO -----------------------------------------------------
# 1. 비행기에서 총알 쏘기
# 2. 적 Enemy 출현
#    a. 적 이미지 준비, 이미지 좌표 저장소 준비
#    b. 적 생성용 타이머 준비
#    c. 일정시간마다 생성: enemy_timer가 enemy_interval과 같아 질 때
#       생성위지는 화면의 오른쪽 끝, Y좌표는 랜덤으로
#    d. 랜덤함수 사용을 위해 random 패키지 사용
#    e. 화면 업데이트될 때마다 적 이미지 이동
#       화면에서 벗어나면 삭제
# 3. 총알쏘기 효과음 추가
#    a. 효과음 준비
#    b. 총알 쏠 때 효과음 내기
# ----------------------------------------------------------

import pygame
# TODO-2d 랜덤 패키지 추가
from random import *

# global variables
pad_width = 640
pad_height = 480
BgColor = (255, 255, 255)

# initialize pygame module
pygame.init()

# create game window
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("Day2 PyGame")

# 배경 이미지 생성하기
bgImage = pygame.image.load("bg_cloud.png").convert()
# 배경 이미지를 게임화면에 가득 채우도록 크기 조절하기
bgImage = pygame.transform.scale(bgImage, (pad_width, pad_height))
bgImage2 = bgImage
# 비행기 이미지 준비
ship_w = 40
ship_h = 40
ship = pygame.image.load("warship.png")
ship = pygame.transform.scale(ship, (ship_w, ship_h))

# 총알 이미지 준비
bull_w = 30
bull_h = 10
bullet = pygame.image.load("fireball.png").convert_alpha()
bullet = pygame.transform.scale(bullet, (bull_w, bull_h))
# 총알 좌표 저장소 준비
bulls_xy = []

# TODO-2a 적 이미지 준비
# enemy: "enemy.png" size: 원래 이미지 그대로 사용
enemy = pygame.image.load("enemy.png").convert_alpha()
#enemy = pygame.transform.scale(enemy, (enemy_w, enemy_h))
enemy_w = enemy.get_width()
enemy_h = enemy.get_height()
# 적 이미지 좌표 저장소 준비
enemies_xy = []
# 적 이미지 이동속도: 픽셀
enemy_speed_x = 5
#enemy_speed_y = 5

# TODO-2b 적 생성용 타이머 준비
# 이미지 업데이트할 때마다 timer를 증가시킬 것이므로 타이머 단위는 1/60초
# enemy_interval, enemy_timer
enemy_timer = 0
enemy_interval = 20

# create refresh timer
clock = pygame.time.Clock()

# 배경 이미지 좌표 저장
bg_x = 0
bg2_x = pad_width

# 비행기 이미지 좌표 저장
ship_x = 50
ship_y = pad_height/2
ship_dy = 0

running = True
while running:
    for event in pygame.event.get():
        # pygame 모듈의 기능을 사용해서 게임창 닫기 버튼이 눌렸는지 조사
        if event.type == pygame.QUIT:
            running = False
        # 키보드가 눌렸는지 확인
        if event.type == pygame.KEYDOWN:
            # 화살표키 UP이면 비행기 Y좌표를 증가
            if event.key == pygame.K_UP:
                ship_dy -= 5
            # 화살표키 DOWN이면 비행기 Y좌표를 감소
            elif event.key == pygame.K_DOWN:
                ship_dy += 5
            # 스페이스바 키를 누르면 총알 생성 -> 총알 좌표를 목록에 담기
            # 총알 이미지는 같은것을 사용할 것이므로 좌표만 저장하면 된다.
            elif event.key == pygame.K_SPACE:
                bulls_xy.append([ship_x + ship_w,
                    int(ship_y + ship_h/2 - bull_h/2)])
        # 눌렸던 키가 떨어졌는지 확인
        elif event.type == pygame.KEYUP:
            # 화살표키를 떼면 좌표 이동크기를 0으로 변경
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship_dy = 0


    # fill game window with background color
    game_pad.fill(BgColor)

    # 그려지는 배경 이미지가 왼쪽으로 이동하도록 좌표 계산
    bg_x = bg_x - 10
    bg2_x = bg2_x - 10

    # 그려지는 배경 이미지가 화면을 완전히 벗어나면 좌표를 처음 위치로 변경
    if bg_x < -bgImage.get_width():
        bg_x = pad_width-10
    if bg2_x < -bgImage2.get_width():
        bg2_x = pad_width-10

    # draw background image on game window
    game_pad.blit(bgImage, (bg_x, 0))
    game_pad.blit(bgImage2, (bg2_x, 0))

    # draw battleship
    ship_y += ship_dy
    if ship_y < 0:
        ship_y = 0
    elif ship_y > pad_height-ship_h:
        ship_y = pad_height-ship_h
    game_pad.blit(ship, (ship_x, ship_y))

    # draw bullets
    if len(bulls_xy) > 0:
        for i, xy in enumerate(bulls_xy):
            game_pad.blit(bullet, xy)
            xy[0] += 5
            if xy[0] > pad_width:
                bulls_xy.remove(xy)

    # TODO-2c 일정 시간마다 적 이미지 생성
    enemy_timer += 1
    if enemy_timer > enemy_interval:
        # create enemy 좌표
        enemies_xy.append([pad_width - enemy_w,
            randint(0, pad_height-enemy_h)])
        # reset timer
        enemy_timer = 0

    # TODO-2e 적 이미지 좌표이동
    # 화면 벗어나면 삭제: x좌표가 0보다 작아질 때
    # 적 이미지 그리기
    for i, xy in enumerate(enemies_xy):
        # x좌표를 왼쪽으로 스피드만큼 이동함
        xy[0] -= enemy_speed_x
        if xy[0] < 0:
            # y좌표도 위아래로 조금씩 이동하도록 함
            xy[1] = randint(-3, 3)
            enemies_xy.remove(xy)
        else:
            game_pad.blit(enemy, xy)

    # update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
