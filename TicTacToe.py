import os
from objects import x,o,line,titleboard,cancel
import time
# Importing Pygame
import pygame
  
# Initializing Pygame 
pygame.init() 
pygame.display.set_caption('Tic Tac Toe 1.0')
  
# Initializing surface 
surface = pygame.display.set_mode((300,300))

#Initalizing Font
font = pygame.font.Font('./font.ttf', 60)
font2 = pygame.font.Font('./font.ttf', 20)
font3 = pygame.font.Font('./font.ttf', 40)
font4 = pygame.font.Font('./font.ttf', 60)
font5 = pygame.font.Font('./font.ttf', 40)
font6 = pygame.font.Font('./font.ttf', 40)
font7 = pygame.font.Font('./font.ttf', 60)
font8 = pygame.font.Font('./font.ttf', 40)

color = (255,0,0) 
Black = (0,0,0)
green = (0, 255, 0)
blue = (0, 0, 128)
White = (255,255,255)

#Creating Each X and O
Player_X1 = x()
Player_X2 = x()
Player_X3 = x()
Player_X4 = x()
Player_X5 = x()
Player_X6 = x()
Player_X7 = x()
Player_X8 = x()
Player_X9 = x()
Player_X10 = x()
Player_X11 = x()
Player_O1 = o()
Player_O2 = o()
Player_O3 = o()
Player_O4 = o()
Player_O5 = o()
Player_O6 = o()
Player_O7 = o()
Player_O8 = o()
Player_O9 = o()
Player_O10 = o()
Player_O11 = o()

line1 = line()
line2 = line()
line3 = line()
line4 = line()
line5 = line()
line6 = line()
line7 = line()
line8 = line()

ttlboard = titleboard()
cancel_sign = cancel()

line1.x = 0
line1.y = 0
line2.x = 0
line2.y = 100
line3.x = 0
line3.y = 200
line4.x = 20
line4.y = 0
line5.x = 120
line5.y = 0
line6.x = 220
line6.y = 0
line7.x = 0
line7.y = 0
line8.x = 0
line8.y = 0

#X For Each Square
Player_X1.x = 0
Player_X1.y = 0
Player_X2.x = 100
Player_X2.y = 0
Player_X3.x = 200
Player_X3.y = 0
Player_X4.x = 0
Player_X4.y = 100
Player_X5.x = 100
Player_X5.y = 100
Player_X6.x = 200
Player_X6.y = 100
Player_X7.x = 0
Player_X7.y = 200
Player_X8.x = 100
Player_X8.y = 200
Player_X9.x = 200
Player_X9.y = 200
Player_X10.x = 22
Player_X10.y = 70
Player_X11.x = 100
Player_X11.y = 85

#O For Each Square
Player_O1.x = 0
Player_O1.y = 0
Player_O2.x = 100
Player_O2.y = 0
Player_O3.x = 200
Player_O3.y = 0
Player_O4.x = 0
Player_O4.y = 100
Player_O5.x = 100
Player_O5.y = 100
Player_O6.x = 200
Player_O6.y = 100
Player_O7.x = 0
Player_O7.y = 200
Player_O8.x = 100
Player_O8.y = 200
Player_O9.x = 200
Player_O9.y = 200
Player_O10.x = 180
Player_O10.y = 70
Player_O11.x = 100
Player_O11.y = 85

def Draw_TitleBoard(x,y):
    surface.blit(ttlboard.sprite,(x,y))

def Draw_Cancel(x,y):
    surface.blit(cancel_sign.sprite, (x,y))

def Draw_Line(x,y,n):
    if n == 1:
        surface.blit(line1.sprite, (x,y))
        line1.drawn = True
    if n == 2:
        surface.blit(line2.sprite, (x,y))
        line2.drawn = True
    if n == 3:
        surface.blit(line3.sprite, (x,y))
        line3.drawn = True
    if n == 4:
        surface.blit(line4.sprite_up, (x,y))
        line4.drawn = True
    if n == 5:
        surface.blit(line5.sprite_up, (x,y))
        line5.drawn = True
    if n == 6:
        surface.blit(line6.sprite_up, (x,y))
        line6.drawn = True
    if n == 7:
        surface.blit(line7.sprite_D1, (x,y))
        line7.drawn = True
    if n == 8:
        surface.blit(line8.sprite_D2, (x,y))
        line8.drawn = True

