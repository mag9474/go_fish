import pygame

#sets the game display window (see game_logic for more info)
displayHeight = 600
displayWidth = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Go Fish')
icon = pygame.image.load('resources\cartoon-2027752_640.png')
pygame.display.set_icon(icon)

#Timer that is later used to set fps
clock = pygame.time.Clock()

#this defines the card images' dimensions
w=50
h=75

#this function works very similarly to the button function in 'main_menu' but instead it resizes and adds outline to cards when mouse is over them
#see main_menu\button for more details
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
    cards = {} #empty dictonary that will later be used to store cards and their images
    suit = ['d','h','c','s']
    for i in range(13):
        for y in range(4):
            card_name = str((i+2))+suit[y] #this uses the loop variables to name the card, for example if i+2=14 and y 4, then it returns 14s which coressponds to the file for ace of spades
            cardimage = pygame.image.load(r"resources\Cards\{}.png".format(card_name)) #loads the card image
            cardimage = pygame.transform.scale(cardimage, (50, 75)) #resizes to fit the game
            card_name = card_name.upper() #the following logic translates the 'cardname' into the format used in the game. the game uses numbers and letters so that only the first character is needed to define the card (k=king instead of 13=king)
            card_suit = card_name[len(card_name)-1]
            card_name = card_name.replace(card_suit,'')
            card_name = card_name + '_' + card_suit
            card_name = card_name.replace('11','J')
            card_name = card_name.replace('12','Q')
            card_name = card_name.replace('13','K')
            card_name = card_name.replace('14','A')
            cards.update({card_name:cardimage}) #adds the card name and image so that it can easily be called during the game
    cardimage = pygame.image.load(r"resources\Cards\gray_back.png") #also loads the back of a card
    cardimage = pygame.transform.scale(cardimage, (50, 75)) #resizes the back of the card
    cards.update({'card_back':cardimage}) #adds to library
    return cards

def card_visual(playercards,cards,turn=False): #this is how the game knows how to display the cards in a players hand
    select = None
    for i in range(len(playercards)): # this limits the number of cards in the player's hands to being only 14 in the first row
        if len(playercards) < 14: #if the players total cards is less than 14, then the number of cards is used for calculating display locations
            cardnumber = len(playercards)
        else: 
            cardnumber = 14 #if the total cards 14 plus then 14 is used for calucalting the display of the first row
            secondlvl = len(playercards) - 14
        if i < 14:
            x = (displayWidth/2)+(i*55)-(cardnumber*0.5*55) #this returns the cards x location for each card in the loop (for first layer). dynamically resizes based on total cards in hand
            y = 380 #stagnat y coordinate
            if cardisplay(cards[playercards[i]],x,y,w,h,playercards[i],turn) != None:
                select = cardisplay(cards[playercards[i]],x,y,w,h,playercards[i],turn) #runs the animation for selecting a card if turn is True, else just display
        else:
            x = (displayWidth/2)+((i-15)*55)-(secondlvl*0.5*55) #same as above for second level
            y = 460
            if cardisplay(cards[playercards[i]],x,y,w,h,playercards[i],turn) != None: 
                select = cardisplay(cards[playercards[i]],x,y,w,h,playercards[i],turn)
    return select

def comp_visual(compcards,cards): #simlair to card_visual but for the computer. only shows the back and only needs one layer because cards are not spread apart enough to warrant it 
        for i in range(len(compcards)):
            x = (displayWidth/2)+(i*20)-(len(compcards)*0.5*20)
            y = 75
            gameDisplay.blit(cards['card_back'],(x,y))



def main():
    pass

if __name__ == '__main__':
    main()