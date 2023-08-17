import art, random, math
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

def draw_card(player: list):
    card = random.choice(list(cards.keys()))
    player.append(card)
def calculate_score(cards_list: list):
    score = sum([cards[card] for card in cards_list])
    aces_to_be_one = math.ceil((score - 21) / 10)
    if cards_list.count("A") >= aces_to_be_one:
        score -= aces_to_be_one * 10
    else:
        score -= cards_list.count("A") * 10
    return score

def dealer_turn(dealer_cards: list, player_cards: list):
    while calculate_score(dealer_cards) < 17:
        draw_card(dealer_cards)
    if calculate_score(dealer_cards) > 21:
        print("you win")
    elif calculate_score(dealer_cards) > calculate_score(player_cards):
        print("you lose")
    elif calculate_score(dealer_cards) == calculate_score(player_cards):
        print("draw")
    elif calculate_score(dealer_cards) < calculate_score(player_cards):
        print('you win')


def game():
    player_cards = random.choices(list(cards.keys()), k=2)
    dealer_cards = random.choices(list(cards.keys()), k=2)
    print(art.logo)
    while True:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw == 'y':
            draw_card(player_cards)
            print(player_cards)
            if calculate_score(player_cards) > 21:
                print("you lose")
                break
            else:
                continue
        elif draw == 'n':
            if calculate_score(dealer_cards) > calculate_score(player_cards):
                print("You lose")
                break
            elif calculate_score(dealer_cards) <= calculate_score(player_cards):
                dealer_turn()
                break
                
game()