def canRearrangeCards(hand, groupSize):
    freq_map = {}  # Dictionary to store the frequency of each card value

    for card in hand:
        if card in freq_map:
            freq_map[card] += 1
        else:
            freq_map[card] = 1

    while freq_map:
        # Find the minimum card value in the current available cards
        min_card = min(freq_map.keys())

        # Iterate through consecutive card values to form a group
        for i in range(min_card, min_card + groupSize):
            if i not in freq_map:
                return False
            freq_map[i] -= 1
            if freq_map[i] == 0:
                del freq_map[i]

        # Remove card values with frequency 0 from the map
        freq_map = {card: freq for card, freq in freq_map.items() if freq > 0}

    return True

# Example usage
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(canRearrangeCards(hand, groupSize))  # Output: False
