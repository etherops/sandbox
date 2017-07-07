#!/usr/bin/python

from pprint import pprint
import random

class CardDeck:
    CARDS = [str(c) for c in range(2,10)] + ['J', 'Q', 'K', 'A']
    SUITS = ['S', 'H', 'D', 'C']

    def __init__(self):
        self.items = [card + suit for suit in self.SUITS for card in self.CARDS]

    def __str__(self):
        return str(self.items)

    def shuffle(self):
        random.shuffle(self.items)

    def deal_card(self):
        return self.items.pop()


class Player:
    def __init__(self):
        self.cards= []

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return self.__str__()

    def add_card(self, card):
        self.cards.append(card)


class Dealer:
    def deal_a_round(self, deck, players):
        for player in players:
            player.add_card(deck.deal_card())

    def shuffle_deck(self, deck):
        deck.shuffle()

deck = CardDeck()
dealer = Dealer()
players = [Player() for i in range(4)]

dealer.shuffle_deck(deck)

print deck

for i in range(5):
    dealer.deal_a_round(deck, players)

print deck

pprint(players)
