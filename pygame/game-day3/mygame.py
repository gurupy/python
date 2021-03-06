# TODO -----------------------------------------------------
# 1. 클래스를 사용해 모듈화하기
#    a. 폭파시킬 적 Enemy 클래스 만들기
# 2. 랜덤 위치에서 Enemy 생성하기
# 3. up/down 키 처리
# 4. 비행기 움직이기: up/down 키로 이동, 누른 상태는 up/down 계속
#    a. 비행기 좌표 계산
#    b. 비행기 그리기
# ----------------------------------------------------------

import pygame


# 클래스를 사용해 배경그리기 모듈화
class ScrollBackground:
    def __init__(self, file_name):
        # self.file = file_name
        self.x1 = 0
        self.y = 0
        self.m = 3
        self.image = pygame.image.load(file_name).convert_alpha()
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x2 = self.w

    def __del__(self):
        self.image = None

    def set_pos(self, x, y):
        self.x1 = x
        self.x2 = x + self.w
        self.y = y

    def set_speed(self, speed):
        self.m = speed

    def set_size(self, width, height):
        # temp = pygame.image.load(self.file).convert_alpha()
        # self.image = pygame.transform.scale(temp, (width, height))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x2 = self.x1 + self.w

    def get_size(self):
        return self.w, self.h

    def set_scale(self, scale_x, scale_y):
        # temp = pygame.image.load(self.file).convert_alpha()
        # width = int(temp.get_width()*scale_x)
        # height = int(temp.get_height()*scale_y)
        width = int(self.w * scale_x)
        height = int(self.h * scale_y)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x2 = self.x1 + self.w
        # print(self.w, temp.get_width(), temp.get_height(), scale_x, scale_y, width, height)

    def draw(self, surface):
        self.x1 -= self.m
        self.x2 -= self.m
        if self.x1 <= self.w * (-1):
            self.x1 = self.w
        if self.x2 <= self.w * (-1):
            self.x2 = self.w
        surface.blit(self.image, (self.x1, self.y))
        surface.blit(self.image, (self.x2, self.y))
        # print(self.x1, self.x2, self.y)


# 클래스를 사용해 비행기 그리기 모듈화
class BattleShip:
    HitSound = None
    
    def __init__(self, file_name):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(file_name).convert_alpha()
        self.w = self.image.get_width()
        self.h = self.image.get_height()

        # default bullet (w,h)
        # self.b_size = {'w': 0, 'h': 0}
        self.b_size = (0, 0)

        # default fire effect
        if BattleShip.HitSound is None:
            BattleShip.HitSound = pygame.mixer.Sound("res/hit.wav")
            BattleShip.HitSound.set_volume(0.3)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos_x(self):
        return self.x

    def get_pos_y(self):
        return self.y

    def set_size(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.w = self.image.get_width()
        self.h = self.image.get_height()

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    # TODO change_weapon(w_type), add_weapon(w_type, weapon_file)
    def set_weapon(self, size):
        # self.b_size['w'] = size[0]
        # self.b_size['h'] = size[1]
        self.b_size = size

    # return bullet position: (x, y)
    # or return bullet position: (x, y, weapon_type)
    def fire(self):
        BattleShip.HitSound.play()
        return [self.x + self.w,
                int(self.y + self.h / 2 - self.b_size[0] / 2)]

    def draw(self, surface, move_y):
        self.y += move_y
        if self.y < 0:
            self.y = 0
        pad_height = surface.get_height()
        if self.y > (pad_height - self.h):
            self.y = pad_height - self.h
        surface.blit(self.image, (self.x, self.y))


def main():
    # constants
    pad_width = 1024
    pad_height = 600
    # BgColor = (255, 0, 255)

    # initialize pygame window
    pygame.init()
    game_pad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("My PyGame")

    # create ScrollBackground
    bg_image1 = ScrollBackground("res/city_background_night_gray.png")
    w, h = bg_image1.get_size()
    stretch_ratio = pad_height / h
    bg_image1.set_scale(stretch_ratio, stretch_ratio)
    bg_image1.set_speed(1)

    bg_image2 = ScrollBackground("res/city_background_clean.png")
    stretch_ratio *= 0.6
    bg_image2.set_scale(stretch_ratio, stretch_ratio)
    bg_image2.set_speed(3)
    bg_image2.set_pos(0, int(pad_height - (pad_height * 0.6)))

    # create Battleship
    ship = BattleShip("res/ship.png")
    ship.set_size(50, 30)
    ship.set_pos(30, pad_height / 2 - ship.get_height() / 2)
    # create bullet image
    bullet = pygame.image.load("res/bullet.png").convert_alpha()
    bullet = pygame.transform.scale(bullet, (30, 10))
    ship.set_weapon((30, 10))

    # TODO-
    # create Enemy

    # TODO-
    # create background music & sound effect
    pygame.mixer.init()
    pygame.mixer.music.load("res/bgm_BossMain.wav")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.2)

    
    # get pygame clock
    clock = pygame.time.Clock()

    # drawing values
    s_move_y = 0

    # drawing objects
    bullets = []

    # game main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    s_move_y = -5
                elif event.key == pygame.K_DOWN:
                    s_move_y = 5
                elif event.key == pygame.K_SPACE:
                    bullets.append(ship.fire())

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    s_move_y = 0

        # draw background color
        # game_pad.fill(BgColor)

        # draw scrolling background
        bg_image1.draw(game_pad)
        bg_image2.draw(game_pad)

        # draw battle ship
        ship.draw(game_pad, s_move_y)

        # draw bullets
        if len(bullets) > 0:
            for i, xy in enumerate(bullets):
                game_pad.blit(bullet, xy)
                xy[0] += 5
                if xy[0] > pad_width:
                    bullets.remove(xy)

        # TODO-
        # draw enemies

        # update display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


# python 파일을 실행할때만 main()을 호출한다.
if __name__ == "__main__":
    main()
