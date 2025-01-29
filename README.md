# Blackjack Game (Python Implementation)

## Overview
This project is a **Blackjack (21)** game implemented in Python. It demonstrates the use of **Classes and Objects** to create a deck of cards, shuffle them, deal hands, and implement game logic. The player competes against the dealer to achieve a hand value closest to 21 without exceeding it.

## Features

### Core Functionality
- **Deck of Cards**: A full deck of 52 playing cards is created using the `DeckOfCards` class.
- **Shuffling Mechanism**: The deck is shuffled before the game starts.
- **Dealing Cards**: Players receive two initial cards, and additional cards can be drawn.
- **Game Mechanics**: Players decide whether to take a "hit" (draw another card) or "stand" (stop drawing).
- **Dealer AI**: The dealer automatically draws cards until reaching at least 17 points.
- **Winning Conditions**:
  - Player wins if their score is **higher than the dealer's** but does not exceed 21.
  - Player wins if the **dealer busts** by exceeding 21.
  - Player loses if they **bust** (go over 21) or if the dealer has an equal or higher score without busting.
- **Ace Handling**: Aces can count as **11 or 1** depending on the player's hand to prevent busting.
- **Replay Option**: The game allows players to play multiple rounds using the same deck.

## Game Flow
1. **Welcome Message**: Displayed at the start of the game.
2. **Deck Initialization & Shuffle**: The deck is printed before and after shuffling to verify the shuffle mechanism.
3. **Initial Deal**: Two cards are dealt to both the player and dealer (dealer's cards remain hidden initially).
4. **Player Turn**:
   - The player can hit (draw another card) or stand.
   - If the player busts, the dealer wins immediately.
5. **Dealer Turn**:
   - The dealer reveals their cards and keeps drawing until reaching 17 or higher.
   - If the dealer busts, the player wins.
6. **Result Determination**:
   - The player and dealer scores are compared.
   - A winner is declared based on the rules.
7. **Replay Prompt**: The player can choose to play again, and the deck is reshuffled.

## Code Structure
- **`DeckOfCards.py`**: Contains the `Card` and `DeckOfCards` classes.
  - `Card`: Represents an individual playing card.
  - `DeckOfCards`: Manages the deck, shuffling, and dealing cards.
- **`play_game.py`**: Implements the game logic.
  - Imports `DeckOfCards` from `DeckOfCards.py`.
  - Manages player interactions and game flow.
  - Handles scoring and winner determination.

## Scoring System
- **Number Cards (2-10)**: Face value.
- **Face Cards (Jack, Queen, King)**: 10 points each.
- **Ace**: 11 points (can be adjusted to 1 if needed to avoid busting).

## Example Game Output
```
Welcome to Black Jack!

deck before shuffled:
2 of Hearts, 3 of Hearts, ..., Ace of Clubs

deck after shuffled:
8 of Hearts, 10 of Clubs, ..., Queen of Spades

Your hand: 8 of Hearts, 10 of Clubs
Your total score is: 18
Would you like a hit? (y/n) n

Dealer's hand: 9 of Spades, King of Diamonds
Dealer score is: 19
Dealer score is higher, you lose!
Another game? (y/n) y
```

## Future Enhancements
- Implement **betting mechanics** for added challenge.
- Add **multiplayer support** for local or online play.
- Improve **dealer AI** for more dynamic gameplay.
- Introduce **graphics and GUI** instead of text-based gameplay.

---

_Developed as an example of object-oriented programming and game logic in Python._

