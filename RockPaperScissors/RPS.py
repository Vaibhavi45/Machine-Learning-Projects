import random

def player(prev_play, opponent_history=[]):
    # Track opponent's moves
    if prev_play:
        opponent_history.append(prev_play)

    # If not enough history, play randomly
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    # Count frequency of opponent's moves
    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1
    most_common = max(freq, key=freq.get)

    # Counter the most common move
    counter = {"R": "P", "P": "S", "S": "R"}
    prediction = most_common
    move = counter[prediction]

    # Pattern detection: check for repeated sequences
    if len(opponent_history) > 5:
        pattern_length = 3
        recent = opponent_history[-pattern_length:]
        for i in range(len(opponent_history) - pattern_length):
            if opponent_history[i:i+pattern_length] == recent:
                # Predict the next move in the pattern
                if i + pattern_length < len(opponent_history):
                    prediction = opponent_history[i + pattern_length]
                    move = counter[prediction]
                    break

    return move 