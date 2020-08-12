import pygame
import time

displayHeight = 600
displayWidth = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Go Fish')
icon = pygame.image.load('resources\cartoon-2027752_640.png')
pygame.display.set_icon(icon)


textbubble = pygame.image.load(r'resources\textbox.png')


def game_score(player, score,x,y):
    font = pygame.font.SysFont(None, 25)
    text = font.render(str(player) +": " + str(score),True,(255,255,0))
    gameDisplay.blit(text,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True, (0,0,0))
    return textSurface, textSurface.get_rect()

def comp_speak(text,player):
    if player == 'player2':
        x = 600
        y = 100
        textbub = pygame.transform.scale(textbubble, (200, 150))
        font = pygame.font.Font('freesansbold.ttf',(26-(len(text)//2)))
        TextSurf, TextRect = text_objects(text, font)
        TextRect.center = (x,y)
        gameDisplay.blit(textbub,((x-100),(y-75)))
        gameDisplay.blit(TextSurf,TextRect)
    if player == 'player1':
        x=600
        y = 500
        textbub = pygame.transform.scale(textbubble, (200, 150))
        textbub = pygame.transform.flip(textbub,False,True)
        font = pygame.font.Font('freesansbold.ttf',(26-(len(text)//2)))
        TextSurf, TextRect = text_objects(text, font)
        TextRect.center = (x,y)
        gameDisplay.blit(textbub,((x-100),(y-75)))
        gameDisplay.blit(TextSurf,TextRect)
    



def message_display(text,size,width,height):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    gameDisplay.blit(TextSurf,TextRect)


def game_over(text):
    x = 400
    y = 300
    font = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf,TextRect)

def main():
    pass

if __name__ == '__main__':
    main()