def Draw_X(x,y,n):
    if n == 1:
        surface.blit(Player_X1.sprite, (x,y))
        Player_X1.drawn = True
    if n == 2:
        surface.blit(Player_X2.sprite, (x,y))
        Player_X2.drawn = True
    if n == 3:
        surface.blit(Player_X3.sprite, (x,y))
        Player_X3.drawn = True
    if n == 4:
        surface.blit(Player_X4.sprite, (x,y))
        Player_X4.drawn = True
    if n == 5:
        surface.blit(Player_X5.sprite, (x,y))
        Player_X5.drawn = True
    if n == 6:
        surface.blit(Player_X6.sprite, (x,y))
        Player_X6.drawn = True
    if n == 7:
        surface.blit(Player_X7.sprite, (x,y))
        Player_X7.drawn = True
    if n == 8:
        surface.blit(Player_X8.sprite, (x,y))
        Player_X8.drawn = True
    if n == 9:
        surface.blit(Player_X9.sprite, (x,y))
        Player_X9.drawn = True
    if n == 10:
        surface.blit(Player_X10.sprite, (x,y))
        Player_X10.drawn = True
    if n == 11:
        surface.blit(Player_X11.sprite, (x,y))
        Player_X11.drawn = True

def Draw_O(x,y,n):
    if n == 1:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O1.drawn = True
    if n == 2:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O2.drawn = True
    if n == 3:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O3.drawn = True
    if n == 4:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O4.drawn = True
    if n == 5:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O5.drawn = True
    if n == 6:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O6.drawn = True
    if n == 7:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O7.drawn = True
    if n == 8:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O8.drawn = True
    if n == 9:
        surface.blit(Player_O1.sprite, (x,y))
        Player_O9.drawn = True
    if n == 10:
        surface.blit(Player_O10.sprite, (x,y))
        Player_O10.drawn = True
    if n == 11:
        surface.blit(Player_O11.sprite, (x,y))
        Player_O11.drawn = True

def GetBoardState():
    state = [0,0,0,0,0,0,0,0,0]
    if Player_X1.drawn == True:
        state[0] = 1
    if Player_O1.drawn == True:
        state[0] = 2
    if Player_X2.drawn == True:
        state[1] = 1
    if Player_O2.drawn == True:
        state[1] = 2
    if Player_X3.drawn == True:
        state[2] = 1
    if Player_O3.drawn == True:
        state[2] = 2
    if Player_X4.drawn == True:
        state[3] = 1
    if Player_O4.drawn == True:
        state[3] = 2
    if Player_X5.drawn == True:
        state[4] = 1
    if Player_O5.drawn == True:
        state[4] = 2
    if Player_X6.drawn == True:
        state[5] = 1
    if Player_O6.drawn == True:
        state[5] = 2
    if Player_X7.drawn == True:
        state[6] = 1
    if Player_O7.drawn == True:
        state[6] = 2
    if Player_X8.drawn == True:
        state[7] = 1
    if Player_O8.drawn == True:
        state[7] = 2
    if Player_X9.drawn == True:
        state[8] = 1
    if Player_O9.drawn == True:
        state[8] = 2
    return state

def ResetBoard():
    Player_X1.drawn = False
    Player_X2.drawn = False
    Player_X3.drawn = False
    Player_X4.drawn = False
    Player_X5.drawn = False
    Player_X6.drawn = False
    Player_X7.drawn = False
    Player_X8.drawn = False
    Player_X9.drawn = False
    Player_O1.drawn = False
    Player_O2.drawn = False
    Player_O3.drawn = False
    Player_O4.drawn = False
    Player_O5.drawn = False
    Player_O6.drawn = False
    Player_O7.drawn = False
    Player_O8.drawn = False
    Player_O9.drawn = False
    line1.drawn = False
    line2.drawn = False
    line3.drawn = False
    line4.drawn = False
    line5.drawn = False
    line6.drawn = False
    line7.drawn = False
    line8.drawn = False

def TitleScreen():
    text = font.render('Tic Tac Toe', True, White, Black)
    text2 = font2.render('Created By Jacob Hodgkins', True, White, Black)
    text3 = font3.render('Press s To Start!', True, White, Black)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect.center = (150,35)
    textRect2.center = (150,80)
    textRect3.center = (150,250)
    keys = pygame.key.get_pressed()
    while True:
        surface.blit(text, textRect)
        surface.blit(text2, textRect2)
        surface.blit(text3, textRect3)
        Draw_TitleBoard(ttlboard.x,ttlboard.y)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return 1
