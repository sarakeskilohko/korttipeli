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
def deal (players, deck) -> dict:
    onecard = {}
    for i in players:
        onecard[i] = deck[0]
        deck.remove(onecard[i])
        return onecard


players = allPlayers()
print ("Players are:" + str(players))
print(defineDeck())