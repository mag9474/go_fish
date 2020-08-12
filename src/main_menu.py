import pygame
import time

#sets the game display window (see game_logic for more info)
displayHeight = 600
displayWidth = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Go Fish')
icon = pygame.image.load('resources\cartoon-2027752_640.png')
pygame.display.set_icon(icon)

#for setting fps
clock = pygame.time.Clock()

#loads in the background of the main menu
bg = pygame.image.load(r"resources\Title_BG.png")

#this function returns infomation about color and spatial features of text
def text_objects(text,font):
    textSurface = font.render(text,True, (0,0,0))
    return textSurface, textSurface.get_rect()

#this funtion is made so that buttons can be used in the game 
def button(text,x,y,w,h,icolor,acolor,action=None): 
    mouse = pygame.mouse.get_pos() #pygame returns coodinates of mouse position
    click = pygame.mouse.get_pressed() #returns status of mouse button press

    if x + w > mouse[0] > x and y+h > mouse[1] > y: #if the mouse is within the coordinates of the button, then the buttin will change colors
        pygame.draw.rect(gameDisplay, acolor,(x,y,w,h))
        if click[0] == 1 and action != None: #if click wihtin the button area then will return the action set above 
            return action
    else:
        pygame.draw.rect(gameDisplay, icolor,(x,y,w,h)) #otherwise the buttin is on standard color
    
    smallText = pygame.font.Font('freesansbold.ttf', 20) #this is the text and location of the button
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf,TextRect)



def main_menu(): #this is the main menu loop
    intro = True
    while intro:
        for event in pygame.event.get(): #allows users to close game
            if event.type == pygame.QUIT:
                quit()
        
        gameDisplay.blit(bg, (0, 0)) #adds backgorund image to display        
        play_button = button("Play!",150,450,100,50,(0,200,0),(0,255,0),"Play") #adds play button
        quit_button = button("Quit",550,450,100,50,(255,0,0),(200,0,0),"Quit") #adds quit button
        if quit_button == "Quit": #if press quit game ends
            pygame.quit()
        pygame.display.update() #updates the display
        clock.tick(15) #fps 15
        return play_button #returns play if the play buttin is clicked
        
                

def main():
    pass

if __name__ == '__main__':
    main()



