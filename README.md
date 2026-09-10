# Markov Decision Process (MDP)

A simple Python implementation of a **Markov Decision Process (MDP)** using the **Value Iteration** algorithm.

## Overview

This project demonstrates decision-making in a simple **Weather & Commute** scenario. The agent observes the current weather and chooses between **Walk** and **Bus** to maximize long-term rewards.

## MDP Components

**States:** `Sunny`, `Rainy`
**Actions:** `Walk`, `Bus`
**Discount Factor:** `γ = 0.9`

**Rewards:**

| Weather | Walk | Bus |
| ------- | ---: | --: |
| Sunny   |  +10 |  +2 |
| Rainy   |  -10 |  +5 |

**Transition Probabilities:**

| Current Weather | Sunny | Rainy |
| --------------- | ----: | ----: |
| Sunny           |   0.8 |   0.2 |
| Rainy           |   0.4 |   0.6 |

## Value Iteration

The program calculates the expected long-term value of each action using the Bellman Optimality Equation:

$$
V(s)=\max_a[R(s,a)+\gamma\sum_{s'}P(s'|s,a)V(s')]
$$

The algorithm repeatedly updates the state values and then selects the action with the highest expected value.

## Functions

`calculate_value()` calculates the value of an action using rewards, transition probabilities, the discount factor, and future state values. `value_iteration()` calculates the state values, while `get_policy()` uses those values to determine the optimal action for each state.

## How to Run

No external libraries are required. Make sure Python is installed and run:

```bash
python mdp.py
```

## Output

```text
Markov Decision Process

Calculated State Values:
Sunny = 56.88
Rainy = 49.07

Optimal Policy:
Sunny → Walk
Rainy → Bus
```

## Project Structure

```text
Markov-Decision-Process/
├── mdp.py
└── README.md
```

## Technologies

**Python • Markov Decision Process • Value Iteration**
