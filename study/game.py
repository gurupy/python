import pygame
from random import *

# class spritesheet(object):
#     def __init__(self, filename):
#         try:
#             self.sheet = pygame.image.load(filename).convert()
#         except pygame.error as e:
#             print ('Unable to load spritesheet image:', filename)
#             raise (SystemExit, str(e))
#     # Load a specific image from a specific rectangle
#     def image_at(self, rectangle, colorkey = None):
#         "Loads image from x,y,x+offset,y+offset"
#         rect = pygame.Rect(rectangle)
#         image = pygame.Surface(rect.size).convert()
#         image.blit(self.sheet, (0, 0), rect)
#         if colorkey is not None:
#             if colorkey is -1:
#                 colorkey = image.get_at((0,0))
#             image.set_colorkey(colorkey, pygame.RLEACCEL)
#         return image
#     # Load a whole bunch of images and return them as a list
#     def images_at(self, rects, colorkey = None):
#         "Loads multiple images, supply a list of coordinates"
#         return [self.image_at(rect, colorkey) for rect in rects]
#     # Load a whole strip of images
#     def load_strip(self, rect, image_count, colorkey = None):
#         "Loads a strip of images and returns them as a list"
#         tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
#                 for x in range(image_count)]
#         return self.images_at(tups, colorkey)

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 660
pad_h = 720
f_width = 50
f_height = 50
bg_width = 1024
bullet_h = 10
bullet_w = 30
enemy_size = 40
enemy_types = 30  # 30 different images


def drawObject(obj, xy):
    global game_pad
    game_pad.blit(obj, xy)