def WhoStarts():
    surface.fill((0,0,0))
    text4 = font.render('Who Starts?', True, White, Black)
    textRect4 = text4.get_rect()
    textRect4.center = (150,35)
    text5 = font5.render('Press o for O', True, White, Black)
    textRect5 = text5.get_rect()
    textRect5.center = (150,210)
    text6 = font6.render('Press x for X', True, White, Black)
    textRect6 = text6.get_rect()
    textRect6.center = (150,255)
    while True:
        surface.blit(text4, textRect4)
        surface.blit(text5, textRect5)
        surface.blit(text6, textRect6)
        Draw_X(Player_X10.x,Player_X10.y,10)
        Draw_O(Player_O10.x,Player_O10.y,10)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    return 2

def WinnerScreen(p):
    surface.fill((0,0,0))
    text8 = font8.render('Press c To Continue!', True, White, Black)
    text9 = font8.render('Press q to Quit!', True, White, Black)
    textRect8 = text8.get_rect()
    textRect8.center = (150,220)
    textRect9 = text8.get_rect()
    textRect9.center = (170,265)
    if p == 1:
        text7 = font.render('X Is The Winner!', True, White, Black)
    if p == 2:
        text7 = font.render('O Is The Winner!', True, White, Black)
    if p == 3:
        text7 = font.render('Nobody Wins!', True, White, Black)
    textRect7 = text7.get_rect()
    textRect7.center = (150,35)
    while True:
        surface.blit(text7, textRect7)
        surface.blit(text8, textRect8)
        surface.blit(text9, textRect9)
        if p == 1:
            Draw_X(Player_X11.x,Player_X11.y,11)
        if p == 2:
            Draw_O(Player_O11.x,Player_O11.y,11)
        if p == 3:
            Draw_Cancel(cancel_sign.x,cancel_sign.y)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return 1

def drawboard():
    pygame.draw.rect(surface, White, pygame.Rect(0, 0, 100, 100))
    pygame.draw.rect(surface, Black, pygame.Rect(100, 0, 100, 100))
    pygame.draw.rect(surface, White, pygame.Rect(100, 100, 100, 100))
    pygame.draw.rect(surface, Black, pygame.Rect(0, 100, 100, 100))
    pygame.draw.rect(surface, White, pygame.Rect(200, 0, 100, 100))
    pygame.draw.rect(surface, Black, pygame.Rect(200, 100, 100, 100))
    pygame.draw.rect(surface, White, pygame.Rect(200, 200, 100, 100))
    pygame.draw.rect(surface, Black, pygame.Rect(100, 200, 100, 100))
    pygame.draw.rect(surface, White, pygame.Rect(0, 200, 100, 100))
    if Player_X1.drawn:    
        Draw_X(Player_X1.x,Player_X1.y,1)
    if Player_X2.drawn:    
        Draw_X(Player_X2.x,Player_X2.y,2)
    if Player_X3.drawn:    
        Draw_X(Player_X3.x,Player_X3.y,3)
    if Player_X4.drawn:    
        Draw_X(Player_X4.x,Player_X4.y,4)
    if Player_X5.drawn:    
        Draw_X(Player_X5.x,Player_X5.y,5)
    if Player_X6.drawn:    
        Draw_X(Player_X6.x,Player_X6.y,6)
    if Player_X7.drawn:    
        Draw_X(Player_X7.x,Player_X7.y,7)
    if Player_X8.drawn:    
        Draw_X(Player_X8.x,Player_X8.y,8)
    if Player_X9.drawn:    
        Draw_X(Player_X9.x,Player_X9.y,9)
    if Player_O1.drawn:    
        Draw_O(Player_O1.x,Player_O1.y,1)
    if Player_O2.drawn:    
        Draw_O(Player_O2.x,Player_O2.y,2)
    if Player_O3.drawn:    
        Draw_O(Player_O3.x,Player_O3.y,3)
    if Player_O4.drawn:    
        Draw_O(Player_O4.x,Player_O4.y,4)
    if Player_O5.drawn:    
        Draw_O(Player_O5.x,Player_O5.y,5)
    if Player_O6.drawn:    
        Draw_O(Player_O6.x,Player_O6.y,6)
    if Player_O7.drawn:    
        Draw_O(Player_O7.x,Player_O7.y,7)
    if Player_O8.drawn:    
        Draw_O(Player_O8.x,Player_O8.y,8)
    if Player_O9.drawn:    
        Draw_O(Player_O9.x,Player_O9.y,9)
    if line1.drawn:
        Draw_Line(line1.x,line1.y,1)
    if line2.drawn:
        Draw_Line(line2.x,line2.y,2)
    if line3.drawn:
        Draw_Line(line3.x,line3.y,3)
    if line4.drawn:
        Draw_Line(line4.x,line4.y,4)
    if line5.drawn:
        Draw_Line(line5.x,line5.y,5)
    if line6.drawn:
        Draw_Line(line6.x,line6.y,6)
    if line7.drawn:
        Draw_Line(line7.x,line7.y,7)
    if line8.drawn:
        Draw_Line(line8.x,line8.y,8)
    pygame.display.flip()

