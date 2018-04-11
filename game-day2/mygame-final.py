# TODO -----------------------------------------------------
# 1. 클래스를 사용해 모듈화하기
#    a. 배경처리용 클래스 ScrollBackground 만들기
#    b. 멤버 변수: x, y, scroll_size, scroll_orientation
#    c. 멤버 함수: set_size(size), set_speed(speed)
# 2. 비행기 이미지 생성
# 3. up/down 키 처리
# 4. 비행기 움직이기: up/down 키로 이동, 누른 상태는 up/down 계속
#    a. 비행기 좌표 계산
#    b. 비행기 그리기
# ----------------------------------------------------------

import pygame

# global variables
pad_width = 800
pad_height = 512
BgColor = (255, 0, 255)


# TODO-1a 클래스를 사용해 배경그리기 모듈화하기
class ScrollBackground:

    # TODO-1b
    def __init__(self, file_name):
        self.file = file_name
        self.x1 = 0
        self.y = 0
        self.m = 3
        self.image = pygame.image.load(file_name).convert_alpha()
        self.w = self.image.get_width()
        self.x2 = self.x1 + self.w

    def __del__(self):
        self.image = None

    def set_pos(self, x, y):
        self.x1 = x
        self.x2 = x + self.w
        self.y = y

    def set_speed(self, speed):
        self.m = speed

    def set_size(self, width, height):
        temp = pygame.image.load(self.file).convert_alpha()
        self.image = pygame.transform.scale(temp, (width, height))
        self.w = self.image.get_width()

    def set_scale(self, scale_x, scale_y):
        temp = pygame.image.load(self.file).convert_alpha()
        width = int(temp.get_width()*scale_x)
        height = int(temp.get_height()*scale_y)
        self.image = pygame.transform.scale(temp, (width, height))
        self.w = self.image.get_width()

    def draw(self, surface):
        self.x1 += self.m
        self.x2 += self.m
        if self.x1 <= self.w*(-1):
            self.x1 = self.w
        if self.x2 <= self.w*(-1):
            self.x2 = self.w
        surface.blit(self.image, (self.x1, self.y))
        surface.blit(self.image, (self.x2, self.y))


# init graphics
def init():
    global game_pad, bgImage1, bgImage2, clock

    pygame.init()
    game_pad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("My PyGame")

    # prepare resources
    # image height = 1024
    bgImage1 = ScrollBackground("res/city_background_night_gray.png")
    bgImage2 = ScrollBackground("res/city_background_clean.png")
    bgImage2.set_scale(0.6, 0.6)
    bgImage2.set_pos(0, int(pad_height*0.6))

    # TODO-3

    clock = pygame.time.Clock()


def run():
    global game_pad, bgImage1, bgImage2, clock

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # TODO-4
            # TODO-5a

        # draw background color
        # game_pad.fill(BgColor)

        # draw scrolling background
        bgImage1.draw(game_pad)
        bgImage2.draw(game_pad)

        # TODO-3
        # TODO-5b
        # update display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def main():
    init()
    run()


# python 파일을 실행할때만 main()을 호출한다.
if __name__ == "__main__":
    main()
