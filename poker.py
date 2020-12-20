'''
author: Alexis Bianco
date created: 4/6/2020

edit 12/20/2020 -- TODO: fix the global variables issue and just pass functions
'''
import random

def create_cards():
    '''
    Creates the playing cards
    :return: List of 52 tuples in the format (rank, suit)
    '''

    global the_deck = []
    
    for suit in range(0, 4):

        if suit == 0:
            card_suit = "SPADES"
        elif suit == 1:
            card_suit = "DIAMONDS"
        elif suit == 2:
            card_suit = "CLUBS"
        else:
            card_suit = "HEARTS"

        for rank in range(2, 15):

            if rank == 14:
                the_deck.append(("A", card_suit))
            elif rank == 13:
                the_deck.append(("K", card_suit))
            elif rank == 12: 
                the_deck.append(("Q", card_suit))
            elif rank == 11:
                the_deck.append(("J", card_suit))
            else:
                the_deck.append((str(rank), card_suit))
    
    return the_deck


def shuffle_cards():
    '''
    shuffles the deck of cards randomly each time
    :return: list of tuples in random order
    '''
    return random.sample(create_cards(), 52)


def enter_number_opponents():
    '''
    user inputs the number of opponents
    :return: int number of opponents
    '''
    num_opponents = int(input("Enter the number of opponents between 1 and 7:"))

    while num_opponents < 1 or num_opponents > 7:
        if int(num_opponents) > 7:
            num_opponents = int(input("Please enter a number less than 8:"))
        if int(num_opponents) <= 0:
            num_opponents = int(input("Please enter a number between 1 and 7: "))

    return num_opponents


def deal_out_cards():
    '''
    gives two cards to each opponent and the user
    prints out the user's hand
    :return:
    '''
    global the_deck = shuffle_cards()
    num_opponents = enter_number_opponents()
    remaining_deck = the_deck #TODO: FIX THIS
    #print(the_deck)
    return remaining_deck


def burn_cards(the_deck):
    return the_deck.pop(0)


def run_one_round():
    pass


if __name__ == "__main__":
    #print(enter_number_opponents())
    deal_out_cards()
    burn_cards(the_deck)
    
