
import pygame_textinput
import pygame
import util
import login
from pygame_textinput import *


class Main_page():
    def __init__(self,name,token):
        pygame.init()
        self.name = name
        self.token = token

        self.font = pygame.font.Font('sources/font/simsun.ttc', 35)
        self.font_info = pygame.font.Font('sources/font/simsun.ttc', 18)
        self.window = pygame.display.set_mode((1140, 630))
        pygame.display.set_caption("猪尾巴")  #设置标题
        self.clock = pygame.time.Clock()
        # Pygame now allows natively to enable key repeat:
        pygame.key.set_repeat(200, 25)
        # self.run()

    def render(self):
        self.window.fill((225, 225, 225))
        background = pygame.image.load('sources/images/main_page_back.jpg')
        image1 = pygame.transform.rotozoom(background, 0, 1)
        self.window.blit(image1, (0, 0))
        #用户名
        text = self.font_info.render(self.name, True, (0, 34, 119))
        self.window.blit(text, (1000, 26))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                pos = pygame.mouse.get_pos()
                #人人
                if pos[0]>60 and pos[0] < 236 and pos[1] >384 and pos[1] <439:
                    return False,{"status":2}
                #人机
                elif pos[0]>436 and pos[0] < 614 and pos[1] >384 and pos[1] <439:
                    return False,{"status":3}
                #在线
                elif pos[0]>806 and pos[0] < 982 and pos[1] >384 and pos[1] <439:
                    return False,{"status":4}
                #返回
                elif pos[0]>1092 and pos[0] < 1118 and pos[1] >23 and pos[1] <47:
                    return False,{"status":0}
        pygame.display.update()
        self.clock.tick(30)
        return True,None


    def run(self):
        pygame.mixer.init()
        backgroung_music = pygame.mixer.Sound("sources/video/bacakgrount.wav")
        backgroung_music.play(-1)
        while True:
            status, data = self.render()
            if not status:
                return data

    def showInfo(self,text,pos):
        msg = self.font_info.render(text, True, (0, 34, 119))
        self.window.blit(msg, pos)
        pygame.display.update()
        pygame.time.wait(2000)
        self.render()

# 主界面
