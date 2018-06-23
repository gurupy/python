# TODO -----------------------------------------------------
# 1. 격추하기
#    a. 총알과 적이 만나면 이미지 삭제
#    b. 이미지 삭제 후 폭발 이미지를 대신 표시
#    c. 폭발 이미지도 1초 후 삭제
# 2. 격추하기 개선
#    a. 폭발 이미지를 여러장의 이미지로 교체해가면서 표시 (에니메이션 효과)
# 3. 충돌하면 폭파 -> 게임 종료
#    a. 비행기와 Enemy가 만나면 비행기 폭파
#    b. 비행기 폭파하면 게임 종료
# 4. 게임 종료 개선
#    a. 비행기 종료하면 폭발 이미지로 교체
#    b. 키 입력을 받아서 엔터키면 다시 시작, 다른 키면 종료
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
# bullet: "fireball.png", size:(30,10)
bull_w = 30
bull_h = 10
bullet = pygame.image.load("fireball.png").convert_alpha()
bullet = pygame.transform.scale(bullet, (bull_w, bull_h))
# 총알 좌표 저장소 준비
bulls_xy = []

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

    # 그려지는 이미지가 왼쪽으로 이동하도록 좌표 계산
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

    # update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
