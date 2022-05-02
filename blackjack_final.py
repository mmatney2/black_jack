import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

suits = ["Spades \u2664", "Hearts \u2661", "Clubs \u2667", "Diamonds \u2662"]
card_name = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
card_value = {
    "Ace": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6, 
    "Seven": 7, 
    "Eight": 8,
    "Nine": 9, 
    "Ten": 10, 
    "Jack": 10, 
    "Queen": 10, 
    "King": 10,
}

class Card():
    def __init__(self, suit, card_name, card_value):
        self.suit = suit
        self.card_name = card_name
        self.card_value = card_value

class Deck:
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for card in card_name:
                self.deck.append(Card(suit, card, card_value[card]))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card
        
class Dealer:
    def __init__(self, dealer, dealer_hand):
        self.dealer = dealer
        self.dealer_hand = dealer_hand
    def dealer_play(self):
        self.dealer.deal()
    def dealer_win(self):
        print('You lose')
        self.player.end_game()
    def dealer_blackjack_win(self):
        print('')
    def dealer_bust(self):
        print('You Win, dealer bust!')
        self.dealer.endgame()
    def calculate_dealer_score(self):
        self.hand = range(self.hand)
        if self.score > 21 and self.aces > 0:
            self.score -= 10
            self.aces -= 1
            # self.dealer.
            self.dealer.show_all_cards()
    def show_cards(self):
        #display cards
        while True:
            if 21>=self.dealer_hand > self.score:
                self.dealer.dealer_win()
            elif 17> self.dealer_hand < self.score:
                self.dealer.show_cards()
            elif self.dealer_hand > 21:
                self.dealer.dealer_bust()



class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.aces = 0

    def add_card(self, card):
        self.hand.append(card)
        self.score += card_value[card.card_name]
        if card.card_name == "Ace":
            self.aces += 1

    def calculate_score(self):
        if self.score > 21 and self.aces > 0:
            self.score -= 10
            self.aces -= 1
           
class Blackjack:
    def __init___(self, player, dealer, hand):
        self.player = player
        self.dealer = dealer
        self.hand = hand
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Player()
        self.player = Player()
        self.playing = None
    
    def welcome(self):
        print('welcome to BLACKJACK!') 
        name = input('enter name to get started')
        if name.lower() != 'quit':
            self.player_playgame()       
    def push_game(self):
        print('PUSH.')
        self.player.endgame()
    def player_playgame(self):
        self.playing = True
        while True:
            play = input('Would you like to play? yes or no?: ')
            if play.lower() == 'yes':
                print('heres your cards')
                self.playing = True
                self.start_game()
                h_or_s = input('would you like to hit or stand? [h/s]: ')
                
            if h_or_s == 'hit':
                print('heres your new cards.')
            if h_or_s == 'stand':
                print('dealers turn')
                self.hand.show_player_cards()
            if h_or_s != 'hit' or 'stand':
                print('please pick a valid response')
                self.hand.show_player_cards()
            if play.lower() == 'no':
                print('thanks for playing!')
                self.playing = False
                break
            else:
                print('please pick a valid entry')

    def start_game(self):
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.calculate_score()
    def show_player_cards(self):
        self.playing = True
        print("\nYour hand:")
        for ind in range(len(self.player.hand)):
            print(f"{self.player.hand[ind].card_name} of {self.player.hand[ind].suit}")
        print("Your score:", self.player.score)
        print("\nDealer hand:\n<HIDDEN CARD>")
        for ind in range(1, len(self.dealer.hand)):
            print(f"{self.dealer.hand[ind].card_name} of {self.dealer.hand[ind].suit}")
    def show_all_cards(self):
        print("Your hand:")
        for ind in range(len(self.player.hand)):
            print(f"{self.player.hand[ind].card_name} of {self.player.hand[ind].suit}")
        print("Your score:", self.player.score)
        print("\nDealer hand:")
        for ind in range(len(self.dealer.hand)):
            print(f"{self.dealer.hand[ind].card_name} of {self.dealer.hand[ind].suit}")
        print("Dealer score:", self.dealer.score)
    def endgame(self):
        play = input('would you like to play again?')
        if play.lower == 'yes:':
            self.player.welcome()
        elif play.lower == 'no':
            print('thanks for playing again')
            
        else:
            print('please pick a valid option')
    def player_win(self):
        self.player.endgame()
        
    def player_blackjack_win(self):
        print("BLACKJACK!")
        self.player.player_win()
    def player_bust(self):
        print("You bust. Dealer Wins.")

    

def main():
    clear_screen()
    game = Blackjack()
    game.welcome()

if __name__ == "__main__":
    main()