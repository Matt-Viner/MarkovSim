import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from state import State
from agent import Agent

def main():
    # Main Loop
    # Defining two distributions with some slight overlap, both with normal distribution for simplicity
    norm_dist1 = np.random.normal(0.0, 1, 1000)
    norm_dist2 = np.random.normal(3.0, 1, 1000)

    A = State('A', norm_dist1)
    B = State('B', norm_dist2)

    # Basic simulation, Agent steps between two states and takes a random value from the state distribution
    # Initial state chosen at random
    state_list = [A, B]
    initial_state = random.choice(state_list)
    agent = Agent(initial_state)

    # Create empty list
    values_list = []

    while len(values_list) < 100:
        # Agent picks a random value from the distribution of the State it is in, appends to list
        values_list.append(agent.pick_value())

        # If the Agent is in state A, change to B. If in state B, change to A.
        if agent.get_state == A:
            agent.change_state(B)
        else:
            agent.change_state(A)
    
    # Plot the values that the Agent samples from each state
    plt.plot(values_list)
    plt.show()

if __name__ == "__main__":
    main()