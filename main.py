import random
from art import logo

def random_card_generator():
    return random.choice(cards)

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
    print(f"Computer's first card: {comp_cards[0]}")

    draw_cards = True
    while draw_cards:
        another_card = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()
        if another_card == 'y':
            random_card = random_card_generator()
            your_cards.append(random_card)
            curr_score += random_card
            print(f"Your cards {your_cards}, current score: {curr_score}")
            print(f"Computer's first card: {comp_cards[0]}")
            if curr_score > 21:
                print("Oops! You overshot and Lost.")
                decision = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
                if decision == 'n':
                    return
                else:
                    blackjack(cards)
        else:
            draw_cards = False

    while comp_score < 17:
        random_card = random_card_generator()
        comp_cards.append(random_card)
        comp_score += random_card
        
    if comp_score > 21:
        print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
        print("The Computer Overshot! You Win!")
    elif comp_score > curr_score:
        print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
        print("Oops! You Lose!")
    elif comp_score == curr_score:
        print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
        print("It's a Draw!")
    else:
        print(f"Computer's Final hand: {comp_cards}, Computer score: {comp_score}")
        print("You WIN! Fair n Square.")

    want_to_play = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
    if want_to_play == 'n':
        return
    else:
        blackjack(cards)


play = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

decision = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()

if decision == 'n':
    play = False
else:
    blackjack(cards)




