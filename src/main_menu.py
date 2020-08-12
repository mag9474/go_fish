import pygame
import time

displayHeight = 600
displayWidth = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Go Fish')
icon = pygame.image.load('resources\cartoon-2027752_640.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

bg = pygame.image.load(r"resources\Title_BG.png")

def text_objects(text,font):
    textSurface = font.render(text,True, (0,0,0))
    return textSurface, textSurface.get_rect()


def button(text,x,y,w,h,icolor,acolor,action=None): 
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, acolor,(x,y,w,h))
        if click[0] == 1 and action != None:
            return action
    else:
        pygame.draw.rect(gameDisplay, icolor,(x,y,w,h))
    
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf,TextRect)



def main_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        gameDisplay.blit(bg, (0, 0))
        #gameDisplay.fill((255,255,255))
        #message_display('Go Fish!',115,displayWidth,displayHeight)
        
        play_button = button("Play!",150,450,100,50,(0,200,0),(0,255,0),"Play")
        quit_button = button("Quit",550,450,100,50,(255,0,0),(200,0,0),"Quit")
        if quit_button == "Quit":
            pygame.quit()
        pygame.display.update()
        clock.tick(15)
        return play_button
        
                

def main():
    main_menu()
    pass

if __name__ == '__main__':
    main()



