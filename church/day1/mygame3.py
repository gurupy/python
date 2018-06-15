# TODO -----------------------------------------------------
# 1. 비행기 움직이기
#    a. 비행기용 이미지 준비
#    b. 화살표 up/down 키 이벤트 받기
#    d. 이미지 그리기
# 2. 비행기 좌표 계산 개선
#    a. 키를 누르고 있는 동안 계속 이동
#    b. 이미지 좌표 계산
#    c. up 키를 눌렀을 때 화면을 벗어나서 위로 올라가지 못하게 하기
#    d. down 키를 눌렀을 때 화면을 벗어나서 아래로 내려가지 못하게 하기
# ----------------------------------------------------------

import pygame

# global variables
pad_width = 640
pad_height = 480
BgColor = (255, 255, 255)

# initialize pygame module
pygame.init()

# create game window
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("My 3rd PyGame")

# 배경 이미지 생성하기
bgImage = pygame.image.load("bg_cloud.png").convert()
# 배경 이미지를 게임화면에 가득 채우도록 크기 조절하기
bgImage = pygame.transform.scale(bgImage, (pad_width, pad_height))
bgImage2 = bgImage

# TODO-1a
# 비행기 이미지 준비
# 파일명: "warship.png", 크기조절: (40,40)

# create refresh timer
clock = pygame.time.Clock()

# 배경 이미지 좌표 저장
bg_x = 0
bg2_x = pad_width

# 비행기 이미지 좌표 저장
ship_y = pad_height/2
ship_dy = 0

running = True
while running:
    for event in pygame.event.get():
        # pygame 모듈의 기능을 사용해서 게임창 닫기 버튼이 눌렸는지 조사
        if event.type == pygame.QUIT:
            running = False

        # TODO-1b
        # 키보드가 눌렸는지 확인하고: pygame.KEYDOWN
        # TODO-1c
        # 그 키가 UP/DOWN 화살표키인지 확인: pygame.K_UP, ygame.K_DOWN
            # 화살표키 UP이면 비행기 Y좌표를 감소
            # 화살표키 DOWN이면 비행기 Y좌표를 증가
        # TODO-2a
        # UP/DOWN 키가 눌려있는 동안은 비행기 Y좌표를 계속 증가/감소
        # 키가 떨어지면 비행기 Y좌표 그대로: pygame.KEYUP

    # fill game window with background color
    game_pad.fill(BgColor)

    # 그려지는 배경 이미지가 왼쪽으로 이동하도록 좌표 계산
    bg_x = bg_x - 10
    bg2_x = bg2_x - 10

    # 그려지는 이미지가 화면을 완전히 벗어나면 좌표를 처음 위치로 변경
    if bg_x < -bgImage.get_width():
        bg_x = pad_width-10
    if bg2_x < -bgImage2.get_width():
        bg2_x = pad_width-10

    # draw image on game window
    game_pad.blit(bgImage, (bg_x, 0))
    game_pad.blit(bgImage2, (bg2_x, 0))

    # TODO-2b
    # 비행기 이미지 좌표 계산

    # TODO-2c
    # 비행기 좌표가 화면 위로 벗어나면 화면 맨 상단으로 고정

    # TODO-2d
    # 비행기 좌표가 화면 아래로 벗어나면 화면 맨 아래로 고정

    # TODO-1d
    # draw battleship

    # update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
