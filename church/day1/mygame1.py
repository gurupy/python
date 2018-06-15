# TODO -----------------------------------------------------
# 1. 배경 움직이기
#    a. 배경 이미지 생성
#    b. 배경 이미지 좌표 계산
#    c. 배경 그리기
# 2. 배경 이미지 좌표 계산 개선
#    : 배경이 화면 밖으로 나가면 다시 그리기
# ----------------------------------------------------------

import pygame

# global variables
pad_width = 540
pad_height = 512
BgColor = (255, 255, 255)

# initialize pygame module
pygame.init()

# create game window
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("My 1st PyGame")

# TODO-1a
# 배경 이미지 생성하기
# 배경 이미지를 게임화면에 가득 채우도록 크기 조절하기

# create refresh timer
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        # pygame 모듈의 기능을 사용해서 게임창 닫기 버튼이 눌렸는지 조사
        if event.type == pygame.QUIT:
            running = False

    # fill game window with background color
    game_pad.fill(BgColor)

    # TODO-1b
    # 그려지는 이미지가 왼쪽으로 이동하도록 좌표 계산

    # TODO-2
    # 그려지는 이미지가 화면을 완전히 벗어나면 좌표를 처음 위치로 변경

    # TODO-1c
    # draw image on game window

    # update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()

# TODO-1c
