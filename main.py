import art, random
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
}

def draw_card(player: list):
    card = random.choice(list(cards.keys()))
    player.append(card)

def game():
    player_cards = random.choices(list(cards.keys()), k=2)
    dealer_cards = random.choices(list(cards.keys()), k=2)
    player_score = sum([cards[card] for card in player_cards])
    dealer_score = sum([cards[card] for card in dealer_cards])
    print(art.logo)
    while True:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        

game()