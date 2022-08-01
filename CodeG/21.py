import setup
num_of_games = 0
chips_next_round = 100

print('Welcome to BlackJack! Get as close to 21 as you can without going over!')
print('')
print('Dealer hits as long as she is below 21. Aces count as 1 or 11.')

while True:
# Create & shuffle the deck, deal two cards to each player
    deck = setup.Deck()
    deck.shuffle()
    
    player_hand = setup.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = setup.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips = setup.Chips()  # remember the default value is 100
    player_chips.total = chips_next_round
    
    # Prompt the Player for their bet:
    setup.take_bet(player_chips)
    
    # Show the cards:
    setup.show_some(player_hand,dealer_hand)
    
    while setup.playing:  # recall this variable from our hit_or_stand function
        print("")
        print("Player's Hand = {}".format(player_hand.value))
        print("You need {} more to hit 21.".format(21-player_hand.value))
        print("")
        print("Dealer's Hand = {}".format(dealer_hand.value))

        # Prompt for Player to Hit or Stand
        setup.hit_or_stand(deck,player_hand)
        setup.show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            setup.player_busts(player_hand,dealer_hand,player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 21:
            setup.hit(deck,dealer_hand)
            
        # Show all cards
        setup.show_all(player_hand,dealer_hand)
        
        # Test different winning scenarios
        if dealer_hand.value > 21:
            setup.dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            setup.dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            setup.player_wins(player_hand,dealer_hand,player_chips)

        else:
            setup.push(player_hand,dealer_hand)

    # Inform player of their chips total    
    print("\nPlayer's winnings stand at",player_chips.total)
    chips_next_round = player_chips.total

    num_of_games += 1
    
    if chips_next_round == 0:
      print("You have lost all of your chips! Thanks for playing!")
      break

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("You played {} hands! Thanks for playing!".format(num_of_games))
        break
