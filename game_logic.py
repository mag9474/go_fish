import pygame
import time
import src.main_menu as main
import src.loadcards as loadcards
import random
import src.score_text as score

######################### (1) Pygame data

#initializes pygame
pygame.init()

#creating screen and the width/height
displayHeight = 600
displayWidth = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

#adding a caption and image to the window
pygame.display.set_caption('Go Fish')
icon = pygame.image.load('resources\cartoon-2027752_640.png')
pygame.display.set_icon(icon)

#This is the image used for the background during the main gaem loop
bg = pygame.image.load(r"resources\bg.png")

# This function essentially tgells pygame what should always be shown during the game loop
def game_disp():
    displayHeight = 600 #display height
    displayWidth = 800 #display width
    gameDisplay = pygame.display.set_mode((displayWidth,displayHeight)) #sets and stores the display 
    pygame.display.set_caption('Go Fish') #the widow caption
    icon = pygame.image.load('resources\cartoon-2027752_640.png') #window icon
    pygame.display.set_icon(icon) #actaully loads the icon into the display
    gameDisplay.blit(bg, (0, 0)) #adds the background to the game window
    score.game_score('Player', score1,0,0) #uses a function to add the players score to the game
    score.game_score('Computer', score2,675,0) #adds computer's score to the game
    loadcards.comp_visual(player2,image_cards) #adds the computers cards to the game
    loadcards.card_visual(player1,image_cards,False) #adds players cards to the game
    if len(deck) > 0:
        gameDisplay.blit(image_cards['card_back'],(90,250)) #adds a card to the screen that represents the deck
    if score1 > 0: #if the player has scored it will add a card to represent the pile of 'scored cards'
        gameDisplay.blit(image_cards['card_back'],(710,270))
    if score2 > 0: #same as two lines above for computer
        gameDisplay.blit(image_cards['card_back'],(710,180))
    for event in pygame.event.get(): #this allows the game window to be closed using the 'x' at the top of the window
        if event.type == pygame.QUIT:
            running = quit()


#Timer that is later used to set fps
clock = pygame.time.Clock()

#Function defined in loadcards that loads all card images
image_cards = loadcards.loadallcards()

#loads the sounds used in the game
card_sound = pygame.mixer.Sound('resources\card_sound.wav')
deck_sound = pygame.mixer.Sound('resources\deck_sound.wav')
score_sound = pygame.mixer.Sound('resources\score_sound.wav')

#I wanted to put this function in another module, but could not get it to work outside of the main.
#this function is how the cards are animated moving throughout the game
def card_animation(y_start, y_end, x_start,x_end,text_option=None,card_type=None,player_num=None):
    animate = True
    pygame.mixer.Sound.play(card_sound) #plays the card sound
    if x_start == x_end: #if the starting x position and edning position are the same then the x speed will be 0
        x_speed = 0
    else:
        x_speed = 10 * ((x_start-x_end)/abs(x_start-x_end)) #if the start and end positions are not the same, then it will set the spped to 10 and the following logic will tell it whther it is positive or negative movement
    if y_start == y_end: #see above for x
        y_speed = 0
    else:
        y_speed = 10 * ((y_start-y_end)/abs(y_start-y_end)) 
    while animate: #this is the animation loop
        game_disp() #resets the gamedisplay at the start of each loop
        if text_option == 1: #if specified by the function this will make it display what card is being given and by who
            score.comp_speak(('I will give you my '+ card_type + 's!'),player_num)
        if text_option == 2: #if specified by the function this will make it display a player saying go fish during the animatino
            score.comp_speak('Go Fish!',player_num)
        gameDisplay.blit(image_cards['card_back'],(x_start,y_start)) #adds the card image to the screen
        y_start -= y_speed #changes the coordinates for the card to display on the next cycle of tyhe loop
        x_start -= x_speed
        if y_start == y_end: #if the y coordinates reach the end, the y speed is set to zero so it does not continue
            y_speed = 0
        if x_start == x_end: #see above for y
            x_speed = 0
        if y_start == y_end and x_start == x_end: #if both x and y coordinates have made it to the end position, then the loop ends
            animate = False
        pygame.display.update() #updates the display
        clock.tick(60) #sets fps to 60


######################### End of (1)



######################### (2) Game Definitions 

# dealing function. You can pass it a number, and it returns a list of cards(in string)
# I used the random.randint function, which gives a random int in the defined range
# e.g if the initial handsize is 7, you'd call deal(7), each time a player draw a card, it'd be deal(1)
# the function also auto remove the dealt cards from the pool

def deal(number):
    global deck
    cards = []
    for i in range(number):
        card_ind = random.randint(0,len(deck)-1) #this function also includes the last number (unlike most range functions)
        card = deck[card_ind]
        cards.append(card)
        deck.remove(card)
    return cards

### Variant of deal that only deals 1 card, adds it to the players cards, and returns that value
###

# the simple asking for a card function, doens't require any momory or thinking
# if randomly identify a card in hand and ask for one of the available kinds
# input is a player card list (player1 or player2), return is the kind in str format e.g 'A','2'

