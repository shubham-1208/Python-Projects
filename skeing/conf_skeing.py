import sys
import os


FPS = 60
SCREENSIZE = (640, 640)
SKIER_IMAGE_PATHS = [
    os.path.join(os.getcwd(), 'skier_forward.png'),
    os.path.join(os.getcwd(), 'skier_right1.png'),
    os.path.join(os.getcwd(), 'skier_right2.png'),
    os.path.join(os.getcwd(), 'skier_left2.png'),
    os.path.join(os.getcwd(), 'skier_left1.png'),
    os.path.join(os.getcwd(), 'skier_fall.png')
]

OBSTACLE_PATHS = {
    'tree': os.path.join(os.getcwd(), 'tree.png'),
    'flag': os.path.join(os.getcwd(), 'flag.png')
}

BGMPATH = os.path.join(os.getcwd(), 'bgm.mp3')
FONTPATH = os.path.join(os.getcwd(), 'FZSTK.TTF')