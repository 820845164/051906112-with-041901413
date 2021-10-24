
import pygame
import random


class Qipan():
    '''棋盘类'''

    def __init__(self):
        # 加载图片
        self.load_cards()
        # 对局数据-------------------------------------------------------
        self.IP_1_cards = {}
        self.IP_2_cards = {}
        self.left_cards = list(self.cards.keys())
        random.shuffle(self.left_cards)  # 打乱牌堆
        self.right_cards = []
        self.IP_1_action = True
        self.IP_1_selected = 0  # 0未选  1翻牌  2手牌
        self.IP_2_selected = 0
        self.left_card_selected = False
        # ---------------------------------------------------------------
        pygame.init()
        self.font = pygame.font.Font('sources/font/simsun.ttc', 35)
        self.font_info = pygame.font.Font('sources/font/simsun.ttc', 18)
        self.window = pygame.display.set_mode((1140, 641))
        pygame.display.set_caption("猪尾巴")  # 设置标题
        self.clock = pygame.time.Clock()
        # Pygame now allows natively to enable key repeat:
        pygame.key.set_repeat(200, 25)

    def render(self):
        self.window.fill((225, 225, 225))
        background = pygame.image.load('sources/images/qipan_back.jpg')
        image1 = pygame.transform.rotozoom(background, 0, 1)
        self.window.blit(image1, (0, 0))
        # 显示棋牌
        self.show_ip_cards(pos=(43, 17), cards=self.IP_2_cards)
        self.show_ip_cards(pos=(43, 454), cards=self.IP_1_cards)
        self.show_left_cards()
        self.show_right_cards()
        self.show_button()
        is_continue, info, winner = self.judge()
        if not is_continue:
            return False, {"status": 1, "winner": winner}
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # print(pos)
                # IP2选
                if not self.IP_1_action:
                    if pos[0] > 43 and pos[0] < len(self.IP_2_cards.keys()) * 19 + 93 + 43 and pos[1] > 61 and pos[
                        1] < 197:
                        selected = min(len(self.IP_2_cards) - 1, (pos[0] - 43) // 19)
                        keys = list(self.IP_2_cards.keys())
                        for i in range(len(self.IP_2_cards.keys())):
                            if i == selected:
                                self.IP_2_cards[keys[i]] = 1 - self.IP_2_cards[keys[i]]
                                self.IP_2_selected = 2 if self.IP_2_cards[keys[i]] else 0
                            else:
                                self.IP_2_cards[keys[i]] = 0
                    if pos[0] > 50 and pos[0] < 195 and pos[1] > 217 and pos[1] < 426:
                        self.left_card_selected = not self.left_card_selected
                        for k, v in self.IP_2_cards.items():
                            self.IP_2_cards[k] = 0
                        if self.left_card_selected:
                            self.IP_2_selected = 1
                    # IP2确认
                    if pos[0] > 252 and pos[0] < 252 + 71 and pos[1] > 206 and pos[1] < 206 + 30:
                        suc = False
                        if not self.right_cards:
                            if self.IP_2_selected == 1:
                                card = self.left_cards.pop()
                                img = self.cards[card]
                                img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
                                self.window.blit(img, (376, 217))
                                pygame.display.update()
                                pygame.time.wait(2000)

                                self.right_cards.append(card)
                                self.left_card_selected = False
                                suc = True
                            else:
                                for key, value in self.IP_2_cards.items():
                                    if value:
                                        img = self.cards[key]
                                        img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
                                        self.window.blit(img, (376, 217))
                                        pygame.display.update()
                                        pygame.time.wait(2000)
                                        self.right_cards.append(key)
                                        del self.IP_2_cards[key]
                                        suc = True
                                        break
                        else:
                            if self.IP_2_selected == 1:
                                card = self.left_cards.pop()
                                img = self.cards[card]
                                img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
                                self.window.blit(img, (376, 217))
                                pygame.display.update()
                                pygame.time.wait(2000)
                                if card.split('_')[-1] != self.right_cards[-1].split('_')[-1]:
                                    self.right_cards.append(card)
                                else:
                                    self.IP_2_cards[card] = 0
                                    for i in self.right_cards:
                                        self.IP_2_cards[i] = 0
                                    self.right_cards = []
                                self.left_card_selected = False
                                suc = True
                            else:
                                for key, value in self.IP_2_cards.items():
                                    if value:
                                        img = self.cards[key]
                                        img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
                                        self.window.blit(img, (376, 217))
                                        pygame.display.update()
                                        pygame.time.wait(2000)
                                        if key.split('_')[-1] != self.right_cards[-1].split('_')[-1]:
                                            self.right_cards.append(key)
                                            del self.IP_2_cards[key]
                                        else:
                                            self.IP_2_cards[key] = 0
                                            for i in self.right_cards:
                                                self.IP_2_cards[i] = 0
                                            self.right_cards = []
                                        suc = True
                                        break
                        if suc:
                            self.IP_1_action = True
                            self.IP_2_selected = 0



                else:
                    if pos[0] > 43 and pos[0] < len(self.IP_1_cards.keys()) * 19 + 93 + 43 and pos[1] > 498 and pos[
                        1] < 630:
                        selected = min(len(self.IP_1_cards) - 1, (pos[0] - 43) // 19)
                        keys = list(self.IP_1_cards.keys())
                        for i in range(len(self.IP_1_cards.keys())):
                            if i == selected:
                                self.IP_1_cards[keys[i]] = 1 - self.IP_1_cards[keys[i]]
                                self.IP_1_selected = 2 if self.IP_1_cards[keys[i]] else 0
                            else:
                                self.IP_1_cards[keys[i]] = 0
                    if pos[0] > 50 and pos[0] < 195 and pos[1] > 217 and pos[1] < 426:
                        self.left_card_selected = not self.left_card_selected
                        for k, v in self.IP_1_cards.items():
                            self.IP_1_cards[k] = 0
                        if self.left_card_selected:
                            self.IP_1_selected = 1
                    # IP1确认
                    if pos[0] > 252 and pos[0] < 252 + 71 and pos[1] > 418 and pos[1] < 418 + 30 and self.IP_1_selected:
                        suc = False
                        if not self.right_cards:
                            if self.IP_1_selected == 1:
                                card = self.left_cards.pop()
                                img = self.cards[card]
                                img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
                                self.window.blit(img, (376, 217))
                                pygame.display.update()
                                pygame.time.wait(2000)
                                self.right_cards.append(card)
                                self.left_card_selected = False
                                suc = True
                            else:
                                for key, value in self.IP_1_cards.items():
                                    if value:
                                        img = self.cards[key]
                                        img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
                                        self.window.blit(img, (376, 217))
                                        pygame.display.update()
                                        pygame.time.wait(2000)
                                        self.right_cards.append(key)
                                        del self.IP_1_cards[key]
                                        suc = True
                                        break
                        else:
                            if self.IP_1_selected == 1:
                                card = self.left_cards.pop()
                                img = self.cards[card]
                                img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
                                self.window.blit(img, (376, 217))
                                pygame.display.update()
                                pygame.time.wait(2000)
                                if card.split('_')[-1] != self.right_cards[-1].split('_')[-1]:
                                    self.right_cards.append(card)
                                else:
                                    self.IP_1_cards[card] = 0
                                    for i in self.right_cards:
                                        self.IP_1_cards[i] = 0
                                    self.right_cards = []
                                self.left_card_selected = False
                                suc = True
                            else:
                                for key, value in self.IP_1_cards.items():
                                    if value:
                                        img = self.cards[key]
                                        img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
                                        self.window.blit(img, (376, 217))
                                        pygame.display.update()
                                        pygame.time.wait(2000)
                                        if key.split('_')[-1] != self.right_cards[-1].split('_')[-1]:
                                            self.right_cards.append(key)
                                            del self.IP_1_cards[key]
                                        else:
                                            self.IP_1_cards[key] = 0
                                            for i in self.right_cards:
                                                self.IP_1_cards[i] = 0
                                            self.right_cards = []
                                        suc = True
                                        break
                        if suc:
                            self.IP_1_action = False
                            self.IP_1_selected = 0

        pygame.display.update()
        self.clock.tick(30)
        return True, None

    def load_cards(self):
        self.cards = {}
        for i in list(range(2, 11)) + ["A", "J", "Q", "K"]:
            for j in range(4):
                card = str(i) + "_" + str(j)
                self.cards[card] = pygame.image.load(f'sources/images/cards/{card}.jpg')
        self.crad_back = pygame.image.load('sources/images/cards/back.jpg')

    def show_ip_cards(self, pos, cards):
        for card_id, is_up in cards.items():
            img = self.cards[card_id]
            img = pygame.transform.rotozoom(img, 0, 0.9)  # 原图105x50
            self.window.blit(img, (pos[0], pos[1] + (44 * (1 - is_up))))
            pos = (pos[0] + 19, pos[1])

    def show_left_cards(self):
        counts = len(self.left_cards)
        text = self.font_info.render(f'剩余:{counts:0>2}张', True, (0, 0, 0))
        self.window.blit(text, (220, 320))
        if counts:
            img = self.crad_back
            img = pygame.transform.rotozoom(img, 0, 0.83)  # 原图105x50
            self.window.blit(img, (49, 217))
            if self.left_card_selected:
                self.window.blit(img, (70, 200))

    def show_right_cards(self):
        counts = len(self.right_cards)
        text = self.font_info.render(f'剩余:{counts:0>2}张', True, (0, 0, 0))
        self.window.blit(text, (880, 320))
        if counts:
            img = self.cards[self.right_cards[-1]]
            img = pygame.transform.rotozoom(img, 0, 1.4)  # 原图105x50
            self.window.blit(img, (977, 217))

    def show_button(self):
        if self.IP_2_selected:
            pygame.draw.rect(self.window, (255, 255, 255), (252, 206, 71, 30), 0)
            text = self.font_info.render(f'确认', True, (0, 0, 0))
            self.window.blit(text, (252, 201))
        elif self.IP_1_selected:
            pygame.draw.rect(self.window, (255, 255, 255), (252, 418, 71, 30), 0)
            text = self.font_info.render(f'确认', True, (0, 0, 0))
            self.window.blit(text, (252, 418))
        elif not self.IP_1_action:
            pygame.draw.rect(self.window, (255, 255, 255), (895, 206, 65, 30), 0)
            text = self.font_info.render(f'请选择', True, (0, 0, 0))
            self.window.blit(text, (895, 206))
        else:
            pygame.draw.rect(self.window, (255, 255, 255), (895, 418, 65, 30), 0)
            text = self.font_info.render(f'请选择', True, (0, 0, 0))
            self.window.blit(text, (895, 418))

    def judge(self):
        '''判断游戏是否结束'''
        if not self.left_cards:
            info,winner = "平局" if len(self.IP_1_cards) == len(self.IP_2_cards) else '恭喜IP 1获得胜利' if len(
                self.IP_1_cards) < len(self.IP_2_cards) else '恭喜IP 2获得胜利', 'IP 1' if len(self.IP_1_cards) < len(
                self.IP_2_cards) else 'IP 2'
            self.showInfo(info,(420,350))
            return False, info,winner

        return True, None, None

    def run(self):
        pygame.mixer.init()
        self.backgroung_music = pygame.mixer.Sound("sources/video/bacakgrount.wav")
        self.backgroung_music.play(-1)
        while True:
            status, data = self.render()
            if not status:
                return data

    def showInfo(self, text, pos):
        msg = self.font.render(text, True, (0, 34, 119))
        self.window.blit(msg, pos)
        pygame.display.update()
        pygame.time.wait(3000)
        # self.render()

    def __del__(self):
        return 1

# Qipan().run()
# 游戏算法
