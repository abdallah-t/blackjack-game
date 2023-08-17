import art
import random
import math

# Define the values of different cards
cards = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}

# Function to draw a card for a player
def draw_card(player: list):
    card = random.choice(list(cards.keys()))
    player.append(card)

# Function to calculate the total score of a list of cards
def calculate_score(cards_list: list):
    score = sum([cards[card] for card in cards_list])

    # Handling the value of Aces when score exceeds 21
    if score > 21:
        aces_to_be_one = math.ceil((score - 21) / 10)
        if cards_list.count("A") >= aces_to_be_one:
            score -= aces_to_be_one * 10
        else:
            score -= cards_list.count("A") * 10
    return score

# Function to handle the dealer's turn
def dealer_turn(dealer_cards: list, player_cards: list):
    while calculate_score(dealer_cards) < 17:
        draw_card(dealer_cards)

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    # Determine the winner or a draw based on scores
    if dealer_score > 21:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"dealer's cards: {dealer_cards}: score: {dealer_score}")
        print("You win")
    elif dealer_score > player_score:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"dealer's cards: {dealer_cards}, score: {dealer_score}")
        print("You lose")
    elif dealer_score == player_score:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"dealer's cards: {dealer_cards}, score: {dealer_score}")
        print("Draw")
    elif dealer_score < player_score:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"dealer's cards: {dealer_cards}, score: {dealer_score}")
        print('You win')

# Main game loop
def game():
    player_cards = random.choices(list(cards.keys()), k=2)
    dealer_cards = random.choices(list(cards.keys()), k=2)
    print(art.logo)

    while True:
        player_score = calculate_score(player_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        draw = input("Type 'y' to get another card, type 'n' to pass: ")

        if draw == 'y':
            draw_card(player_cards)
            print(player_cards)
            if calculate_score(player_cards) > 21:
                print(f"Your cards: {player_cards}, current score: {player_score}")
                print(f"dealer's cards: {dealer_cards}, score: {calculate_score(dealer_cards)}")
                print("You lose")
                break
            else:
                continue
        elif draw == 'n':
            if calculate_score(dealer_cards) > calculate_score(player_cards):
                print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
                print(f"dealer's cards: {dealer_cards}, score: {calculate_score(dealer_cards)}")
                print("You lose")
                break
            elif calculate_score(dealer_cards) <= calculate_score(player_cards):
                dealer_turn(dealer_cards, player_cards)
                break

# Main loop to play the game multiple times
while True:
    game()
    play_again = input("Would you like to play again? 'y' / 'n'\n")
    if play_again.lower() == 'y':
        continue
    else:
        break