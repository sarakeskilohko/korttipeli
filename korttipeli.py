import random

# luodaan peli kahdelle hengelle
def allPlayers() -> list:
    players = []
    player1 = str(input("Name?"))
    player2 = str(input("Name?"))
    players.append(player1)
    players.append(player2)

    return players

print ("Players are")
allPlayers()

# luodaan korttipakka pelaamista varten
def defineDeck() -> list:
    card = 1
    deck = []
    for i in range(1, 14):
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
print(defineDeck())

#tehdään metodi, joka ajetaan joka pelikierroksen välissä = jaetaan pelaajille kortti
def deal (players, deck) -> dict:
    onecard = {}
    for i in players:
        #yksi random kortti pakasta/hlö ja kortti poistetaan pakasta, kortit tallennetaan pelaajille erikseen