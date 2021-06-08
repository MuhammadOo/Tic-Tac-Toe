import pygame
import sys
import numpy as np
pygame.init()

width=600
height=width
white= (255,255,255)
red=(255,0,0)
row=3
column=3
circle_radius=80
space=35
#BG_COLOR=(28,170,156)
background_image=pygame.image.load("C:\\Users\\ChefAbi\\Desktop\\291c8a1a7afc5666fc7ae76737a993da.jpg")
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Mehemmedin oyunu")
#window.fill(BG_COLOR)
board=np.zeros((row,column))

def draw_lines():
    pygame.draw.line(window, white, (10, 200), (590, 200), 5)
    pygame.draw.line(window, white, (10, 400), (590, 400), 5)
    pygame.draw.line(window, white, (200, 10), (200, 590), 5)
    pygame.draw.line(window, white, (400, 10), (400, 590), 5)
def draw_figures():
    for x in range(row):
        for y in range(column):
            if board[x][y]==1:
                pygame.draw.circle(window,white,(int(y*200+100),(x*200+100)),circle_radius,15)
            elif board[x][y]==2:
                pygame.draw.line(window,white,(y*200+space,x*200+space),(y*200+200-space,x*200+200-space),25)
                pygame.draw.line(window, white, (y * 200 + 200-space, x * 200 + space),
                                 (y * 200 + space, x * 200 +200- space), 25)
def mark_square(row,column,player):
    board[row][column]=player

def availabe_square(row,column):
    if board[row][column]==0:
        return True
    else:
        return False
def check_fullboard():
    for x in range(row):
        for y in range(column):
            if board[x][y]==0:
                return False
    return True

def check_win(player):
    #vertical win check
    for y in range(column):
        if board[0][y]==player and board[1][y]==player and board[2][y]==player:
            vertical_winning_line(y,player)
            return True
    #horizontal win check
    for x in range(row):
        if board[x][0]==player and board[x][1]==player and board[x][2]==player:
            horizontal_winning_line(x,player)
            return True
    #left diagonal check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        desc_diagonal_winning_line(player)
        return True
    #right diagonal check
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        asc_diagonal_winning_line(player)
        return True

    return False

def vertical_winning_line(y,player):

    posX=y*200+100
    if player==1:
        color=white
    elif player==2:
        color=red

    pygame.draw.line(window,color,(posX,35),(posX,height-space),15)

def horizontal_winning_line(x,player):

    posY=x*200+100
    if player==1:
        color=white
    elif player==2:
        color=red
    pygame.draw.line(window,color,(35,posY),(600-space,posY),15)


def asc_diagonal_winning_line(player):

    if player==1:
        color=white
    elif player==2:
        color=red
    pygame.draw.line(window,color,(space,600-space),(600-space,space),15)

def desc_diagonal_winning_line(player):
    if player == 1:
        color = white
    elif player == 2:
        color = red
    pygame.draw.line(window, color, (space, space), (600 - space, 600 - space), 15)

def play_again():
    window.blit(background_image, [0, 0])
    draw_lines()
    player=1
    for x in range(row):
        for y in range(column):
            board[x][y]=0


#draw_lines()
player=1
gameover=False
window.blit(background_image, [0, 0])
while True:
    #window.blit(background_image, [0, 0])
    #draw_figures()
    #draw_lines()

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
        if i.type==pygame.MOUSEBUTTONDOWN and not gameover:
            mouseX=i.pos[0] #0 for x cordinate
            mouseY=i.pos[1] #1 for y cordinate
            clicked_row=int(mouseY//200)
            clicked_column = int(mouseX // 200)

            if availabe_square(clicked_row,clicked_column)==True:
                if player==1:
                    mark_square(clicked_row,clicked_column,player)
                    if check_win(player)==True:
                        gameover=True
                    player=2
                elif player==2:
                    mark_square(clicked_row,clicked_column,player)
                    if check_win(player)==True:
                        gameover=True
                    player=1

                #draw_figures()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_r:
                play_again()
                player=1
                gameover=False

    #draw_figures()
    draw_lines()
    draw_figures()


    pygame.display.update()
