# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:16:14 2020

@author: RGhogare
"""


# Code for simplified version of Blackjack Game

import random

playing = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three','Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':11}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value= values[rank]
        
    def __str__(self):
        return self.rank + 'of' + self.suit
        
class Deck:
    def __init__(self):
        # Creating an empty array to store 52 cards
        self.all_cards = [] 
        
        # looping over an array of 52 cards from given tuple ans list
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def __str__(self):
        deck_card = ''  
        for card in self.all_cards:
            # calling each object of class card for printing
            deck_card += '\n '+card.__str__()  
        return 'The deck has:' + deck_card
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_card(self):
        return self.all_cards.pop()
        
class HandClass:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value +=values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1
        
        
    def reassign_ace_value(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -=1
            
class Chips:
    
    def __init__(self):
        self.amount = 100
        self.bet = 0
        
    def win_amount(self):
        self.amount +=self.bet
        
    def lose_amount(self):
        self.amount -=self.bet
        

def request_bet(chips):
#    if Chips().bet > Chips().amount:
#        print('Please enter valid amount')
#    else:
#        print('Please start playing...!')
    while True:
        try:
            chips.bet = int(input('Please Enter an amount to be bet..!!!'))
        except ValueError:
            print('Sorry thats invalid number...please eneter whole Number')
        else:
            if chips.bet > chips.amount:
                print('Please Check your balance and entered value exceeded balance amount!')
            else:
                break
            
def Hit(deck,handclass):
    deck.shuffle()
    handclass.add_card(deck.deal_card())
    handclass.reassign_ace_value()
    
def bust_or_stand(deck,handclass):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's':")
        
        if x[0].lower() == 'h':
            Hit(deck,handclass)
            
        elif x[1].lower() == 's':
            print('Player stand..Dealer is playing')
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break
          
    
def visible_few_cards(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
    
    
def player_busts(player,dealer,chips):
    print('Player has busted')
    chips.lose_amount()
    
def player_wins(player,dealer,chips):
    print('Player has wins')
    chips.win_amount()

def dealer_busts(player,dealer,chips):
    print('Dealer has wins')
    chips.win_amount()
    
def dealer_wins(player,dealer,chips):
    print('Dealer has wins..')
    chips.lose_amount()
    
def push(player,dealer,chips):
    print("Dealer and Player tie! It's a push.")
    
while True:
    print('Grand Welcome to BlackJack Game at Casino! Try to reach to 21 and  without spilling over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, and each player can get two cards 
    deck = Deck()
    deck.shuffle()
    
    player_hand = HandClass()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand = HandClass()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    
    # Setting up players bet deal
    
    player_chips = Chips()
    
    # Prompt the Player for their bet
    request_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    visible_few_cards(player_hand, dealer_hand)
    
    
    while playing:
        # Prompt for Player to Hit or Stand
        bust_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        visible_few_cards(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
     # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            Hit(deck, player_hand)
        # Show all cards
        show_all(player_hand, dealer_hand)
        
        # visit different winning scenarios
        
        if dealer_hand.value > 21:
            player_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand)
            
            
    # Intimating Player of their final chips total 
    print("\nPlayer's winnings stand at",player_chips.amount)

            
    # Request a new game  again
    new_game  = input ("\n Do you wish to play new game again: Enter 'Y' or'N' " )
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks...Do visit Again..')
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
                
    


        
            
        

        