def simple_ask(player):
    card_ind = random.randint(0,len(player)-1)
    #print(card_ind)
    cardname = player[card_ind]
    #print(cardname)
    if cardname[0] in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        score.comp_speak(('Do you have any ' + cardname[0] + "s?"),"player2") #this function displays the what card is being asked, becasue this loop is only run by the computer is is specified as 'player2'
        pygame.display.update() #updates the display 
        clock.tick(60) #fps 60
        time.sleep(1) #pauses for 1 second for users to read the computer's question
        return cardname[0]
    elif cardname[0] == '1':
        score.comp_speak(('Do you have any ' + cardname[0:2] + "s?"),"player2") #this functions the same as above
        pygame.display.update()
        clock.tick(60)
        time.sleep(1)
        return cardname[0:2]

# slightly more advanced, remembers what it just asked and doesn't repeat
# can consi

#def mindful_ask(player, player_asks):
#    while 

#    return cardname

def human_ask(): #not used in the visulaized mode.
    ask = input("Do you have any XXXXs? (Ask for a card type): ")
    cardname = ask[0].upper()
    return cardname

# function of a player after being asked
# input is the requested kind or name, and player card list (player1 or player2)
# return is a tuple (new player card list, transfered cards list)

def beingasked(kind,player,player_num):
    give = []
    global turn
    if len(kind) > 2: #this ifelse returns the players cards as just the card type (computer is already done through simple ask)
        if kind[:1] == '10': #ten is done on its own because it is the only 2 character number
            card_type = 10
        else: 
            card_type = kind[0] #all other can be classified as by the first digit
    else:
        card_type = kind #for the cards already changed by simple ask, will be passed through
    card_type = what_kind[card_type] #this changes card type into the full word version - ie Q to queen

    for i in range(len(player)): #select cards to give
        if player[i][0] == kind[0]:
            give.append(player[i])
    
    for i in give: # remove cards that are given
        player.remove(i)

    
    if len(give) == 0:  # say 'go fish' if there's no available cards
        print('Go fish')
        if player_num == 'player1': #this sets the starting and ending coordinates for the subsequent card animation for the player
            y_start = 250
            y_end = 80
            x_start = 90
            x_end =400
        else: #this sets the coordinations for the computer
            y_start = 250
            y_end = 380
            x_start = 90
            x_end =400
        give = deal(1) 
        card_animation(y_start, y_end, x_start, x_end,2,player_num=player_num) #runs the animation
        print('fished',give)
        turn = False
    else:       # display transfered cards if there are cards to give
        if player_num == 'player1': #this is the animation for when a card is given from player to computer or visa versa. similar to the above
            y_start = 380
            y_end = 70
        else:
            y_start = 70
            y_end = 380
        card_animation(y_start, y_end, (displayWidth/2), (displayWidth/2),1,card_type,player_num)
        print('I will give you', give)
    return (player, give)

# function of a player after getting cards either from another player or the deck
# input is the cards they got (list ["A_H, 10_D"]), and player original card list (player1,player2)
# output is a tuple of the new player card list (include the senario where they get a point), and the score they get from this round (0 or 1)

def getcards(cards,player,player_score,player_num):
 #   score = 0
    player += cards     # put the new cards in the list
    thistype = []       # record cards that are of the same kind as the new card(s)
    for i in player:    # put card(s) of the same kind as the new card(s) in this list
        if i[0] == cards[0][0]:
            thistype.append(i)
    if len(thistype) == 4: # see if you have 4 cards of this kind and get a point
        for i in thistype: # if so remove these 4 cards and score = 1
            player.remove(i)
        if player_num == 'player1': #this plays tyhe animation for scoring cards to move to the 'scored cards pile'
            y_start = 380
            y_end = 270
            x_start = 400
            x_end = 710
        else:
            y_start = 80
            y_end = 180
            x_start = 400
            x_end = 710
        pygame.mixer.Sound.play(score_sound) #plays the score sound
        card_animation(y_start, y_end, x_start, x_end) #runs the animation using the specifications above
        player_score += 1
    return (player, player_score)

# see if the game ends (no cards in the pool, no cards in either player's hand)
# no input, output True (end) or False (not end)

def ifend():
    global deck
    global player1
    global player2
    if deck == [] or player1 == [] or player2 == []:
        return True
    else:
        return False

# call the results

def result():
    global score1
    global score2
    if score1 > score2:
        #print('player1 you won!')
        score.game_over("You WON!!!") #uses function that displays messages to the screen
    elif score1 == score2:
        #print('it is a tie!')
        score.game_over("Its a Tie!")
    else:
        #print('player2 you won!')
        score.game_over("You LOST")

######################## End of (2)

######################## (3) Predefined game variables

# define the initial pool as a list
deck_backup = ['A_C','A_S','A_D','A_H', #made to define the game deck and redefine it if the player wantes to play again
        '2_C','2_S','2_D','2_H',
        '3_C','3_S','3_D','3_H',
        '4_C','4_S','4_D','4_H',
        '5_C','5_S','5_D','5_H',
        '6_C','6_S','6_D','6_H',
        '7_C','7_S','7_D','7_H',
        '8_C','8_S','8_D','8_H',
        '9_C','9_S','9_D','9_H',
        '10_C','10_S','10_D','10_H',
        'J_C','J_S','J_D','J_H',
        'Q_C','Q_S','Q_D','Q_H',
        'K_C','K_S','K_D','K_H']

