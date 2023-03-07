# Rock Paper Scissors

def rps(p1, p2):
    p1_win = "Player 1 won!"
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors":
        return p1_win
    elif p1 == "paper" and p2 == "rock":
        return p1_win
    elif p1 == "scissors" and p2 == "paper":
        return p1_win
    else:
        return "Player 2 won!"


# Smarter way
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"