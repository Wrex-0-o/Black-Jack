import random
import sys
from art import logo

def random_card_generator():
    return random.choice(cards)

def score_21(player_cards):
    if sum(player_cards) == 21:
        return 0
    else:
        return 1

def blackjack(cards):
    print(logo)
    your_cards = []
    comp_cards = []
    comp_score = 0
    curr_score = 0
    for i in range(2):
        random_card_player = random_card_generator()
        random_card_comp = random_card_generator()
        curr_score += random_card_player
        comp_score += random_card_comp
        your_cards.append(random_card_player)
        comp_cards.append(random_card_comp)

    print(f"Your cards: {your_cards}, current score: {curr_score}")
    print(f"Computer's first card: {comp_cards[0]} \n\n")

    if score_21(your_cards) != 0:
        draw_cards = True
        while draw_cards:
            another_card = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()
            if another_card == 'y':
                random_card = random_card_generator()
                your_cards.append(random_card)
                curr_score += random_card
                print(f"Your cards {your_cards}, current score: {curr_score}")
                print(f"Computer's first card: {comp_cards[0]}\n\n")
                if curr_score > 21:
                    if 11 in your_cards:
                        your_cards.remove(11)
                        your_cards.append(1)
                        curr_score -= 10
                    else:
                        print("Oops! You overshot and Lost.")
                        decision = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
                        if decision == 'n':
                            sys.exit(0)
                        else:
                            print("\n" * 30)
                            blackjack(cards)
            else:
                draw_cards = False
    else:
        print("You have a Black-Jack!\n\n")
        if score_21(comp_cards) == 0:
            print("Its a Black-Jack from both the Parties. Draw!\n\n")
            return

    if score_21(comp_cards) != 0:
        while comp_score < 17:
            random_card = random_card_generator()
            comp_cards.append(random_card)
            comp_score += random_card
            
        if comp_score > 21:
            print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
            print("The Computer Overshot! You Win!\n\n")
        elif comp_score > curr_score:
            print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
            print("Oops! You Lose!\n\n")
        elif comp_score == curr_score:
            print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
            print("It's a Draw!\n\n")
        else:
            print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
            print("You WIN! Fair n Square.\n\n")
    else:
        print("Its a Black-Jack in the Dealer's Hand.")
        print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
        print("Sorry! You LOSE.\n\n")

    want_to_play = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
    if want_to_play == 'n':
        sys.exit(0)
    else:
        print("\n" * 30)
        blackjack(cards)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

decision = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()

if decision == 'n':
    sys.exit(0)
else:
    blackjack(cards)
