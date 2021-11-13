import random

Cards = {
    "Two of Clubs": 2,
    "Three of Clubs": 3,
    "Four of Clubs": 4,
    "Five of Clubs": 5,
    "Six of Clubs": 6,
    "Seven of Clubs": 7,
    "Eight of Clubs": 8,
    "Nine of Clubs": 9,
    "Ten of Clubs": 10,
    "Jack of clubs": 10,
    "Queen of Clubs": 10,
    "King of Clubs": 10,
    "Ace of Clubs": 1,
    "Two of Spades": 2,
    "Three of Spades": 3,
    "Four of Spades": 4,
    "Five of Spades": 5,
    "Six of Spades": 6,
    "Seven of Spades": 7,
    "Eight of Spades": 8,
    "Nine of Spades": 9,
    "Ten of Spades": 10,
    "Jack of Spades": 10,
    "Queen of Spades": 10,
    "King of Spades": 10,
    "Ace of Spades": 1,
    "Two of Diamonds": 2,
    "Three of Diamonds": 3,
    "Four of Diamonds": 4,
    "Five of Diamonds": 5,
    "Six of Diamonds": 6,
    "Seven of Diamonds": 7,
    "Eight of Diamonds": 8,
    "Nine of Diamonds": 9,
    "Ten of Diamonds": 10,
    "Jack of Diamonds": 10,
    "Queen of Diamonds": 10,
    "King of Diamonds": 10,
    "Ace of Diamonds": 1,
    "Two of Hearts": 2,
    "Three of Hearts": 3,
    "Four of Hearts": 4,
    "Five of Hearts": 5,
    "Six of Hearts": 6,
    "Seven of Hearts": 7,
    "Eight of Hearts": 8,
    "Nine of Hearts": 9,
    "Ten of Hearts": 10,
    "Jack of Hearts": 10,
    "Queen of Hearts": 10,
    "King of Hearts": 10,
    "Ace of Hearts": 1
}


def game():
    # Greet player and begin or quit game
    user_input = input("Welcome, press any key to begin or Q to quit")

    player_hand = {}  # cards player has been dealt
    player_score = 0  # players current score
    comp_hand = {}  # cards comp has been dealt
    comp_score = 0  # comp current score

    # First hand player and computer receive two cards
    hands_dealt = 0

    while user_input != "Q":
        # Cards are randomly selected from dictionary
        player_next_card = dict([random.choice(list(Cards.items()))])
        comp_most_next_card = dict([random.choice(list(Cards.items()))])
        # The card about to be dealt is stored as a string, allowing it to be compared to cards already dealt and
        # avoid duplicate cards being dealt.
        player_next_key = list(player_next_card)[0]
        comp_next_key = list(comp_most_next_card)[0]

        # Check for duplicates, if card about to be dealt is already in someone's hands, select different card
        if player_next_key in list(player_hand) or player_next_key in list(comp_hand) or comp_next_key in list(comp_hand) or comp_next_key in list(player_hand):
            continue

        else:
            player_hand.update(player_next_card) # add card to player hand
            player_score = sum(player_hand.values()) # player score equals the sum of the value of all cards in hand
            comp_hand.update(comp_most_next_card) # add card to computer hand
            comp_score = sum(comp_hand.values()) # computer score equals the sum of the value of all cards in hand
            if hands_dealt == 0:  # player and comp should receive two cards
                hands_dealt += 1
                continue
            print("PLAYER ",list(player_hand), "Player Score: ", player_score)
            print("COMPUTER ",list(comp_hand), "Comp Score: ", comp_score)

            hands_dealt += 1

        # The logic below was changed to more accurately reflect winds and losses, try comparing the changes using 'Blame' in github (we can go over this)
        if player_score < 21 and comp_score < 21:
            user_input = input("Press any key to continue or Q to quit")

        elif player_score == 21 and comp_score != 21:
            print("You win!")
            user_input = input("Press any key to continue or Q to quit")
            player_hand.clear()
            comp_hand.clear()
            player_score = 0
            comp_score = 0

        elif comp_score == 21 and player_score != 21:
            print("You loose")
            user_input = input("Press any key to continue or Q to quit")
            player_hand.clear()
            comp_hand.clear()
            player_score = 0
            comp_score = 0

        elif comp_score == 21 and player_score == 21:
            print("Tie")
            user_input = input("Press any key to continue or Q to quit")
            player_hand.clear()
            comp_hand.clear()
            player_score = 0
            comp_score = 0

        elif comp_score > 21 and player_score <= 21:
            print("You win!")
            user_input = input("Press any key to continue or Q to quit")
            player_hand.clear()
            comp_hand.clear()
            player_score = 0
            comp_score = 0

        elif player_score > 21 and comp_score <= 21:
            print("You loose")
            user_input = input("Press any key to continue or Q to quit")
            player_hand.clear()
            comp_hand.clear()
            player_score = 0
            comp_score = 0

        else:
            print("Something else happened")


if __name__ == '__main__':
    game()