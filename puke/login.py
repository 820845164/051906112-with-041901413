
import pygame
import util
from pygame_textinput import *


class Login():
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font('sources/font/simsun.ttc', 35)
        self.font_info = pygame.font.Font('sources/font/simsun.ttc', 18)
        self.window = pygame.display.set_mode((1140, 630))
        pygame.display.set_caption("猪尾巴")  #设置标题
        self.clock = pygame.time.Clock()
        # Pygame now allows natively to enable key repeat:
        pygame.key.set_repeat(200, 25)
        self.username = TextInputVisualizer()  #用户名输入框
        self.password = TextInputVisualizer()  #密码输入框
        self.username_writer = False  #是否进行用户名输入
        self.password_writer = False
        # self.run()

    def render(self):
        self.window.fill((225, 225, 225))
        background = pygame.image.load('sources/images/login_bac.jpg')
        image1 = pygame.transform.rotozoom(background, 0, 1)
        self.window.blit(image1, (0, 0))

        text = self.font.render(':', True, (0, 34, 119))
        self.window.blit(text, (415, 225))
        pygame.draw.aaline(self.window, (0,0,0), (431, 259), (628, 259), 1)
        text2 = self.font.render(':', True, (0, 34, 119))
        self.window.blit(text2, (390, 270))
        pygame.draw.aaline(self.window, (0,0,0), (407, 303), (591, 303), 1)

        events = pygame.event.get()
        if self.username_writer:
            self.username.update(events)
            self.window.blit(self.username.surface, (435, 235))
        elif self.password_writer:
            self.password.update(events)
            self.window.blit(self.password.surface, (410, 280))

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #用户名
                if pos[0]>425 and pos[0] < 635 and pos[1] >221 and pos[1] <263:
                    self.username_writer = True
                    self.password_writer = False
                #密码
                elif pos[0]>404 and pos[0] < 602 and pos[1] >274 and pos[1] <306:
                    self.username_writer = False
                    self.password_writer = True
                #登录
                elif pos[0]>432 and pos[0] < 708 and pos[1] >408 and pos[1] <465:
                    self.username_writer = False
                    self.password_writer = False
                    suc,name,token = self.login()
                    if suc:
                        return False,{"status":1,"name":name,"token":token}
        pygame.display.update()
        self.clock.tick(30)
        return True,None

    def login(self):
        username = self.username.value
        password = self.password.value
        if not username or not password:
            self.showInfo(text = "账号与密码不能为空!",pos=(490,380))
        else:
            status,res = util.login(username,password)
            if status:
                name = res["detail"]["name"]
                token = res["token"]
                self.backgroung_music.stop()
                return True,name,token

            else:
                self.showInfo(text=res["error_msg"],pos=(490,380))
                return False,None,None

    def run(self):
        pygame.mixer.init()
        self.backgroung_music = pygame.mixer.Sound("sources/video/bacakgrount.wav")
        self.backgroung_music.play(-1)
        while True:
            status,data = self.render()
            if not status:
                return data

    def showInfo(self,text,pos):
        msg = self.font_info.render(text, True, (0, 34, 119))
        self.window.blit(msg, pos)
        pygame.display.update()
        pygame.time.wait(2000)
        self.render()

    def __del__(self):
        return 1

Login()
