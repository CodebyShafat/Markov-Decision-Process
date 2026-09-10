states = ["Sunny", "Rainy"]
actions = ["Walk", "Bus"]

# Rewards
rewards = {
    "Sunny": {"Walk": 10, "Bus": 2},
    "Rainy": {"Walk": -10, "Bus": 5}
}

# Transition probabilities
transitions = {
    "Sunny": {"Sunny": 0.8,
              "Rainy": 0.2
            },
    "Rainy": {"Sunny": 0.4,
              "Rainy": 0.6
              }
}

gamma = 0.9


# Calculate the value of an action
def calculate_value(state, action, values):
    value = rewards[state][action]

    for next_state in states:
        value += (
            gamma
            * transitions[state][next_state]
            * values[next_state]
        )

    return value


# Value Iteration
def value_iteration():
    values = {
        "Sunny": 0,
        "Rainy": 0
    }

    for i in range(10):
        new_values = {}

        for state in states:
            best_value = -999

            for action in actions:
                value = calculate_value(state, action, values)

                if value > best_value:
                    best_value = value

            new_values[state] = best_value

        values = new_values

    return values


# Find the best action
def get_policy(values):
    policy = {}

    for state in states:
        best_action = ""
        best_value = -999

        for action in actions:
            value = calculate_value(state, action, values)

            if value > best_value:
                best_value = value
                best_action = action

        policy[state] = best_action

    return policy


# Run MDP
values = value_iteration()
policy = get_policy(values)


# Display results
print("Markov Decision Process")

print("\nCalculated State Values:")
for state in states:
    print(state, "=", round(values[state], 2))

print("\nOptimal Policy:")
for state in states:
    print(state, "->", policy[state])