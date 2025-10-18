from collections import defaultdict
import numpy as np
import random


class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.3):
        self.alpha = alpha      # learning rate
        self.gamma = gamma      # gamma for Q-learning
        self.epsilon = epsilon  # probability of random action
        self.Q = defaultdict(lambda: [0.0, 0.0])  # actions: [stand, hit]

    def choose_action(self, state, explore=True):
        """ choose action based on state and epsilon-greedy policy"""
        if explore and random.random() < self.epsilon:
            return random.choice([0, 1])
        else:
            return int(np.argmax(self.Q[state]))

    def update(self, state, action, reward, next_state, done):
        """ update Q-value by Q-learning formula"""
        best_next = 0 if done else max(self.Q[next_state])
        td_target = reward + self.gamma * best_next
        td_error = td_target - self.Q[state][action]
        self.Q[state][action] += self.alpha * td_error

class DealerAgent:
    def choose_action(self, state, explore=False):
        player_sum, _, _, _ = state
        return 1 if player_sum < 17 else 0  # Hit while <17