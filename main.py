import random
from replit import clear
from art import logo

def deal_cards(list):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    list.append(random.choice(cards))

#replace the 11 (Ace) with a value of 1 when beneficial
def calculate_ace(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

#display pretty results
def calculate_results(user, computer):
    result = ["win", "lose", "draw"]
    if computer == user:
        return(result[2])
    if user > 21:
        return(result[1])
    if computer > 21:
        return(result[0])
    if user > computer:
        return(result[0])
    if computer > user:
        return(result[1])

def black_jack():
    user_cards = []
    computer_cards = []
    playing = True
    print(logo)

    #deal 2 cards to the user and computer
    deal_cards(user_cards)
    deal_cards(user_cards)
    calculate_ace(user_cards)
    deal_cards(computer_cards)
    deal_cards(computer_cards)
    calculate_ace(computer_cards)
        
    while playing:
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)

        #add statement for computer black jack
        if computer_score == 21 and len(computer_cards) == 2:
            print("Your opponent got a black jack, you lose")
            playing = False
            
        #give the computer more cards if their score is less than 16
        while computer_score < 16:
            deal_cards(computer_cards)
            calculate_ace(computer_cards)
            computer_score = sum(computer_cards)
        
        print(f"You have {user_cards}, your opponent has a {computer_cards[0]}")
        drawing = True
        while drawing and user_score <= 21:
            #add statement for user black jack
            if user_score == 21 and len(user_cards) == 2:
                print("You got a Black Jack!")
                playing = False
            if user_score <21 and computer_score != 21:
                draw = input("Do you want to draw another card?  Type 'y' or 'n': ")
                if draw == 'y':
                    deal_cards(user_cards)
                    user_score = sum(user_cards)
                    calculate_ace(user_cards)
                    print(f"Your hand is {user_cards}")
                else: 
                    drawing = False
            else:
                drawing = False
        else:
            playing = False
            calculate_ace(user_cards)
            user_score = sum(user_cards)
            calculate_ace(computer_cards)
            computer_score = sum(computer_cards)
            print (f" Your final hand was {user_cards}.  Your final score was {user_score}.\n Your opponent's final hand was {computer_cards}.  Your opponents score was {computer_score}. \n You {calculate_results(user_score, computer_score)}.")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  black_jack()
