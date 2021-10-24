#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：puke 
@File ：people_to_computer.py
@Author ：抱着欣欣看月亮
@Date ：2021/10/24 21:47 
'''
import qipan
import pygame
class People_to_computer(qipan.Qipan):
    def __init__(self):
        super().__init__()

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
        pygame.display.update()
        is_continue, info, winner = self.judge()
        if not is_continue:
            return False, {"status": 1, "winner": winner}
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN or not self.IP_1_action:
                pos = pygame.mouse.get_pos()
                # print(pos)
                # IP2选
                if not self.IP_1_action:
                    pygame.time.wait(1000)
                    # if pos[0] > 43 and pos[0] < len(self.IP_2_cards.keys()) * 19 + 93 + 43 and pos[1] > 61 and pos[
                    #     1] < 197:
                    selected = None
                    ii = 0
                    for k,v in self.IP_2_cards.items():
                        if not self.right_cards:
                            self.IP_2_cards[k] = 1
                            selected = ii
                            self.IP_2_selected = 2
                            break
                        else:
                            if k.split('_')[-1]!=self.right_cards[-1].split('_')[-1]:
                                self.IP_2_cards[k] = 1
                                selected = ii
                                self.IP_2_selected = 2
                                break
                        ii+=1
                    if selected==None:
                        self.left_card_selected = not self.left_card_selected
                        for k, v in self.IP_2_cards.items():
                            self.IP_2_cards[k] = 0
                        if self.left_card_selected:
                            self.IP_2_selected = 1
                    self.show_ip_cards(pos=(43, 17), cards=self.IP_2_cards)
                    self.show_ip_cards(pos=(43, 454), cards=self.IP_1_cards)
                    self.show_left_cards()
                    self.show_right_cards()
                    self.show_button()
                    pygame.time.wait(1000)
                    # IP2确认
                    # if pos[0] > 252 and pos[0] < 252 + 71 and pos[1] > 206 and pos[1] < 206 + 30:
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
# People_to_computer().run()