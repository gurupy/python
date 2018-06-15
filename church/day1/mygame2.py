# TODO -----------------------------------------------------
# 1. 동일한 배경이미지 2개를 사용해서 끊김없는 배경 스크롤
#    a. 이미지 생성
#    b. 이미지 좌표 계산
#    c. 이미지 그리기
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
pygame.display.set_caption("My 2nd PyGame")

# 배경 이미지 생성하기
bgImage = pygame.image.load("bg_cloud.png").convert()
# 배경 이미지를 게임화면에 가득 채우도록 크기 조절하기
bgImage = pygame.transform.scale(bgImage, (pad_width, pad_height))

# TODO-1a
# 같은 배경 이미지를 한장 더 만들기

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
    # 배경 이미지 좌표 계산

    # TODO-1c
    # draw image on game window
    game_pad.blit(bgImage, (0, 0))

    # update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()

# TODO-1c