def CheckForWin():
    BoardState = GetBoardState()
    if BoardState[0] == 1 and BoardState[1] == 1 and BoardState[2] == 1:
        line1.drawn = True
        return 1
    if BoardState[3] == 1 and BoardState[4] == 1 and BoardState[5] == 1:
        line2.drawn = True
        return 1
    if BoardState[6] == 1 and BoardState[7] == 1 and BoardState[8] == 1:
        line3.drawn = True
        return 1
    if BoardState[0] == 1 and BoardState[3] == 1 and BoardState[6] == 1:
        line4.drawn = True
        return 1
    if BoardState[1] == 1 and BoardState[4] == 1 and BoardState[7] == 1:
        line5.drawn = True
        return 1
    if BoardState[2] == 1 and BoardState[5] == 1 and BoardState[8] == 1:
        line6.drawn = True
        return 1
    if BoardState[0] == 1 and BoardState[4] == 1 and BoardState[8] == 1:
        line7.drawn = True
        return 1
    if BoardState[2] == 1 and BoardState[4] == 1 and BoardState[6] == 1:
        line8.drawn = True
        return 1
    if BoardState[0] == 2 and BoardState[1] == 2 and BoardState[2] == 2:
        line1.drawn = True
        return 2
    if BoardState[3] == 2 and BoardState[4] == 2 and BoardState[5] == 2:
        line2.drawn = True
        return 2
    if BoardState[6] == 2 and BoardState[7] == 2 and BoardState[8] == 2:
        line3.drawn = True
        return 2
    if BoardState[0] == 2 and BoardState[3] == 2 and BoardState[6] == 2:
        line4.drawn = True
        return 2
    if BoardState[1] == 2 and BoardState[4] == 2 and BoardState[7] == 2:
        line5.drawn = True
        return 2
    if BoardState[2] == 2 and BoardState[5] == 2 and BoardState[8] == 2:
        line6.drawn = True
        return 2
    if BoardState[0] == 2 and BoardState[4] == 2 and BoardState[8] == 2:
        line7.drawn = True
        return 2
    if BoardState[2] == 2 and BoardState[4] == 2 and BoardState[6] == 2:
        line8.drawn = True
        return 2
    if BoardState[0] != 0 and BoardState[1] != 0 and BoardState[2] != 0 and BoardState[3] != 0 and BoardState[4] != 0 and BoardState[5] != 0 and BoardState[6] != 0 and BoardState[7] != 0 and BoardState[8] != 0:
        return 4
    return 3

def Place(nn,p):
    if nn == "1":
        n = 1
    if nn == "2":
        n = 2
    if nn == "3":
        n = 3
    if nn == "4":
        n = 4
    if nn == "5":
        n = 5
    if nn == "6":
        n = 6
    if nn == "7":
        n = 7
    if nn == "8":
        n = 8
    if nn == "9":
        n = 9
    boardstate = GetBoardState()
    if boardstate[n-1] == 0:
        if p == 1:
            if n == 1:
                    Player_X1.drawn = True
            if n == 2:
                    Player_X2.drawn = True
            if n == 3:
                    Player_X3.drawn = True
            if n == 4:
                    Player_X4.drawn = True
            if n == 5:
                    Player_X5.drawn = True
            if n == 6:
                    Player_X6.drawn = True
            if n == 7:
                    Player_X7.drawn = True
            if n == 8:
                    Player_X8.drawn = True
            if n == 9:
                    Player_X9.drawn = True
            return 1
        if p == 2:
            if n == 1:
                    Player_O1.drawn = True
            if n == 2:
                    Player_O2.drawn = True
            if n == 3:
                    Player_O3.drawn = True
            if n == 4:
                    Player_O4.drawn = True
            if n == 5:
                    Player_O5.drawn = True
            if n == 6:
                    Player_O6.drawn = True
            if n == 7:
                    Player_O7.drawn = True
            if n == 8:
                    Player_O8.drawn = True
            if n == 9:
                    Player_O9.drawn = True
            return 2
    else:
        return 3
        
