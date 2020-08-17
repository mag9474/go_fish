import random
from collections import Counter
# define the initial pool as a list
deck_backup = ['A_C','A_S','A_D','A_H',
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

deck = deck_backup.copy()

# store player1 and player2's card in separate lists
player1 =[]
player2 =[]

# record each player's score
score1 = 0
score2 = 0

player1wins = 0
player2wins = 0
ties = 0
player1_asks = ["x"]
player2_asks = ["x"]
# global for a turn
turn = True
end = False

def reset_game():
  global deck 
  global player1
  global player2
  global score1
  global score2
  global turn
  global end 
  global player1_asks
  global player2_asks
  
  deck = deck_backup.copy()
  player1 = []
  player2 = []
  score1 = 0
  score2 = 0
  turn = True
  end = False
  player1_asks = ["x"]
  player2_asks = ["x"]

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






# the simple asking for a card function, doens't require any momory or thinking
# if randomly identify a card in hand and ask for one of the available kinds
# input is a player card list (player1 or player2), return is the kind in str format e.g 'A','2'

def simple_ask(player):
#    card_ind = random.randint(0,len(player)-1)
#    print(card_ind)
    cardname = random.choice(player)
    #print(cardname)
    if cardname[0] in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        return cardname[0]
    elif cardname[0] == '1':
        return cardname[0:2]

# slightly more advanced AI, gets 3 tries to pick a random card type it didn't play, if not just picks the next random card (a workaround in case you had 3 cards of the same type as otherwise the while loop would continue forever)

def mindful_ask(player, player_asks): 
  tries = 0
  if len(player) < 2:
    cardname = random.choice(player)
    return cardname[0]
  else:
    card_found = False
    while card_found == False:
      cardname = random.choice(player)
      tries += 1
      if cardname[0] != player_ask[-1][0]:
        card_found = True 
      elif tries > 3:
        card_found = True                            

    return cardname[0]

# uses the Counter function to figure out what is the most common card type in the hand then asks for it

def most_ask(player):
    card_type = []
    for i in range(0,len(player)):
      card_type.append(player[i][0])
    most_cards = [word for word, word_count in Counter(card_type).most_common(1)]
    return most_cards[0]
# uses the counter function again but picks the least common card type and asks for it
def least_ask(player):
    card_type = []
    for i in range(0,len(player)):
      card_type.append(player[i][0])
    least_cards = [word for word, word_count in Counter(card_type).most_common()]
    cardname = random.choice(least_cards[-1])
    return cardname[0]
# gets 5 tries to match one of the opponents card asks to something in your hand 
def revenge_ask(player,opposite_player_asks):
    tries = 0
    card_found = False
    while card_found == False:
      card_ind = random.randint(1,len(opposite_player_asks))
      cardname = random.choice(player)
      tries += 1
      if cardname[0] == opposite_player_asks[card_ind*-1][0]:
        card_found = True 
      elif tries > 5:
        card_found = True                            

    return cardname[0]    
    


def human_ask():
    ask = input("Do you have any XXXXs? (Ask for a card type): ")
    cardname = ask[0].upper()
    return cardname

# function of a player after being asked
# input is the requested kind or name, and player card list (player1 or player2)
# return is a tuple (new player card list, transfered cards list)

def beingasked(kind,player):
    give = []
    global turn
    for i in range(len(player)): #select cards to give
        if player[i][0] == kind[0]:
            give.append(player[i])

    for i in give: # remove cards that are given
        player.remove(i)

    if len(give) == 0:  # say 'go fish' if there's no available cards
        #print('Go fish')
        give = deal(1)
        turn = False
    else:               # display transfered cards if there are cards to give
        #print('transfer', give)
        test = 1
    return (player, give)

# function of a player after getting cards either from another player or the deck
# input is the cards they got (list ["A_H, 10_D"]), and player original card list (player1,player2)
# output is a tuple of the new player card list (include the senario where they get a point), and the score they get from this round (0 or 1)

def getcards(cards,player,player_score):
 #   score = 0
    player += cards     # put the new cards in the list
    thistype = []       # record cards that are of the same kind as the new card(s)
    for i in player:    # put card(s) of the same kind as the new card(s) in this list
        if i[0] == cards[0][0]:
            thistype.append(i)
    if len(thistype) == 4: # see if you have 4 cards of this kind and get a point
        for i in thistype: # if so remove these 4 cards and score = 1
            player.remove(i)
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
    global player1wins
    global player2wins
    global ties
    if score1 > score2:
 #       print('player1 you won!')
        player1wins += 1
    elif score1 == score2:
#        print('it is a tie!')
        ties += 1
    else:
  #      print('player2 you won!')
        player2wins += 1



###### Main Loop


# starting_hand = int(input("How many card to start with? "))
starting_hand = 5

for i in range(0,10000):
  player1 = deal(starting_hand)
  player2 = deal(starting_hand)

  player1_turn_over = False
  player2_turn_over = True


  while end == False: 
    while player1_turn_over == False:
      if end == True:
        break
      ask = least_ask(player1)
      player1_asks.append(ask)
      player2, cards = beingasked(ask, player2)
      player1, score1 = getcards(cards,player1,score1)
      end = ifend()
      if turn == False:
        player2_turn_over = False
        player1_turn_over = True

      

    while player2_turn_over == False:
      if end == True:
        break
      ask = revenge_ask(player2, player1_asks)
      player2_asks.append(ask)
      player1, cards = beingasked(ask, player1)
      player2, score2 = getcards(cards,player2,score2)
      end = ifend()
      if turn == False:
        player1_turn_over = False
        player2_turn_over = True


 
  result()
 # print(i)
  reset_game()

print(player1wins, ties, player2wins)