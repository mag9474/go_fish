import pygame
import time

#sets the game display window (see game_logic for more info)
displayHeight = 600
displayWidth = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Go Fish')
icon = pygame.image.load('resources\cartoon-2027752_640.png')
pygame.display.set_icon(icon)

#loads the image representing speech bubble
textbubble = pygame.image.load(r'resources\textbox.png')

#sets the font, size, and content of the text used for the game score
def game_score(player, score,x,y):
    font = pygame.font.SysFont(None, 25)
    text = font.render(str(player) +": " + str(score),True,(255,255,0))
    gameDisplay.blit(text,(x,y))

#returns the color and spatial coordinates of text
def text_objects(text,font):
    textSurface = font.render(text,True, (0,0,0))
    return textSurface, textSurface.get_rect()

#this is how the text is diplayed for asking for cards and saying go fish
def comp_speak(text,player):
    if player == 'player2': #this sets the text location based on which player is speaking
        x = 600
        y = 100
    if player == 'player1':
        x=600
        y = 500
    textbub = pygame.transform.scale(textbubble, (200, 150)) #resizes the speech bubble to fit game
    if player =='player1':
        textbub = pygame.transform.flip(textbub,False,True) #if it is player one talking the bubble needs to be flipped
    font = pygame.font.Font('freesansbold.ttf',(26-(len(text)//2))) #sets the font and size of the text. the logic dynamically resizes the text si that it always fits inside the bubble
    TextSurf, TextRect = text_objects(text, font) #returns the spatial coordinates of text
    TextRect.center = (x,y) #tells where to center the text
    gameDisplay.blit(textbub,((x-100),(y-75))) #this sets the location for the text bubble and then tells it to load to the display
    gameDisplay.blit(TextSurf,TextRect) #loads text to the display ion top of bubble
    
#this is the function that displays the text at the end of the game. nothing notably different than any other text function
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