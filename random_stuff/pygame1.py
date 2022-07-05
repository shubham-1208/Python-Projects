import os
import pygame
                             # importing various necessary files    
width, height = 800, 600
picture = pygame.image.load(os.path.join('C:/Users/shubh/downloads/wallpaper2.jpg'))
sound = os.path.join(os.getcwd(), 'C:/Users/shubh/Desktop/study/123/p/fall.mp3')
#sound = os.path.join(os.getcwd(), 'C:/Users/shubh/anaconda3/pkgs/spyder-4.2.5-py38haa95532_0/Lib/site-packages/spyder/plugins/help/utils/js/mathjax/extensions/a11y/invalid_keypress.mp3')
FPS = 60

GScreen = pygame.display.set_mode((width, height))    # setting the display
pygame.display.set_caption("game 1")
 
def draw():
    GScreen.fill((255, 255, 255))
    GScreen.blit(picture, (0, 0))
    pygame.display.update()


def main():

    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw()
       
if __name__ == "__main__":
    main()