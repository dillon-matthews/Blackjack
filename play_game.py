from DeckOfCards import DeckOfCards

def calculate_score(hand):
    # Calculate total score, adjusting for Aces as needed.
    score = sum(card.val for card in hand)
    aces = sum(1 for card in hand if card.face == 'Ace')
    # Reduce score for each Ace if it helps to avoid busting.
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def play_blackjack():
    deck = DeckOfCards()
    print("Welcome to Black Jack!\n")

    # Showing the deck, shuffled and then shuffled.
    print("deck before shuffled:")
    deck.print_deck()

    deck.shuffle_deck()
    print("\ndeck after shuffled:")
    deck.print_deck()

    # Initial card dealing.
    player_hand = [deck.get_card(), deck.get_card()]
    dealer_hand = [deck.get_card(), deck.get_card()]

    # Player's turn to hit or stand.
    playing = True
    while playing:
        print("\nYour hand:", ', '.join(str(card) for card in player_hand))
        player_score = calculate_score(player_hand)
        print("Your total score is:", player_score)

        # Check for bust; otherwise, offer hit.
        if player_score > 21:
            print("You bust! Dealer wins.")
            break

        hit = input("Would you like a hit?(y/n) ").lower()
        if hit == 'y':
            player_hand.append(deck.get_card())
        else:
            playing = False

    # Dealer's turn if player hasn't busted.
    if not player_score > 21:
        print("\nDealer's hand:", ', '.join(str(card) for card in dealer_hand))
        dealer_score = calculate_score(dealer_hand)
        # Dealer hits until reaching 17 or more.
        while dealer_score < 17:
            dealer_hand.append(deck.get_card())
            dealer_score = calculate_score(dealer_hand)

        # Determine and announce winner.
        print("Dealer's score is:", dealer_score)
        if dealer_score > 21 or player_score > dealer_score:
            print("You win!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    # Option to play again.
    if input("\nAnother game?(y/n): ").lower() == 'y':
        play_blackjack()

if __name__ == "__main__":
    play_blackjack()

