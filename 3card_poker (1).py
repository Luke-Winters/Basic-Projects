def convert_hand(num: int) -> str:
    """
    Converts a single card from an int value to a str.
        
    Args:
        num: the number value of a card
            
    Returns:
        str: the card represented as a string
    """
    if num == 2:
        return "2"
    elif num == 3:
        return "3"
    elif num == 4:
        return "4"
    elif num == 5:
        return "5"
    elif num == 6:
        return "6"
    elif num == 7:
        return "7"
    elif num == 8:
        return "8"
    elif num == 9:
        return "9"
    elif num == 10:
        return "X"
    elif num == 11:
        return "J"
    elif num == 12:
        return "Q"
    elif num == 13:
        return "K"
    elif num == 14:
        return "A"

def hand_to_string(nums: list[int]) -> str:
    """
    Converts a hand of three cards into a single string
        
    Args:
        nums: list of ints representing cards
            
    Returns:
        str: a string of three characters representing the hand
    """
    return convert_hand(nums[0]) + " " + convert_hand(nums[1]) + " " + convert_hand(nums[2])

def sort_hand(hand: list[int]) -> list[int]:
    """
    Sorts a hand of cards from largest to smallest.
        
    Args:
        hand: list of ints representing cards
            
    Returns:
        list[int]: the same hand sorted from largest to smallest card values
    """
    if hand[0] < hand[1]:
        hand[0], hand[1] = hand[1], hand[0]
    if hand[1] < hand[2]:
        hand[1], hand[2] = hand[2], hand[1]
    if hand[0] < hand[1]:
        hand[0], hand[1] = hand[1], hand[0]
    return hand

def has_triple(hand: list[int]) -> bool:
    """
    Determines if a hand has a triple.
        
    Args:
        hand: list of ints representing cards
            
    Returns:
        bool: wehter or not the hand contains all three of the same cards
    """
    return hand[0] == hand[1] == hand[2]

def has_straight(hand: list[int]) -> bool:
    """
    Determines if a hand has a straight.
        
    Args:
        hand: list of ints representing cards
            
    Returns:
        bool: whether or not the hand contains a straigth
    """
    return hand[1] == hand[0]-1 and hand[2] == hand[0] - 2

def has_pair(hand: list[int]) -> bool:
    """
    Determines if a hand has a pair.
        
    Args:
        hand: list of ints representing cards
            
    Returns:
        bool: wheter or not the hand contains a pair of cards
    """
    return hand[0] == hand[1] or hand[0] == hand[2] or hand[1] == hand[2]

def score_hand(hand: list[int]) -> int:
    """
    Determines the score of a hand.
    
    Args:
        hand: list of ints representing cards  
        
    Returns:
        int: the score of the players hand
    """
    if has_triple(hand):
        feature = 16
    elif has_straight(hand):
        feature = 15
    elif has_pair(hand):
        if hand[0] == hand[1]:
            feature = hand[0]
        elif hand[1] == hand[2]:
            feature = hand[1]
    else:
        feature = 0
    return feature * 16**3 + hand[0] * 16**2 + hand[1] * 16 + hand[2]

def dealer_plays(hand: list[int]) -> bool:
    """
    Takes in the hand of a dealer and decides whether it should play the hand or not
      
    Args:
        hand: list of ints representing cards
        
    Returns:
        bool: if dealer plays or not
    """
    if score_hand(hand) > score_hand([11, 10, 8]):
        return True
    else: 
        return False
    
def play_round() -> int:
    """
    Plays a round of 3 card poker
    
    returns:
        int: the players score after a round
    """
    score = 0
    player_hand = sort_hand(deal())
    print(hand_to_string(player_hand))
    choice = get_choice()
    if choice == 'f':
        return score -10
    elif choice == 'p':
        dealer_hand = sort_hand(deal())
        print(hand_to_string(dealer_hand))
        if not dealer_plays(dealer_hand):
            return score + 10
        elif dealer_plays(dealer_hand):
            if score_hand(player_hand) < score_hand(dealer_hand):
                return score - 20
            elif score_hand(player_hand) > score_hand(dealer_hand):
                return score + 20
            elif score_hand(player_hand) == score_hand(dealer_hand):
                return score + 20
            
def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

from random import randint

def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
while True:
    score += play_round()
    print("Your score is", score, "... Starting a new round!")
    