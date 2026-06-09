# Rayuela Mortal: Stochastic Simulation & Analysis 🎲

A high-performance Python simulation of the "Rayuela Mortal" game, refactored with **NumPy** and **Pandas** to analyze game dynamics, probabilistic strategies, and board scaling.

## 🔬 Mathematical Model

The game can be modeled as a **Discrete-Time Markov Chain (DTMC)** with absorbing states. 

### 1. State Space
The state is defined by the positions of Team A ($x_a$) and Team B ($x_b$) on a board of length $L$:
$$S = \{ (x_a, x_b) \in \mathbb{Z}^2 : 0 \le x_a \le x_b \le L-1 \}$$

### 2. Transition Rules
In each turn $t$, a movement occurs based on the probability $P(A_{adv})$:
- Team A moves: $(x_a, x_b) \to (x_a + 1, x_b)$
- Team B moves: $(x_a, x_b) \to (x_a, x_b - 1)$

### 3. The Collision Constraint
A collision occurs when $x_a = x_b$. The conflict is resolved via a duel (Rock-Paper-Scissors). Let $W$ be the winner:
- If $W=A$, then $x_b \to L-1$ (Team B is reset).
- If $W=B$, then $x_a \to 0$ (Team A is reset).

### 4. Absorbing States (Winning)
The game ends when:
- $x_a = L-1$ (Victory for A)
- $x_b = 0$ (Victory for B)

## 🛠️ Features
- **Vectorized Simulations**: Optimized using NumPy for thousands of iterations.
- **Data Analysis**: Pandas-driven experiment management.
- **Visualization**: Professional charts using Seaborn and Matplotlib.
- **Jupyter Integration**: Comprehensive analysis available in `Rayuela_Mortal_Analysis.ipynb`.

## 🚀 Getting Started

### Installation
```bash
pip install -r requirements.txt
```

### Running Simulations
You can run the base experiments directly from the script:
```bash
python main.py
```
Or explore the detailed analysis in the Jupyter Notebook.

## 📊 Key Insights
1. **Board Scaling**: The expected game length $E[T]$ grows super-linearly with board size $L$ due to the high penalty of resets.
2. **Strategy Neutrality**: Biasing Rock-Paper-Scissors moves against a random opponent does not deviate the win rate from the 50/50 equilibrium.
3. **Kinetic Dominance**: Movement probability $P(A_{adv})$ is the primary determinant of victory.

## 👥 Contributors
- Joaquín Bustamante
- Lisa Muñoz
