from RPS import player
import random

# Example bot: always plays 'R'
def always_rock(prev_play, opponent_history=[]):
    return "R"

# Example bot: cycles through R, P, S
def cycle_bot(prev_play, opponent_history=[]):
    moves = ["R", "P", "S"]
    if not opponent_history:
        opponent_history.append(random.choice(moves))
    else:
        last = opponent_history[-1]
        idx = moves.index(last)
        opponent_history.append(moves[(idx + 1) % 3])
    return opponent_history[-1]

# Play function to simulate matches
def play(player1, player2, num_games, verbose=False):
    p1_history = []
    p2_history = []
    p1_score = 0
    p2_score = 0
    beats = {"R": "S", "P": "R", "S": "P"}
    prev1 = ""
    prev2 = ""
    for i in range(num_games):
        move1 = player1(prev2, p2_history)
        move2 = player2(prev1, p1_history)
        p1_history.append(move1)
        p2_history.append(move2)
        prev1 = move1
        prev2 = move2
        if move1 == move2:
            result = "Tie"
        elif beats[move1] == move2:
            p1_score += 1
            result = "Player 1 wins"
        else:
            p2_score += 1
            result = "Player 2 wins"
        if verbose:
            print(f"Game {i+1}: Player 1 ({move1}) vs Player 2 ({move2}) -> {result}")
    print(f"Player 1 score: {p1_score}")
    print(f"Player 2 score: {p2_score}")
    print(f"Win rate: {p1_score/num_games*100:.2f}%")

if __name__ == "__main__":
    print("Testing player vs always_rock bot:")
    play(player, always_rock, 1000, verbose=False)
    print("\nTesting player vs cycle_bot:")
    play(player, cycle_bot, 1000, verbose=False)
    # Uncomment the next line if you have test_module.py
    # import test_module 