import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def simulate_game(n_cells, p_advance_a=0.5, p_rock_a=1/3):
    """
    Simulates a single game of Rayuela Mortal using NumPy.
    
    Parameters:
    - n_cells: Length of the board.
    - p_advance_a: Probability that team A moves on a turn.
    - p_rock_a: Probability that A chooses rock in a duel.
    """
    pos_a = 0
    pos_b = n_cells - 1
    turns = 0
    
    # RPS probabilities for A
    # Remaining 1-p_rock_a is split between paper and scissors
    p_other = (1 - p_rock_a) / 2
    probs_a = [p_rock_a, p_other, p_other]
    probs_b = [1/3, 1/3, 1/3]
    
    while True:
        turns += 1
        
        # Movement phase
        if np.random.random() < p_advance_a:
            pos_a += 1
        else:
            pos_b -= 1
            
        # Collision check
        if pos_a == pos_b:
            # Duel phase (0: Rock, 1: Paper, 2: Scissors)
            # A wins if (a - b) % 3 == 1
            winner = None
            while winner is None:
                move_a = np.random.choice([0, 1, 2], p=probs_a)
                move_b = np.random.choice([0, 1, 2], p=probs_b)
                
                if move_a == move_b:
                    continue
                elif (move_a - move_b) % 3 == 1:
                    winner = 'A'
                else:
                    winner = 'B'
            
            # Reset loser
            if winner == 'A':
                pos_b = n_cells - 1
            else:
                pos_a = 0
        
        # Winning condition
        if pos_a >= n_cells - 1:
            return 'A', turns
        if pos_b <= 0:
            return 'B', turns

def run_experiment_1(min_size=4, max_size=20, iterations=50):
    results = []
    for size in range(min_size, max_size + 1):
        durations = [simulate_game(size)[1] for _ in range(iterations)]
        results.append({'Board Size': size, 'Avg Duration': np.mean(durations)})
    return pd.DataFrame(results)

def run_experiment_2(n_cells=10, iterations=100):
    p_rocks = np.linspace(0, 1, 11)
    win_rates = []
    for p in p_rocks:
        wins = sum(1 for _ in range(iterations) if simulate_game(n_cells, p_rock_a=p)[0] == 'A')
        win_rates.append({'P(Rock)_A': p, 'Win Rate A': wins / iterations})
    return pd.DataFrame(win_rates)

def run_experiment_3(n_cells=10, iterations=100):
    p_advances = np.linspace(0, 1, 11)
    results = []
    for p in p_advances:
        wins_a = sum(1 for _ in range(iterations) if simulate_game(n_cells, p_advance_a=p)[0] == 'A')
        results.append({'P(Advance)_A': p, 'Win Rate A': wins_a / iterations, 'Win Rate B': 1 - (wins_a / iterations)})
    return pd.DataFrame(results)

if __name__ == "__main__":
    sns.set_theme()
    print("Running Experiment 1...")
    df1 = run_experiment_1()
    print(df1)