def run_game():
    global game_pad, clock, fighter, bgimage, fball, enemy
    global hit, shoot, fire, answers, crash

    x = pad_width * 0.05
    y = pad_height * 0.5
    y_change = 0
    bg1_x = 0
    bg2_x = 1024
    enemyRise = 30
    enemyTimer = 0
    enemyList = [] # enemy list (x, y, img_idx)
    fireList = [] # bullet list (x, y, img_idx)
    shotList = []   # explosion list (x, y, timer)
    answerList = []

    # init enemies
    while len(enemyList) < 5:
        # x, y, image index
        ry = randint(0, pad_height)
        ri = randint(0, enemy_types-1)
        enemyList.append([pad_width - 5, ry, ri])

    crashed = False
    paused = False
    quit = False
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_SPACE:
                    fireList.append([x+f_width, y+((f_height-5)/2), 0])
                    shoot.play()
                elif event.key == pygame.K_RETURN:
                    if crashed:
                        enemyList.clear()
                        shotList.clear()
                        fireList.clear()
                        answerList.clear()
                        enemyRise = 25
                        crashed = False
                    else:
                        paused = not paused
                        
                    if crashed or paused:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    
        if crashed or paused:
            continue

        y += y_change
        if y > pad_height-(f_height):
            y = pad_height-(f_height)
        elif y < 0:
            y=0

        enemyTimer = (enemyTimer +1) % enemyRise
        if enemyTimer == 0 and len(enemyList) < 50:
            # x, y, image index
            ry = randint(0, pad_height)
            ri = randint(0,enemy_types-1)
            enemyList.append([pad_width-5, ry, ri])
            # print (len(enemyList), pad_width-5, ry, ri)

        bg1_x -= 4
        bg2_x -= 4
        if bg1_x <= bg_width*(-1):
            bg1_x = bg_width
        if bg2_x <= bg_width*(-1):
            bg2_x = bg_width

        # draw background
        game_pad.fill((50,100,50))
        drawObject(bgimage, (bg1_x,0))
        drawObject(bgimage, (bg2_x,0))

        # draw fighter
        drawObject(fighter, (x,y))

        # check crash
        fx = x
        fy = y
        for j, jtem in enumerate(enemyList):
            ex = jtem[0]
            ey = jtem[1]
            if fx > ex and fx < ex + enemy_size:
                if (fy > ey and fy < ey + enemy_size) or (fy + f_height > ey and fy + f_height < ey + enemy_size):
                    # print ("hit", fx, fy, ex, ey)
                    crashed = True
                    crash.play()
                    enemyList.remove(jtem)
                    shotList.append([fx, fy, 30])
                    pygame.mixer.music.pause()
                    break;

        # check hit
        for i,  item in enumerate(fireList):
            fx = item[0] + bullet_w   # right x of bullet
            fy = item[1]
            for j, jtem in enumerate(enemyList):
                ex = jtem[0]
                ey = jtem[1]
                if fx > ex and fx < ex + enemy_size:
                    if (fy > ey and fy < ey + enemy_size) or (fy + bullet_h > ey and fy + bullet_h < ey + enemy_size):
                        # print ("hit", fx, fy, ex, ey)
                        if len(answerList) > 20 and answerList.count(jtem[2]) > 0:
                            answerList.remove(jtem[2])
                        else:
                            answerList.append(jtem[2])
                        hit.play()
                        fireList.remove(item)
                        enemyList.remove(jtem)
                        shotList.append([fx, fy, 30])
                        break;

        # draw enemies
        i = 0
        for i,  item in enumerate(enemyList):
            item = enemyList[i]  # x,y,img
            px = item[0]
            py = item[1]
            drawObject(enemy[item[2]], (px, py))
            px -= randint(3,8)
            py += randint(-5, 5)
            if (px < 0):
                px = pad_width
            if (py < -10):
                py = pad_height
            if (py > pad_height-enemy_size):
                py = 0
            item[0]=px
            item[1]=py
            i+=1

        # draw fighter bullets
        if len(fireList) > 0:
            for i, item in enumerate(fireList):
                drawObject(fball[item[2]], (item[0], item[1]))
                #idx = (idx+1)%2
                item[0] += 5
                if (item[0] > pad_width):
                    fireList.remove(item)
                i+=1

        # draw explosion
        for i, item in enumerate(shotList):
            drawObject(fire, (item[0], item[1]))
            item[0] -= 5
            item[2] -= 1
            if (item[2] < 0):
                shotList.remove(item)
            i+=1

        # draw answers
        answerList = list(set(answerList))
        for i, item in enumerate(answerList):
            if item < 13:
                drawObject(answers[item], (20+item*(enemy_size+15), pad_height))
            else:
                drawObject(answers[item], (50+(item-13)*(enemy_size+15), pad_height+30))
            i+=1
        if len(answerList) > 15:
            enemyRise = 10;

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def init_game():
    import os
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (2, 30)

    global game_pad, clock, fighter, bgimage, fball, fire, enemy
    global hit, shoot, answers, crash

    pygame.init()
    game_pad = pygame.display.set_mode((pad_width, pad_h))
    pygame.display.set_caption("Find Bible")

    fighter = pygame.image.load("fighter2.png")
    fighter = pygame.transform.scale(fighter, (f_width, f_height))
    bgimage = pygame.image.load("bg1.png")
    bgimage = pygame.transform.scale(bgimage, (1024, pad_height))
    # fire = spritesheet("fire.jpg")
    # fires = fire.load_strip().convert_alpha()
    fire = pygame.image.load("explosion3.png")

    fb1 = pygame.image.load("fireball-2a.png")
    fb1 = pygame.transform.scale(fb1, (bullet_w, bullet_h))
    fb2 = pygame.image.load("fireball-2a.png")
    fb2 = pygame.transform.scale(fb2, (bullet_w, bullet_h))
    fball = [fb1, fb2]

    # load enemy images
    enemy = []
    for i in range (1, enemy_types+1):
        filename = "a" + str(i) + ".png"
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (enemy_size, enemy_size))
        enemy.append(img)

    answers = []
    for i in range (1, enemy_types+1):
        filename = str(i) + ".png"
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (enemy_size, enemy_size))
        answers.append(img)

    # load audio files
    pygame.mixer.init()
    hit = pygame.mixer.Sound("boom2.wav")
    crash = pygame.mixer.Sound("boom.wav")
    shoot = pygame.mixer.Sound("shoot.wav")
    hit.set_volume(0.2)
    crash.set_volume(0.2)
    shoot.set_volume(0.05)
    pygame.mixer.music.load('BossMain.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

    clock = pygame.time.Clock()
    run_game()


init_game()