deck = deck_backup.copy() #copies the backup deck into the game deck

#Type to number/name. this is used to translate the card types into words for the display. 10 and 1 are both ten because I was having a 
# glitch where the computer was asking for ones (which obviously dont exist) but still ran the code for tens so I just made both translate into 10 which works
what_kind = {'1':'ten','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven',
'8':'eight','9':'nine','10':'ten','J':'jack','Q':'queen','K':'king','A':'ace'}

# store player1 and player2's card in separate lists
player1 =[]
player2 =[]

# record each player's score
score1 = 0
score2 = 0

# not sure if we need it, but it stores cards that are being transfered
cardtransfer = []

# starting_hand = int(input("How many card to start with? "))
starting_hand = 5

# global for a turn
turn = True

#variable for the game loop
end = False

#sets the player and computer's hands
player1 = deal(starting_hand)
print('player1 got,', player1)
player2 = deal(starting_hand)
print('player2 got,', player2)

#turn variables
player1_turn_over = False
player2_turn_over = True

# For starting the pygame start screen and overall game
running = True
intro = True


######################## End of (3)



######################## (4) Main Loop
# Things to do
# merge ifend and result
# need to program some of the AI's
# Need to have a way to get the AI's to play against each other

### Implement Settings/AI/ETC

#print(player2)
#print(deck)
#print(deck_backup)

#this is the main game loop
while running:
    for event in pygame.event.get(): #these three lines allow the 'x' in top  of the sindow to funtion
        if event.type == pygame.QUIT:
            running = False
    while intro: #this runs the intro screen (loop defined in 'main_menu' module)
        menu = main.main_menu()
        if menu == "Play": #if the play button within the main menu returns play then into loop ends and game begins
            intro = False
            pygame.mixer.Sound.play(deck_sound) #deck shuffle sound
    
    while end == False: #this is the actual game loop
        game_disp() #loads all the basic game display images (see definition above)
        while player1_turn_over == False:
            game_disp() #loads game display within the player turn loop
            end = ifend() # added this because game kept crashing at player 2's turn, so added this to be safe
            if end == True:
                break
            #ask = simple_ask(player1) #this if for running AI vs AI
            #ask = human_ask() #this will alow user to play through console
            ask = None #sets ask to none for the loop below
            while ask == None:
                game_disp() #loads game display during the player asking loop
                #score.game_score('1', score1,0,0)
                ask = loadcards.card_visual(player1,image_cards,True) #runs finction that allows player to select card with mouse. Also adds visuals to card when mouse is hovering over it
                pygame.display.update() #updates the display so that the card visuals can be seen
                clock.tick(60) #sets fps
            print('player1 asked', ask) 
            print('player2 said:')
            player2, cards = beingasked(ask, player2,'player2') #based on player selection runs animation for go fish or card transfer and handles the game logic (also sets turn to false if go fish)
            player1, score1 = getcards(cards,player1,score1,'player1') #handles the game logic of if player has 4 cards and runs the animiation if so
            print('player1 now has:',player1,'score=',score1)
            end = ifend()
            pygame.display.update() #updates the display
            clock.tick(60) #fps at 60
            if turn == False: #logic for changin turns
                player2_turn_over = False
                player1_turn_over = True
                turn = True

        if end == True:
            break
        
        while player2_turn_over == False: #this is essentially the same loop as above except for the computer. Only difference is the simple ask istead of the human ask
            game_disp()
            end = ifend() # added this because game kept crashing due to 0 cards here
            if end == True:
                break
            ask = simple_ask(player2)
            print('player2 asked', ask)
            print('player1 said:')
            player1, cards = beingasked(ask, player1,'player1')
            player2, score2 = getcards(cards,player2,score2,'player2')
            print('player2 now has:',player2,'score=',score2)
            end = ifend()
            pygame.display.update()
            clock.tick(60)
            if turn == False:
                player1_turn_over = False
                player2_turn_over = True
                turn = True   
        pygame.display.update()
        clock.tick(60) 
    game_disp()
    result() #when the game ends this runs to declare a winner or tie
    play_again_button = main.button("Again?",150,450,100,50,(0,200,0),(0,255,0),"Play") #button to play again
    quit_game_button = main.button("Quit",550,450,100,50,(255,0,0),(200,0,0),"Quit") #button to quit
    if play_again_button == 'Play': #if play again this resets everything back to tyhe initgial game settings.
        player1 = []
        player2 = []
        score1 = 0
        score2 = 0
        deck = deck_backup
        player1 = deal(starting_hand)
        player2 = deal(starting_hand)
        end = False
    if quit_game_button == "Quit": #if player quits it ends the game
        pygame.quit()
    pygame.display.update() #updates the display during the results display
    clock.tick(60) #sets the fps
pygame.quit()
quit()