TitleScreen()
first_player = WhoStarts()
turn = first_player
RUNNING = True
os.system("clear")
while RUNNING:
    drawboard()
    os.system("clear")
    cc = CheckForWin()
    drawboard()
    if cc == 1:
        time.sleep(1)
        WinnerScreen(1)
        ResetBoard()
    elif cc == 2:
        time.sleep(1)
        WinnerScreen(2)
        ResetBoard()
    elif cc == 4:
        time.sleep(1)
        WinnerScreen(3)
        ResetBoard()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                bs = GetBoardState()
                if turn == 1:
                    if 0 <= pos[0] <= 100 and 0 <= pos[1] <= 100:
                        if bs[0] == 0:
                            Player_X1.drawn = True
                            drawboard()
                            turn = 2
                    if 100 <= pos[0] <= 200 and 0 <= pos[1] <= 100:
                        if bs[1] == 0:
                            Player_X2.drawn = True
                            drawboard()
                            turn = 2
                    if 200 <= pos[0] <= 300 and 0 <= pos[1] <= 100:
                        if bs[2] == 0:
                            Player_X3.drawn = True
                            drawboard()
                            turn = 2
                    if 0 <= pos[0] <= 100 and 100 <= pos[1] <= 200:
                        if bs[3] == 0:
                            Player_X4.drawn = True
                            drawboard()
                            turn = 2
                    if 100 <= pos[0] <= 200 and 100 <= pos[1] <= 200:
                        if bs[4] == 0:
                            Player_X5.drawn = True
                            drawboard()
                            turn = 2
                    if 200 <= pos[0] <= 300 and 100 <= pos[1] <= 200:
                        if bs[5] == 0:
                            Player_X6.drawn = True
                            drawboard()
                            turn = 2
                    if 0 <= pos[0] <= 100 and 200 <= pos[1] <= 300:
                        if bs[6] == 0:
                            Player_X7.drawn = True
                            drawboard()
                            turn = 2
                    if 100 <= pos[0] <= 200 and 200 <= pos[1] <= 300:
                        if bs[7] == 0:
                            Player_X8.drawn = True
                            drawboard()
                            turn = 2
                    if 200 <= pos[0] <= 300 and 200 <= pos[1] <= 300:
                        if bs[8] == 0:
                            Player_X9.drawn = True
                            drawboard()
                            turn = 2
                elif turn == 2:
                    if 0 <= pos[0] <= 100 and 0 <= pos[1] <= 100:
                        if bs[0] == 0:
                            Player_O1.drawn = True
                            drawboard()
                            turn = 1
                    if 100 <= pos[0] <= 200 and 0 <= pos[1] <= 100:
                        if bs[1] == 0:
                            Player_O2.drawn = True
                            drawboard()
                            turn = 1
                    if 200 <= pos[0] <= 300 and 0 <= pos[1] <= 100:
                        if bs[2] == 0:
                            Player_O3.drawn = True
                            drawboard()
                            turn = 1
                    if 0 <= pos[0] <= 100 and 100 <= pos[1] <= 200:
                        if bs[3] == 0:
                            Player_O4.drawn = True
                            drawboard()
                            turn = 1
                    if 100 <= pos[0] <= 200 and 100 <= pos[1] <= 200:
                        if bs[4] == 0:
                            Player_O5.drawn = True
                            drawboard()
                            turn = 1
                    if 200 <= pos[0] <= 300 and 100 <= pos[1] <= 200:
                        if bs[5] == 0:
                            Player_O6.drawn = True
                            drawboard()
                            turn = 1
                    if 0 <= pos[0] <= 100 and 200 <= pos[1] <= 300:
                        if bs[6] == 0:
                            Player_O7.drawn = True
                            drawboard()
                            turn = 1
                    if 100 <= pos[0] <= 200 and 200 <= pos[1] <= 300:
                        if bs[7] == 0:
                            Player_O8.drawn = True
                            drawboard()
                            turn = 1
                    if 200 <= pos[0] <= 300 and 200 <= pos[1] <= 300:
                        if bs[8] == 0:
                            Player_O9.drawn = True
                            drawboard()
                            turn = 1

pygame.quit()
