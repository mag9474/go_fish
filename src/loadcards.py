import pygame


displayHeight = 600
displayWidth = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Go Fish')
icon = pygame.image.load('resources\cartoon-2027752_640.png')
pygame.display.set_icon(icon)

#Timer that is later used to set fps
clock = pygame.time.Clock()

w=50
h=75

def cardisplay(image,x,y,w,h,card_name,turn=False): 
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y and turn == True:
        image2 = pygame.transform.scale(image,(60, 85))
        gameDisplay.blit(image2,(x-5,y-5))
        pygame.draw.rect(gameDisplay, (0, 100, 255), (x-5, y-5, 60, 85), 3)
        if click[0] == 1:
            return card_name
    else:
        gameDisplay.blit(image,(x,y))
    
# Loads all cards to images using a for loop to get file names, 
# then converts card name into the format used in the game logic so that images can be called later.
def loadallcards():
    cards = {}
    suit = ['d','h','c','s']
    for i in range(13):
        for y in range(4):
            card_name = str((i+2))+suit[y]
            cardimage = pygame.image.load(r"resources\Cards\{}.png".format(card_name))
            cardimage = pygame.transform.scale(cardimage, (50, 75))
            card_name = card_name.upper()
            card_suit = card_name[len(card_name)-1]
            card_name = card_name.replace(card_suit,'')
            card_name = card_name + '_' + card_suit
            card_name = card_name.replace('11','J')
            card_name = card_name.replace('12','Q')
            card_name = card_name.replace('13','K')
            card_name = card_name.replace('14','A')
            cards.update({card_name:cardimage})
    cardimage = pygame.image.load(r"resources\Cards\gray_back.png")
    cardimage = pygame.transform.scale(cardimage, (50, 75))
    cards.update({'card_back':cardimage})
    print(cards)
    return cards

def card_visual(playercards,cards,turn=False):
    select = None
    for i in range(len(playercards)):
        if len(playercards) < 14:
            cardnumber = len(playercards)
        else: 
            cardnumber = 14
            secondlvl = len(playercards) - 14
        if i < 14:
            x = (displayWidth/2)+(i*55)-(cardnumber*0.5*55)
            y = 380
            if cardisplay(cards[playercards[i]],x,y,w,h,playercards[i],turn) != None:
                select = cardisplay(cards[playercards[i]],x,y,w,h,playercards[i],turn)
        else:
            x = (displayWidth/2)+((i-15)*55)-(secondlvl*0.5*55)
            y = 460
            if cardisplay(cards[playercards[i]],x,y,w,h,playercards[i],turn) != None:
                select = cardisplay(cards[playercards[i]],x,y,w,h,playercards[i],turn)
    return select

def comp_visual(compcards,cards):
        for i in range(len(compcards)):
            x = (displayWidth/2)+(i*20)-(len(compcards)*0.5*20)
            y = 75
            gameDisplay.blit(cards['card_back'],(x,y))


def give_card(player_num, cards,ystart,yend,x):
    ystart -= 5
    gameDisplay.blit(cards['card_back'],(x,ystart))
    if ystart == yend:
        return False
    return




def main():
    loadallcards()

if __name__ == '__main__':
    main()