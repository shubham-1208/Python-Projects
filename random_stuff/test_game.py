import sys
import conf_skeing
import pygame
import random

class skier_class(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.direction = 0
        self.imagepaths = conf_skeing.SKIER_IMAGE_PATHS[:-1]
        self.image = pygame.image.load(self.imagepaths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.speed = [self.direction, 6-abs(self.direction)*2]

    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)

        center = self.rect.center
        self.image = pygame.image.load(self.imagepaths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = [self.direction, 6-abs(self.direction)*2]
        return self.speed

    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)

    def set_fall(self):
        self.image = pygame.image.load(conf_skeing.SKIER_IMAGE_PATHS[-1])

    def set_forward(self):
        self.direction = 0
        self.image = pygame.image.load(self.imagepaths[self.direction])



class obstacle_class(pygame.sprite.Sprite):
   
    def __init__(self, img_path, location, attribute):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.attribute = attribute
        self.passed = False

    def move(self, num):
        self.rect.centery = self.location[1] - num


def create_obstacle(s, e, num=10):
    obstacles = pygame.sprite.Group()
    locations = []

    for i in range(num):
        row = random.randint(s, e)
        col = random.randint(0, 9)
        location = [col*64+20, row*64+20]

        if location not in locations:
            locations.append(location)
            attribute = random.choice(list(conf_skeing.OBSTACLE_PATHS.keys()))
            img_path = conf_skeing.OBSTACLE_PATHS[attribute]
            obstacle = obstacle_class(img_path, location, attribute)
            obstacles.add(obstacle)

    return obstacles

def add_obstacles(obstacles0, obstacles1):
    obstacles = pygame.sprite.Group()
    for obstacle in obstacles0:
        obstacles.add(obstacle)
    for obstacle in obstacles1:
        obstacles.add(obstacle)
    return obstacles


def show_start_interface(screen, screensize):
    screen.fill((255, 255, 255))
    tfont = pygame.font.Font(conf_skeing.FONTPATH, screensize[0]//6)
    cfont = pygame.font.Font(conf_skeing.FONTPATH, screensize[0]//25)
    gsfont = pygame.font.Font(conf_skeing.FONTPATH, screensize[0]//30)
    title = tfont.render(u'Skier Game', True, (255, 0, 0))
    content = cfont.render(u'Press any key to START', True, (0, 0, 255))
    name = gsfont.render(u'MADE BY SHUBHAM MEHRA', True, (23, 25, 29))
    trect = title.get_rect()
    trect.midtop = (screensize[0]/2, screensize[1]/5)
    crect = content.get_rect()
    crect.midtop = (screensize[0]/2, screensize[1]/2)
    gsrect = title.get_rect()
    gsrect.midtop = (screensize[0]/2, screensize[1]/7)
    screen.blit(title, trect)
    screen.blit(content, crect)
    screen.blit(name, gsrect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.update()

def show_score(screen, score, pos=(10,10)):
    font = pygame.font.Font(conf_skeing.FONTPATH, 30)
    score_text = font.render("score: %s" % score, True, (0,0,0))
    screen.blit(score_text, pos)

def update_frame(screen, obstacles, skier, score):
    screen.fill((255, 255, 255))
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    show_score(screen, score)
    pygame.display.update()

def main():

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(conf_skeing.BGMPATH)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode(conf_skeing.SCREENSIZE)
    pygame.display.set_caption('Skier Game')

    show_start_interface(screen, conf_skeing.SCREENSIZE)

    skier = skier_class()

    obstacles0 = create_obstacle(20, 29)
    obstacles1 = create_obstacle(10, 19)
    obstacles_flag = 0
    obstacles = add_obstacles(obstacles0, obstacles1)

    clock = pygame.time.Clock()

    distance = 0
    score = 0
    speed = [0, 6]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    speed = skier.turn(1)
        skier.move()
        distance += speed[1]
        if distance >= 640 and obstacles_flag == 0:
            obstacles_flag = 1
            obstacles0 = create_obstacle(20, 29)
            obstacles = add_obstacles(obstacles0, obstacles1)

        if distance >= 1280 and obstacles_flag == 1:
            obstacles_flag = 0
            distance -= 1280
            for obstacle in obstacles0:
                obstacle.location[1] = obstacle.location[1] - 1280
            obstacles1 = create_obstacle(10, 19)
            obstacles = add_obstacles(obstacles0, obstacles1)

        for obstacle in obstacles:
            obstacle.move(distance)

        hitted_obstacles = pygame.sprite.spritecollide(skier, obstacles, False)

        if hitted_obstacles:
            if hitted_obstacles[0].attribute =='tree' and not hitted_obstacles[0].passed:
                if score > 50:
                    score -= 50
                    skier.set_fall()
                    update_frame(screen, obstacles, skier, score)
                    pygame.time.delay(1000)
                    skier.set_forward()
                    speed = [0, 6]
                    hitted_obstacles[0].passed = True
                elif score == 50:
                    score = 0
                    skier.set_fall()
                    update_frame(screen, obstacles, skier, score) 
                    pygame.time.delay(1000)
                    skier.set_forward()
                    speed = [0, 6]
                    hitted_obstacles[0].passed = True
                elif score < 50:
                    score = 0
                    skier.set_fall()
                    update_frame(screen, obstacles, skier, score)
                    pygame.time.delay(1000)
                    skier.set_forward()
                    speed = [0, 6]
                    hitted_obstacles[0].passed = True

            elif hitted_obstacles[0].attribute == 'flag' and not hitted_obstacles[0].passed:
                score += 10
                obstacles.remove(hitted_obstacles[0])




        update_frame(screen, obstacles, skier, score)
        clock.tick(conf_skeing.FPS)




if __name__ =='__main__':
    main()