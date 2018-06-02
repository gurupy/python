# TODO -----------------------------------------------------
# 1. 게임창 만들기
# 2. 배경 이미지 만들기
# 3. 1초 60번씩 화면을 다시 그리기 위한 타이머 만들기
# 4. 게임창을 닫을 때까지 반복해서 게임화면을 그리기
#  a. 게임창 닫기 버튼이 눌렸는지 확인
#  b. 게임창에 배경색 칠하기
#  c. 게임창에 이미지 그리기
# 5. 게임을 종료함
# ----------------------------------------------------------

import pygame

# global variables
pad_width = 540
pad_height = 512
BgColor = (255, 255, 255)

# initialize pygame module
pygame.init()

# TODO-1
# create game window
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("My PyGame")

# TODO-2
# prepare background resources
bgImage = pygame.image.load("bg_cloud.png").convert()
bgImage = pygame.transform.scale(bgImage, (pad_width, pad_height))

# TODO-3
# create refresh timer
clock = pygame.time.Clock()

# TODO-4
running = True
while running:
    # pygame 모듈의 기능을 사용해서 이벤트 가져오기
    # 예) 키보드가 눌렸는지, 마우스가 움직였는지 등...
    for event in pygame.event.get():
        # pygame 모듈의 기능을 사용해서 게임창 닫기 버튼이 눌렸는지 조사
        # 닫기 버튼이 눌렸으면 게임화면 그리기를 종료하기 위해 running울 False로 바꿈
        if event.type == pygame.QUIT:
            running = False

    # TODO-4b
    # fill game window with background color
    game_pad.fill(BgColor)

    # TODO-4c
    # draw image on game window
    game_pad.blit(bgImage, (0, 0))

    # update display
    # pygame 모듈을 통해 그린 화면을 실제 모니터 화면에 표시함
    pygame.display.update()

    # 1초에 화면이 60회 그려지도록 시간이 남으면 쉬었다가 다음으로 넘어감
    clock.tick(60)

# 게임을 종료함
pygame.quit()

# TODO-5
