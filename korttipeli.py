import random

# luodaan peli kahdelle hengelle
def allPlayers() -> list:
    players = []
    player1 = str(input("Name?"))
    player2 = str(input("Name?"))
    players.append(player1)
    players.append(player2)

    return players

# luodaan korttipakka pelaamista varten
def defineDeck() -> list:
    card = 1
    deck = []
    for card in range(1, 14):
        deck.append(('♤', card))
        deck.append(('❤', card))
        deck.append(('✠', card))
        deck.append(('♢', card))
        card = card + 1

   #sekoitetaan pakka vielä valmiiksi tässä metodissa
    deck = shuffle(deck)
    return deck


def shuffle(deck):
     random.shuffle(deck)
     return deck

#tehdään metodi, joka ajetaan joka pelikierroksen välissä = jaetaan pelaajille kortti
#tehdään metodit erikseen kummallekkin pelaajille, jotta kortit tallennetaan eri sanakirjoihin
def deal1 (players, deck) -> dict:
    player1 = {}
    for i in players:
        player1[i] = deck[0]
        deck.remove(player1[i])
        return player1

def deal2 (players, deck) -> dict:
    player2 = {}
    length = len(players)
    for index in range(1 , length):
        i = players[index]
        player2[i] = deck[0]
        deck.remove(player2[i])
        return player2


def number1(deal1):
    card1 = deal1(players, deck)
    list = card1.keys()
    card = list[0]
    guess = int(input("Which number?"))
    if guess == card:
        print("Correct! Give one drink!")
        print("Card was: " + str(card1))
    else:
        print("Wrong, drink one!")
        print("Card was: " + str(card1))

def number2(deal2):
    card2 = deal2(players, deck)
    list = card2.keys()
    card = list[0]
    guess = int(input("Which number?"))
    if guess == card:
        print("Correct! Give one drink!")
        print("Card was: " + str(card2))
    else:
        print("Wrong, drink one!")
        print("Card was: " + str(card2))


def compare1(deal1):
    card = deal1(players, deck)
    guess = str(input("Higher, lower or same?"))
    if guess == 'higher' and card[0] < card[1]:
        print("Correct! Give two drinks!")
        print("Card was: " + str(card[1]))
    elif guess == 'lower' and card[0] > card[1]:
        print("Correct, give two drinks!")
        print("Card was: " + str(card[1]))
    elif guess == 'same' and card[0] == card[1]:
        print("Correct, give two drinks!")
        print("Card was: " + str(card[1]))
    else:
        print("Wrong, drink one!")
        print("Card was: " + str(card[1]))

def compare2(deal2):
    card = deal2(players, deck)
    guess = str(input("Higher, lower or same?"))
    if guess == 'higher' and card[0] < card[1]:
        print("Correct! Give two drinks!")
        print("Card was: " + str(card[1]))
    elif guess == 'lower' and card[0] > card[1]:
        print("Correct, give two drinks!")
        print("Card was: " + str(card[1]))
    elif guess == 'same' and card[0] == card[1]:
        print("Correct, give two drinks!")
        print("Card was: " + str(card[1]))
    else:
        print("Wrong, drink one!")
        print("Card was: " + str(card[1]))


#print(defineDeck())
players = allPlayers()
print ("Players are:" + str(players))
deck = defineDeck()
#kortit1 = deal1(players, deck)
#kortit2 = deal2(players, deck)
#print(kortit1)
#print(kortit2)
number1(deal1)
number2(deal2)
print(str(deal1))
#compare1(deal1)
#compare2(deal2)
