import random
import os
from art import logo

def deal_card():
    """ Deals a card"""  
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """ calculates score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "Everyone loses."

    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, blackjack computer"
    elif player_score == 0:
        return "Win, blackjack"
    elif player_score > 21:
        return "You went over"
    elif computer_score > 21:
        return "Dealer break"
    elif player_score > computer_score:
        return "Win"
    else:
        return "Lose"

def play_game():
    print(logo)
    
    player_hand = []
    computer_hand = []
    is_game_over = False

    [player_hand.append(deal_card()) for _ in range(2)]
    [computer_hand.append(deal_card()) for _ in range(2)]

    while not is_game_over: # When user wants to draw
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            draw_card = input("Type 'y' to get another card, 'n' for no. ")
            if draw_card == "y":
                player_hand.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Final Hand: {player_hand} | Score: {player_score}")
    print(f"Computer's Final Hand: {computer_hand} | Score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Want to play? Type 'y' for yes, 'n' for no. ") == 'y':
    os.system('cls')
    play_game()
