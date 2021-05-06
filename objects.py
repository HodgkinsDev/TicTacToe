import os
import pygame

class x:
    sprite_file = "./sprites/x.png"
    XPlayer = pygame.image.load(sprite_file)
    sprite = pygame.transform.scale(XPlayer, (100, 100))
    x = 0
    y = 0
    drawn = False

class o:
    sprite_file = "./sprites/o.png"
    OPlayer = pygame.image.load(sprite_file)
    sprite = pygame.transform.scale(OPlayer, (100, 100))
    x = 0
    y = 0
    drawn = False

class line:
    sprite_file = "./sprites/line.png"
    sprite_file_up = "./sprites/upline.png"
    sprite_file_D1 = "./sprites/D1.png"
    sprite_file_D2 = "./sprites/D2.png"
    WinLine = pygame.image.load(sprite_file)
    WinLine2 = pygame.image.load(sprite_file_up)
    WinLine3 = pygame.image.load(sprite_file_D1)
    WinLine4 = pygame.image.load(sprite_file_D2)
    sprite = pygame.transform.scale(WinLine,(300,100))
    sprite_up = pygame.transform.scale(WinLine2,(70,300))
    sprite_D1 = pygame.transform.scale(WinLine3,(300,300))
    sprite_D2 = pygame.transform.scale(WinLine4,(300,300))
    x = 0
    y = 0
    drawn = False

class titleboard:
    sprite_file = "./sprites/title.png"
    boardsprite = pygame.image.load(sprite_file)
    sprite = pygame.transform.scale(boardsprite,(100,100))
    x = 100
    y = 115

class cancel:
    sprite_file = "./sprites/cancel.png"
    cancell = pygame.image.load(sprite_file)
    sprite = pygame.transform.scale(cancell,(100,100))
    x = 100
    y = 85
